from django.shortcuts import redirect, render
from gedus.issues.forms import IssuesForm
from gedus.issues.models import Postuler, Issues
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, template_name="ense_index.html")


def app_print(request, id):
    context = {}

    try:
        postule = Postuler.objects.filter(
            problematique__entreprise=request.user.entreprise
        ).get(id=id)
        context["postule"] = postule
    except Exception as e:
        print(e)

    print(context)

    return render(request, "application_print.html", context)


def premium_request(request):
    return render(request, template_name="premium_request.html")



###-----------------------PROBLEMATIQUE------------------------###


def problematique_create(request):
    context = {"form": IssuesForm}
    try:
        if request.method == "POST":
            form = IssuesForm(request.POST)
            publish_date = request.POST.get("publish_date")
            duree_recherche = request.POST.get("duree_recherche")
            titre = request.POST.get("titre")
            domaine = request.POST.get("domaine")
            active = bool(request.POST.get("active"))
            draft = bool(request.POST.get("is_draft"))
            user = request.user.entreprise

            if form.is_valid():
                description = form.cleaned_data["description"]
                profil_rechercher = form.cleaned_data["profil_rechercher"]

            article = Issues.objects.create(
                entreprise=user,
                domaine=domaine,
                active=active,
                is_draft=draft,
                duree_recherche=duree_recherche,
                publish_date=publish_date,
                description=description,
                profil_rechercher=profil_rechercher,
                titre=titre,
            )
            print(article)
            return redirect("/entreprise/prob-list/")

    except Exception as e:
        print(e)

    return render(request, "prob_create.html", context)


def problematique_read(request, slug):
    context = {}
    try:
        article_obj = Issues.objects.filter(slug=slug).first()
        context["article_obj"] = article_obj
    except Exception as e:
        print(e)
    return render(request, "prob_read.html", context)


def problematique_update(request, slug):
    context = {}
    try:
        issues = Issues.objects.get(slug=slug)

        if issues.entreprise != request.user.entreprise:
            return redirect("/")

        form = IssuesForm(instance=issues)
        if request.method == "POST":
            form = IssuesForm(request.POST, instance=issues)

            if form.is_valid():
                form.save()
            return redirect("/entreprise/prob-list/")

        context["issues"] = issues
        context["form"] = form
    except Exception as e:
        print(e)

    return render(request, "prob_update.html", context)


def problematique_delete(request, id):
    try:
        issues = Issues.objects.get(id=id)

        if issues.entreprise == request.user.entreprise:
            issues.delete()

    except Exception as e:
        print(e)

    return redirect("/entreprise/prob-list/")


def problematique_list(request):
    context = {}

    try:
        issues = Issues.objects.filter(
            entreprise=request.user.entreprise, is_draft=False, active=True
        )
        context["issues"] = issues
    except Exception as e:
        print(e)

    print(context)
    return render(request, "prob_list.html", context)


def problematique_draft(request):
    context = {}

    try:
        issues = Issues.objects.filter(
            entreprise=request.user.entreprise, is_draft=True, active=False
        )
        context["issues"] = issues
    except Exception as e:
        print(e)

    print(context)
    return render(request, "prob_draft.html", context)


###-----------------------PROBLEMATIQUE TERMINE------------------------###



###-----------------------POSTULER A UNE PROBLEMATIQUE------------------------###


def postule_list(request):
    context = {}

    try:
        postule = Postuler.objects.filter(
            problematique__entreprise=request.user.entreprise
        )
        context["postule"] = postule
    except Exception as e:
        print(e)

    print(context)
    return render(request, "postule_list.html", context)


def postule_read(request, id):
    context = {}

    try:
        postule = Postuler.objects.filter(
            problematique__entreprise=request.user.entreprise
        ).get(id=id)
        context["postule"] = postule
    except Exception as e:
        print(e)

    print(context)
    return render(request, "postule_read.html", context)


###-----------------------POSTULER A UNE PROBLEMATIQUE TERMINE------------------------###
