from django.shortcuts import render, redirect
from main.models.article import Article, CouponCode
from main.models.paiement import Payment
from main.models.user_article import UserArticle
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from togotulawo.settings import *
from time import time
import requests


# @api_view(('GET', 'POST'))
@login_required(login_url="account:login")
def checkout(
    request,
    slug,
):
    article = Article.objects.get(slug=slug)
    user = request.user
    couponcode = request.GET.get("couponcode")
    coupon_code_message = None
    coupon = None
    order = None
    phone = request.POST.get("phone_number")
    network = request.POST.get("network")
    tx_reference = request.GET.get("tx_reference")
    payment = None
    error = None
    amount = None
    url = requests.get("http://togotulawo.com/verify_payment")

    try:
        user_article = UserArticle.objects.get(user=user, article=article)
        error = "Ce document existe déjà dans votre bibliothèque, la voir"
    except:
        pass

    if error is None:
        amount = int((article.price - (article.price * article.discount * 0.01)))
    # if amount is zero dont create paymenty , only save emrollment object

    if couponcode:
        print("COUPONCODE ", couponcode)
        try:
            coupon = CouponCode.objects.get(article=article, code=couponcode)
            amount = article.price - (article.price * coupon.discount * 0.01)
            amount = int(amount) * 100
            print("AMOUNT", amount)
        except:
            coupon_code_message = "Code Coupon Invalide"
            print("coupon code invalid")

    # is the amount is zero dont create payment
    if amount == 0:
        article_user = UserArticle(user=user, article=article)
        article_user.save()
        return redirect("main:bibliotheque")

        # enroll direct
    order = f"togotulawo-{int(time())}"

    # save the payment
    payment = Payment()
    payment.user = user
    payment.article = article
    payment.order_id = order
    payment.payment_id = tx_reference
    payment.phone_number = phone
    payment.network = network
    payment.save()

    # Paymen with paygate API
    if request.method == "POST":
        url = "https://paygateglobal.com/api/v1/pay"
        payload = {
            "auth_token": "2a2b0731-8259-40e3-8df0-26df05801e0e",
            "phone_number": request.POST.get("phone_number"),
            "amount": amount,
            "description": "Achat de document",
            "identifier": order,
            "network": request.POST.get("network"),
        }

        # initiate a request to PayGate
        # and retrieve the referenece id of the transaction
        # initiated by PayGate
        r = requests.post(url, data=payload)
        if r.status_code == 200:
            data = r.json()
            print(data)
            # client.utility.verify_payment_signature(data)
            paygate_tx_reference = data["tx_reference"]
            tx_status_url = "https://paygateglobal.com/api/v1/status"
            url_data = {
                "auth_token": "2a2b0731-8259-40e3-8df0-26df05801e0e",
                "tx_reference": paygate_tx_reference,
            }


            # iniatiate a request to PayGate
            # to retrieve the status of confirmation
            # of the transaction confirmation
            # from The mobile money operator and retrieve the
            # transaction Id
            url_r = requests.post(tx_status_url, data=url_data)
            if url_r.status_code == 200:
                # get the response from the API
                status_data = url_r.json()
                # check the transaction status and
                # perform tasks accordingly
                # status code -> 0 : Paiement réussi avec succès, 2 : En cours, 4 : Expiré, 6: Annulé
                while status_data["status"] == 2:
                    print("waiting for validation of payment from client")
                    url_r = requests.post(tx_status_url, data=url_data)
                    if url_r.status_code == 200:
                        # get the response from the API
                        status_data = url_r.json()
                    print(status_data["status"])

            tx_payment_reference = status_data["payment_reference"]

            payment = Payment.objects.get(order_id=order)
            payment.paygate_payment_id = paygate_tx_reference
            payment.payment_reference = tx_payment_reference
            payment.status = not bool(status_data["status"])

            userArticle = UserArticle(user=payment.user, article=payment.article)
            userArticle.save()

            print("Userarticle", userArticle.id)

            payment.user_article = userArticle
            payment.save()

            return redirect("main:bibliotheque")
         
            # return Response(data, status=status.HTTP_200_OK)

            # return HttpResponse("Détails de paiement invalides")
        # return Response({"error": "Request failed"}, status=r.status_code)

    context = {
        "article": article,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error,
        "coupon": coupon,
        "coupon_code_message": coupon_code_message,
        "url": url,
    }
    return render(request, template_name="checkout.html", context=context)


@login_required(login_url="account:login")
@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        try:
            # client.utility.verify_payment_signature(data)
            paygate_tx_reference = data["tx_reference"]
            # paygate_payment_reference = data['payment_reference']

            payment = Payment.objects.get(order_id=paygate_tx_reference)
            payment.payment_id = paygate_tx_reference
            payment.status = True

            userArticle = UserArticle(user=payment.user, article=payment.article)
            userArticle.save()

            print("Userarticle", userArticle.id)

            payment.user_article = userArticle
            payment.save()

            return redirect("main:bibliotheque")

        except:
            return HttpResponse("Détails de paiement invalides")
