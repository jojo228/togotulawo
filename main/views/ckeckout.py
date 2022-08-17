from django.shortcuts import render, redirect
from main.models.article import Article, CouponCode
from main.models.paiement import Payment
from main.models.user_article import UserArticle
from main.models.video import Video
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



@api_view(('GET', 'POST'))
@login_required(login_url='/account/login')
def checkout(request, slug,): 
    article = Article.objects.get(slug=slug)
    user = request.user
    couponcode = request.GET.get('couponcode')
    coupon_code_message = None
    coupon = None
    order = None
    phone = request.POST.get("phone_number")
    network = request.POST.get("network")
    payment = None
    error = None
    amount = None
    url = requests.get('http://localhost:8000/verify_payment')
    
    try:
        user_article = UserArticle.objects.get(user=user, article=article)
        error = "Ce document existe déjà dans votre bibliothèque"
    except:
        pass
    
    if error is None:
        amount = int(
            (article.price - (article.price * article.discount * 0.01)) * 100)
   # if amount is zero dont create paymenty , only save emrollment object

    if couponcode:
        print("COUPONCODE ", couponcode)
        try:
            coupon = CouponCode.objects.get(article=article, code=couponcode)
            amount = article.price - (article.price * coupon.discount * 0.01)
            amount = int(amount) * 100
            print("AMOUNT", amount)
        except:
            coupon_code_message = 'Code Coupon Invalide'
            print('coupon code invalid')

    if amount == 0:
        article_user = UserArticle(user=user, article=article)
        article_user.save()
        return redirect('bibliotheque')

        # enroll direct
    order=f"togotulawo-{int(time())}"
    
    #save the payment
    payment = Payment()
    payment.user = user
    payment.article = article
    payment.order_id = order
    payment.phone_number = phone
    payment.network = network
    payment.save()
    
    #Paymen with paygate API
    if request.method == "POST":
        
        url = 'https://paygateglobal.com/api/v1/pay'
        payload = {'auth_token': '2a2b0731-8259-40e3-8df0-26df05801e0e',
                   'phone_number': request.POST.get("phone_number"),
                    'amount': amount,
                    'description': "Achat de document",
                    'identifier': order,
                    'network': request.POST.get("network")}
        print(payload)
        r = requests.post(url, data= payload)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"error": "Request failed"}, status=r.status_code)
    

    context = {
        "article": article,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error,
        'coupon': coupon,
        "coupon_code_message": coupon_code_message,
        'url': url,
        
       
    }
    return render(request, template_name="checkout.html", context=context)


@login_required(login_url='/account/login')
@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            # client.utility.verify_payment_signature(data)
            paygate_tx_reference = data['tx_reference']
            paygate_payment_reference = data['payment_reference']

            payment = Payment.objects.get(order_id=paygate_tx_reference)
            payment.payment_id = paygate_payment_reference
            payment.status = True

            userArticle = UserArticle(user=payment.user, article=payment.article)
            userArticle.save()

            print("Userarticle",  userArticle.id)

            payment.user_article = userArticle
            payment.save()

            return redirect('my-articles')

        except:
            return HttpResponse("Détails de paiement invalides")



