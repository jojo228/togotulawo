from django.shortcuts import redirect, render
from entreprise.models import Problematique
from main.models.article import Article, Categorie
from django.contrib import messages
from django.core.paginator import Paginator
from main.forms.newletter import SubscibersForm


def home_page(request):
    article = Article.objects.filter(active=True, is_draft=False,)
    paginator = Paginator(article, 15)  # Show 15 articles per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    category = Categorie.objects.all()

    problematique = Problematique.objects.filter(is_draft=False, active=True)
    
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()

    context = {'article': article, 'category': category, 'prob': problematique, 'page_obj': page_obj, 'form': form,}

    return render(request, template_name = "main_base.html", context=context)





