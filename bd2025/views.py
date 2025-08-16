from datetime import datetime

from django.shortcuts import render
from .models import Member, Parcelle, Affectation, Jardin


def index(request):
    return render(request, "index.html")


def inscription(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date_nis = request.POST.get("datenis")
        genre = request.POST.get("genre")
        password = request.POST.get("password")
        verify_password = request.POST.get("verify")

        if password != verify_password:
            return render(request, "success.html", {"error": "verify password should be same password"})

        mem = Member.objects.filter(email=email)
        if mem:
            return render(request, "success.html", {"error": "Email existe deja dans db"})


        v = Member.objects.create(
            nomMem=name,
            genre=genre,
            dateNais=date_nis,
            email=email,
            mdp=password
        )
        print(v)
        mem = Member.objects.get(email=email)

        return render(request, "success.html", {"msg": "Inscription réussie", "valeur_générée": mem.idMem})
    return render(request, "inscription.html")


def affectation(request):
    if request.method == "POST":
        idmem = request.POST.get("idmem")
        idpar = request.POST.get("idpar")
        date = request.POST.get("date")

        mem = Member.objects.filter(idMem=idmem)
        if mem is None:
            return render(request, "success.html", {"error": "Member inexistant"})
        par = Parcelle.objects.filter(idPar=idpar)
        if par:
            return render(request, "success.html", {"error": "Affectation existante"})

        Affectation.objects.create(
            idMem=idmem,
            idPar=idpar,
            date=date# datetime.now()
        )
        return render(request, "success.html", {"error": "Affectation réussie"})

    return render(request, "affectation.html")
