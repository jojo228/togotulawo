from django.shortcuts import render, redirect
from main.models.article import Article, CouponCode
from main.models.paiement import Payment
from main.models.user_article import UserArticle
from main.models.video import Video
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from togotulawo.settings import *
from time import time
import requests




@login_required(login_url='/login')
def checkout(request, slug,):
    article = Article.objects.get(slug=slug)
    user = request.user
    couponcode = request.GET.get('couponcode')
    coupon_code_message = None
    coupon = None
    order = None
    payment = None
    error = None
    url = requests.get('http://localhost:8000/verify_payment')
    
    try:
        user_article = UserArticle.objects.get(user=user, article=article)
        error = "You are Already Enrolled in this article"
    except:
        pass
    amount = None
    if error is None:
        amount = int(
            (article.price - (article.price * article.discount * 0.01)) * 100)
   # if ammount is zero dont create paymenty , only save emrollment obbect

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
        userArticle = UserArticle(user=user, article=article)
        userArticle.save()
        return redirect('my-articles')

        # enroll direct
    order=f"togotulawo-{int(time())}"
    
    
    payment = Payment()
    payment.user = user
    payment.article = article
    payment.order_id = order
    payment.save()

    context = {
        "article": article,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error,
        'coupon': coupon,
        "coupon_code_message": coupon_code_message,
        'url':url,
       
        
    }
    return render(request, template_name="checkout.html", context=context)


@login_required(login_url='/login')
@csrf_exempt
def verifyPayment(request):
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
            return HttpResponse("Invalid Payment Details")



