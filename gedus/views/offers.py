from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main.forms.postuler import PostuleForm
from entreprise.models import Postuler, Issues
from django.views.generic import ListView


class OfferList(ListView):
    model = Issues
    context_object_name = "prob"
    template_name = "ense_offers.html"
    paginate_by = 12

    def get_queryset(self):
        issues = Issues.objects.filter(is_draft=False, active=True)
        return issues


def offer_detail(request, slug):
    issues = Issues.objects.get(slug=slug)

    context = {
        "prob": issues,
    }

    return render(request, template_name="offer_detail.html", context=context)


@login_required(login_url="account:login")
def offer_create(request, id):
    prob = Issues.objects.get(id=id)
    context = {"form": PostuleForm, "prob": prob}
    try:
        if request.method == "POST":
            form = PostuleForm(request.POST)

            if form.is_valid():
                data = Postuler()
                data.nom_du_candidat = form.cleaned_data["nom_du_candidat"]
                data.prenom_du_candidat = form.cleaned_data["prenom_du_candidat"]
                data.contact_du_candidat = form.cleaned_data["contact_du_candidat"]
                data.email_du_candidat = form.cleaned_data["email_du_candidat"]
                data.motivation_du_candidat = form.cleaned_data[
                    "motivation_du_candidat"
                ]
                data.problematique_id = id
                data.save()

            return redirect("/gedus/success-message/")

    except Exception as e:
        print(e)

    return render(request, "offer_create.html", context)


@login_required(login_url="account:login")
def success_message(request):
    return render(request, template_name="succes_message.html")
