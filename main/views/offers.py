from django.shortcuts import redirect, render
from entreprise.forms import PostuleForm
from entreprise.models import Problematique
from django.views.generic import ListView


class OfferList(ListView):

    model = Problematique
    context_object_name = "prob"
    template_name = 'ense_offers.html'
    paginate_by = 12

    def get_queryset(self):
        problematique = Problematique.objects.filter(
            is_draft=False, active=True)
        return problematique


def offer_detail(request, slug):

    problematique = Problematique.objects.get(slug=slug)

    context = {
        "prob": problematique,
    }

    return render(request, template_name="offer_detail.html", context=context)


def offer_create(request, slug):
    prob = Problematique.objects.get(slug=slug)
    context = {'form': PostuleForm, 'prob':prob}
    try:
        if request.method == 'POST':
            form = PostuleForm(request.POST, instance=prob)

            if form.is_valid():
                form.save()

            return redirect('/success-message/' )

    except Exception as e:
        print(e)

    return render(request, 'offer_create.html', context)



def success_message(request):

    return render(request, template_name = "succes_message.html")




