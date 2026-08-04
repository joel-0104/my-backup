#EXO1
#1
age=int(input("entrez votre age :"))
if age >= 18 :
    print("Vous êtes assez âgé pour apprendre à conduire.")
else:
    print(f"Il vous reste {18-age} ans à attendre pour apprendre à conduire.")
#2

my_age=19
your_age=int(input("entrez votre age :"))
deci=my_age-your_age
if deci >=0:
    if deci==1:
        print(f"vous avez {deci} an de moins que moi")
    elif deci==0:
        print("nous avons le meme age")  
    else :
        print(f"vous avez {deci} ans de moins que moi")
else:
    if abs(deci)==1:
        print(f"vous avez 1 an de plus que moi")
    else:
        print(f"vous avez {abs(deci)} ans de plus que moi")

#3
a=int(input("entrer a :"))
b=int(input("entrer b :"))
if a > b:
    print(f"{a} est plus grand que {b}")
elif b > a:
    print(f"{a} est plus petit que {b}")
elif a==b:
    print(f"{a} est egal a {b}")

#EXO2
print("\n")
#1
note=int(input("entrez votre note(comprise entre 0-100): "))
if note >=90 and note <=100:
    print(f"la note correspondant au score {note} est A")
elif note >=80 and note <=89:
    print(f"la note correspondant au score {note} est B")
elif note >=70 and note <=79:
    print(f"la note correspondant au score {note} est C")
elif note >=60 and note <=69:
    print(f"la note correspondant au score {note} est D")
elif note >=0 and note <=59:
    print(f"la note correspondant au score {note} est F")
#2

month=input("veuillez entrer un moi: ")
month=month.lower()
month=month.capitalize()
if month=="Septembre" or month=="Octobre" or month=="Novembre":
    print(f"la saison correspondante à {month} est : Automne")
elif month=="Decembre" or month=="Janvier" or month=="Février":
    print(f"la saison correspondante à {month} est: L'Hiver")
elif month=="Mars" or month=="Mai" or month=="Avril":
    print(f"la saison correspondante à {month} est: Le printemps")
elif month=="Juin" or month=="Juillet" or month=="Août":
    print(f"la saison correspondante à {month} est: L'Été")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
new_fruit=input("Entrer le nom d'un fruit: ")
if new_fruit in fruits:
    print("Ce fruit existe déjà dans la liste")
else:
    fruits.append(new_fruit)
    print(fruits)

#EXO3
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person :
    if len(person['skills'])%2==1:
        indx_mid=len(person['skills'])//2
        print(f"l'element au milieux du tableau des compétences est : {person['skills'][indx_mid]}")
    elif len(person['skills'])%2==0:
            indx_mid=len(person['skills'])//2
            print(f"les élément au milieux du tableau des compétences sont : {person['skills'][indx_mid-1:indx_mid+1]}")
    print(f"c'ette personne a t'elle une compétence python ? :{'Python'in person['skills']}")

    skills = set(person['skills'])

    # Si la personne n'a QUE JavaScript et React
    if skills == {'JavaScript', 'React'}:
        print('Il est développeur front-end')
    
    # Si la personne a React, Node ET MongoDB (Full-stack)
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('Il est développeur full-stack')
        
    # Si la personne a Node, Python ET MongoDB (Back-end)
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('Il est développeur back-end')
        
    else:
        print('unknown title')

# 2. Vérification de la situation maritale et du pays
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vit en {person['country']}. Il est marié.")