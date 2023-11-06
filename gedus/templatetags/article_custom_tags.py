from django import template
import math

from gedus.main.models import UserArticle 
register = template.Library()

# 100 -> 10% --> mrp  - ( mrp * discount * 0.01 ) = selprice
@register.simple_tag
def cal_sellprice(price , discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    sellprice = price - ( price * discount * 0.01 )
    return math.floor(sellprice)


@register.filter
def cfa(price):
    return f'{price}f cfa'




@register.simple_tag
def is_enrolled(request , article):
   
    user = None
    if not request.user.is_authenticated:
        return False
        # i you are enrooled in this article you can watch every video
    user = request.user
    try:
        user_article = UserArticle.objects.get(user = user  , article = article)
        return True
    except:
        return False

