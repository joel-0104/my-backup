import math
age=19
taille=1.89
comp=1+1j
#AIRE DU TRIANGLE
base=float(input("entrez la base du triangle"))
hauteur=float(input("entrez la hauteur du triangle"))
aire=0.5*base*hauteur
print("l'aire du triangle est:",aire)

#PERIMETRE DU TRIANGLE
cote_a=float(input("entrez le coté a:"))
cote_b=float(input("entrez le coté b:"))
cote_c=float(input("entrez le coté c:"))
peri=cote_a+cote_b+cote_c
print("le perimetre du triangle est:",peri)

#rectangle
eight=float(input("entrez la longueur du rectangle:"))
width=float(input("entrez la largeur du rectangle:"))
peri_rect=2*(eight+width)
aire_rect=eight*width
print("le perimetre du rectanle est:",peri_rect)
print("l'aire du rectangle est:",aire_rect)

#CERCLE
pi=math.pi
radius=float(input("entrez le rayon du cercle:"))
aire_cer=pi*(radius**2)
peri_cer=2*pi*radius
print("le perimetre du cercle est:",peri_cer)
print("l'aire du cercle est:",aire_cer)

#VALEUR PENTE 1
x_1,x_2=0,1
y_1=2*x_1-2
y_2=2*x_2-2
pente_a=(y_2-y_1)/(x_2-x_1)
print("la pente est a=",pente_a)
y_0=-2
x_0=1
print("l'ordonné a l'origine est y0=",y_0)
print("l'abscisse a l'origine est x0=",x_0)

#valeur pente 2
x1,x2=2,6
y1,y2=2,10
m= (y2-y1)/(x2-x1)
distance_euc=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("la pente est pente2=",m)
print('la distance euclidienne est :',distance_euc)

#comparaison
print("pente a est t'elle eguale a la pente b?",pente_a == m)


#12
print("la longueur du mot python est :",len("python"))
print("la longueur du mot dragon est :",len("dragon"))

#13 
print("on se trouve t'il dans les mots precedent?","on"in"python" and "on"in "dragon")

#14
phrase="I hope this course is not full of jargon"
print("jargon se trouve t'il dans",phrase,"?","jargon"in phrase)

#15
print('on'not in"python" and "on" not in "dragon")
#16
longpy=len("python")
longpy1=float(longpy)
longpy2=str(longpy1)
print(longpy2)

# parité 
nbre=int(input("entrer un entier:"))
parité=nbre%2 == 0
print(nbre,"est t'il paire?",parité)

#18
print("18:",7//3 == int(2.7))

#19
print("le type de '10' est-t'il  egal au type de 10?",type("10")== type(10))

#20
lol=float("9.8")
print("(int('9.8)) est-t'il egal a 10?",int(lol)== 10)

#21
heurs=float(input("entrez le nombres d'heures:"))
taux=float(input("entrez le taux horraire"))
print("votre salaire hebdomadaire est:",heurs*taux)

#22
année=int(input("entrez le nombres d'annees vecue:"))
print("vous avez vécu",31536000*année,"secondes")
#23
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
