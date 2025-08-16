# Gestion-des-Jardins-Communautaires-with-Django

<p>
  Dans le but de favoriser les interactions sociales et de soutenir la préservation de l’environnement, la
municipalité d’une ville envisage de réaliser un projet qui permettrait à un groupe d’habitants de participer
d’une manière collaborative à l’entretien des jardins publics. Chaque jardin est composé de 4 parcelles et
chaque habitant participant au projet sera chargé de l’entretien d’une ou de plusieurs parcelles.
Pour ce faire, on demande de créer la partie du site Web permettant de réaliser les opérations suivantes :
  
 Inscription d’un membre (habitant).

 Affectation d’une parcelle d’un jardin à un membre.
  
</p>

<p>
jardin (idJar, nomJar, adresse)<br>
parcelle (idPar, numPar, idJar#)<br>
membre (idMem, nomMem, genre, dateNais, email, mdp)<br>
affectation (idMem#, idPar#, dateDeb)<br>
  
</p>
