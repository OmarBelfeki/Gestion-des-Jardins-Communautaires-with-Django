from django.db import models


class Jardin(models.Model):
    idJar = models.CharField(max_length=2, primary_key=True, help_text="Identifier d'un jardin")
    nomJar = models.CharField(max_length=50, help_text="Nom d'un description")
    adresse = models.CharField(max_length=50, help_text="Adresse d'un jardin")

    def __str__(self):
        return f"{self.idJar}"


class Parcelle(models.Model):
    idPar = models.CharField(auto_created=True, primary_key=True, help_text="Identifiant d’une parcelle d’un jardin.")
    numPar = models.IntegerField(help_text="Numéro d’une parcelle d’un jardin.")
    idJar = models.ForeignKey(Jardin, on_delete=models.CASCADE, help_text="Identifiant d’un jardin.")

    def __str__(self):
        return f"{self.numPar}"


class Member(models.Model):
    class Choice(models.TextChoices):
        F = 0, "Women"
        M = 1, "Men"

    idMem = models.IntegerField(auto_created=True, primary_key=True, help_text="Identifiant d’un membre.")
    nomMem = models.CharField(max_length=50, help_text="Nom et prénom d’un membre.")
    genre = models.CharField(max_length=1, choices=Choice.choices , help_text="Genre d’un membre : 'M' pour Masculin et 'F' pour Féminin.")
    dateNais = models.DateField(help_text="Date de naissance d’un membre.")
    email = models.CharField(max_length=50, unique=True, help_text="Adresse email d’un membre.")
    mdp = models.CharField(max_length=6, help_text="Mot de passe d’un membre.")

    def __str__(self):
        return f"{self.idMem}"


class Affectation(models.Model):
    idPar = models.ForeignKey(Parcelle, on_delete=models.CASCADE, help_text="Identifiant d’un Parcelle.")
    idMem = models.ForeignKey(Member, on_delete=models.CASCADE, help_text="Identifiant d’un Memebr.")
    dateDep = models.DateField(help_text="Date de début de l’affectation d’une parcelle à un membre")

    def __str__(self):
        return f"{self.dateDep}"


