from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models.article import Article, Comment
from main.forms.comment import CommentForm
from main.models.video import Video
from main.models.user_article import UserArticle
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q



# @method_decorator(login_required(login_url='login') , name='dispatch')
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 12

    def get_queryset(self):
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val!="":
            article=Article.objects.filter(Q(title__contains=filter_val) | Q(contenu__contains=filter_val)).order_by(order_by)
        else:
            article=Article.objects.all().order_by(order_by)

        return article

    def get_context_data(self,**kwargs):
        context=super(ArticleList,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","id")
        context["all_table_fields"]=Article._meta.get_fields()
        return context



def articlePage(request, slug):

    article = Article.objects.get(slug=slug)

    comment = article.comment_set.all().count()
    
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
        'videos':videos,
        'comment':comment,
    }
 
    return render(request, template_name="pageArticle.html", context=context)


def comment(request, id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
                data = Comment()
                data.text = form.cleaned_data['text']
                data.rate = form.cleaned_data['rate']
                data.article_id = id
                data.client_id = request.user.client.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)