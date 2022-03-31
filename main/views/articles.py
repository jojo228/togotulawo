from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models.article import Article
from main.models.video import Video
from main.models.user_article import UserArticle
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator



@method_decorator(login_required(login_url='login') , name='dispatch')
class MyArticleList(ListView):
    template_name = 'courses/my_courses.html'
    context_object_name = 'user_article'
    def get_queryset(self):
        return UserArticle.objects.filter(user = self.request.user)



def articlePage(request, slug):

    article = Article.objects.get(slug=slug)
    serial_number  = request.GET.get('lecture')
    videos = article.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number = serial_number , article = article)


    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_article = UserArticle.objects.get(user = user  , article = article)
            except:
                return redirect("checkout" , slug=article.slug)


        
        
    context = {
        "article" : article , 
        "video" : video , 
        'videos':videos
    }
 

    
    
    return render(request, template_name="pageArticle.html", context=context)