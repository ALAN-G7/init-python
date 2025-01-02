print("j'apprend Pytohn!")
calcul=17+35*5
print(f"Resultat {calcul}")
nom="alan"
age="27"
print(f"je m'appelle {nom} et j'ai {age} ")
nom="goblin"
age= 17
taille = 1.85 
si_etudiant= True
si_sfd= False

print(f"resultat {nom} {age} {taille} {si_etudiant} {si_sfd}")
fruits=['pomme', 'anane', 'orange']
fruits[0]='kida'
print(fruits)
 
info={
    "poids":"13",
    "origine":"madagascar"
}
info['nom']="alan"
del info["origine"]
info.keys()
print(info)
 
fruit ={
  "pomme":"rouge",
  "banane":"jaune",
  "orange":"orange"
 }
cles=fruit.values()
print(cles)
fruit["kiwi"]="vert"
fruit["banane"]="couleur_banane"
