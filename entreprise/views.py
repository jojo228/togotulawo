from django.shortcuts import redirect, render
from entreprise.forms import LivreForm, ProblematiqueForm, EntrepriseForm
from entreprise.models import Livre, Postuler, Problematique
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


def entreprise_profil(request):
    user = request.user.entreprise
    form = EntrepriseForm(instance=user)

    if request.method == "POST":
        form = EntrepriseForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {"form": form}

    return render(request, "ense_profil.html", context)


###-----------------------PROBLEMATIQUE------------------------###


def problematique_create(request):
    context = {"form": ProblematiqueForm}
    try:
        if request.method == "POST":
            form = ProblematiqueForm(request.POST)
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

            article = Problematique.objects.create(
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
        article_obj = Problematique.objects.filter(slug=slug).first()
        context["article_obj"] = article_obj
    except Exception as e:
        print(e)
    return render(request, "prob_read.html", context)


def problematique_update(request, slug):
    context = {}
    try:
        problematique = Problematique.objects.get(slug=slug)

        if problematique.entreprise != request.user.entreprise:
            return redirect("/")

        form = ProblematiqueForm(instance=problematique)
        if request.method == "POST":
            form = ProblematiqueForm(request.POST, instance=problematique)

            if form.is_valid():
                form.save()
            return redirect("/entreprise/prob-list/")

        context["problematique"] = problematique
        context["form"] = form
    except Exception as e:
        print(e)

    return render(request, "prob_update.html", context)


def problematique_delete(request, id):
    try:
        problematique = Problematique.objects.get(id=id)

        if problematique.entreprise == request.user.entreprise:
            problematique.delete()

    except Exception as e:
        print(e)

    return redirect("/entreprise/prob-list/")


def problematique_list(request):
    context = {}

    try:
        problematique = Problematique.objects.filter(
            entreprise=request.user.entreprise, is_draft=False, active=True
        )
        context["problematique"] = problematique
    except Exception as e:
        print(e)

    print(context)
    return render(request, "prob_list.html", context)


def problematique_draft(request):
    context = {}

    try:
        problematique = Problematique.objects.filter(
            entreprise=request.user.entreprise, is_draft=True, active=False
        )
        context["problematique"] = problematique
    except Exception as e:
        print(e)

    print(context)
    return render(request, "prob_draft.html", context)


###-----------------------PROBLEMATIQUE TERMINE------------------------###


###-----------------------LIVRES------------------------###


def doc_create(request):
    context = {"form": LivreForm}
    try:
        if request.method == "POST":
            form = LivreForm(request.POST, request.FILES)

            if form.is_valid():
                livre = form.save(commit=False)
                livre.entreprise = request.user.entreprise
                livre.save()

            return redirect("/entreprise/doc-list/")

    except Exception as e:
        print(e)

    return render(request, "book_create.html", context)


def doc_read(request, slug):
    livre = Livre.objects.get(slug=slug)
    context = {"livre": livre}

    return render(request, "book_read.html", context=context)


def doc_update(request, id):
    context = {}
    try:
        livre = Livre.objects.get(id=id)

        if livre.entreprise != request.user.entreprise:
            return redirect("/")

        form = LivreForm(instance=livre)
        if request.method == "POST":
            form = LivreForm(request.POST, instance=livre)

            if form.is_valid():
                form.save()
            return redirect("/entreprise/doc-list/")

        context["livre"] = livre
        context["form"] = form
    except Exception as e:
        print(e)

    return render(request, "book_update.html", context)


def doc_delete(request, id):
    try:
        livre = Livre.objects.get(id=id)

        if livre.entreprise == request.user.entreprise:
            livre.delete()

    except Exception as e:
        print(e)

    return redirect("/entreprise/doc-list/")


def doc_list(request):
    context = {}

    try:
        livres = Livre.objects.filter(entreprise=request.user.entreprise)
        context["livres"] = livres
    except Exception as e:
        print(e)

    print(context)
    return render(request, "book_list.html", context)


###-----------------------LIVRES TERMINE------------------------###

# ---
# ---
# ---
# ---
# ---

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
