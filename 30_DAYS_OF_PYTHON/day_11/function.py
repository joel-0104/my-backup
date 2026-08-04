import math
import cmath
from countries_data import countr_data
#exo1
#1
def add_two_numbers(a,b):
    total=a+b
    return total
print(add_two_numbers(1,4))
#2
def area_of_circle(rayon):
    pi=round(math.pi,2)
    aire=pi*(rayon**2)
    return aire 
print(area_of_circle(5))
#3
def add_all_nums(*numbers):
    som=0
    for i in numbers:
        if type(i) != int and type(i) != float:
            return"Entrer un nombre!"
        som+=i
    return som

print(add_all_nums(2,3,7))
#4
def convert_celsius_to_fahrenheit(celsius):
    print("entrer la temperature en °C pour la conversion")
    far=celsius*(9/5)+32
    reslut=f"la temperature apres conrsion est : {far} °F"
    return reslut
print(convert_celsius_to_fahrenheit(10))
#5
def check_season(month):
    month=month.lower()
    month=month.capitalize()
    automne=["Septembre","Octobre","Novembre"]
    hiver=["Decembre","Janvier","Février"]
    printemps=["Mars","Mai","Avril"]
    été=["Juin","Juillet","Août"]
    if month in automne:
        return f"la saison correspondante à {month} est : Automne"
    elif month in hiver:
        return f"la saison correspondante à {month} est: L'Hiver"
    elif month in printemps:
        return f"la saison correspondante à {month} est: Le printemps"
    elif month in été:
        return f"la saison correspondante à {month} est: L'Été"

print(check_season("mars"))
#6
def calculate_slope(point1,point2):
    x1,y1=point1
    x2,y2=point2
    if x2-x1==0:
        return "pente indefinie(droite verticale)"
    pente=(y2-y1)/(x2-x1)
    pente=round(pente,2)
    return f"la pente obtenue avec les points{point1} et {point2} est : {pente}"
A=(2,5)
B=(5,7)
print(calculate_slope(A,B))

#7
def solve_quadratic_eqn(a,b,c):
    print(f"resolvons {a}X² + {b}X +{c} = 0")
    if a==0:
        return "ceci n'est pas une equation du second dégré"
    delta=math.pow(b,2)-4*a*c
    if delta<0:
        print("delta négatif solution complexes")
        X1=(-b+cmath.sqrt(delta))/(2*a)
        X2=(-b-cmath.sqrt(delta))/(2*a)
        return f"les solutions sont {X1} et {X2}"
    elif delta==0:
        print("solution double")
        X=-b/(2*a)
        return f"la solution est {X}"
    X1=(-b+math.sqrt(delta))/(2*a)
    X2=(-b-math.sqrt(delta))/(2*a)
    return f"les solutions sont {X1} et {X2}"
print(solve_quadratic_eqn(2,4,3))
#8
def print_list(liste):
    for i in liste:
        print(i)
liste=["azi","aye","lol"]
print_list(liste)
#9
def reverse_list(tab1):
    reversed_list=[]
    indx=len(tab1)-1
    for i in range(indx,-1,-1):
        reversed_list.append(tab1[i])
    return reversed_list
        
print(reverse_list(liste))
#10
def capitalize_list_items(tab2):
    cap_tab=[]
    for i in tab2:
        cap_tab.append(i.upper())
    return cap_tab
    
print(capitalize_list_items(liste))
#11
def add_item(tab3,item):
    tab3.append(item)
    return tab3
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
#12
def remove_item(tab4,item1):
    if item1 not in tab4:
        return f"{item1} n'est pas dans la liste specifié"
    tab4.remove(item1)
    return tab4
print(remove_item(liste,"lol"))
#13
def sum_of_numbers(number):
    resultat=0
    for i in range(number+1):
        resultat+=i
    return f"la somme des nombre de 0 à {number} est : {resultat}"

print(sum_of_numbers(100))
#14
def sum_of_odds(number2):
    result2=0
    for i in range(number2+1):
        if i%2==1:
            result2+=i
    return f"la somme des nombres impairs de 0 à {number2} est : {result2}"
print(sum_of_odds(100))
#15
def sum_of_even(number3):
    result3=0
    for i in range(number3+1):
            if i%2==0:
                result3+=i
    return f"la somme des nombres pairs de 0 à {number3} est : {result3}"
print(sum_of_even(100))

#exo2
#1
def even_and_odds(number4):
    evens,odds=0,0
    for i in range(number4+1):
        if i%2==0:
            evens+=1
        elif i%2==1:
            odds+=1
    return f"The number of odds are {odds} \nThe number of evens are {evens} ."
print(even_and_odds(100))
#2
def factorial(number5):
    facto=1
    if number5==0:
        return f"{number5}! = 1"
    elif number5<0:
        return "le factoriel ne prends en compte que les nombres positifs"
    for i in range(1,number5+1):
        facto*=i
    return f"{number5}! = {facto}"
print(factorial(4))
#3
def is_empty(param):
    if not param:
        return "cet objet est vide"
    return "cet objet contient une valeur"
var=[]
print(is_empty(var))
#4

# Liste de 15 entiers avec un mode évident (le 7 apparaît 4 fois)
donnees_test = [12, 7, 3, 7, 18, 5, 7, 2, 10, 7, 3, 18, 9, 5, 12]

#mean
def calculate_mean(tab5):
    somme=0
    for i in tab5:
        somme+=i
    mean=somme/len(tab5)
    mean=round(mean,2)
    return mean
#median
def calculate_median(tab6):
    tab_med=[]
    sorted_tab=sorted(tab6)
    indx_m=len(sorted_tab)//2
    if len(sorted_tab)%2==1:
        median=sorted_tab[indx_m]
        return median
    elif len(sorted_tab)%2==0:
        tab_med.extend(sorted_tab[indx_m-1:indx_m+1])
        median=calculate_mean(tab_med)
        return median

#mode 
def calculate_mode(tab7):
    compteur={}
    tab_mode=[]
    for i in tab7:
        compteur[i]=compteur.get(i,0)+1
    for eff,occurence in compteur.items():
        tab_mode.append((occurence,eff))
   
    copy=sorted(tab_mode,reverse=True)
    occurence,mode=copy[0]
    return(mode,occurence) 
#range
def calculate_range(tab8):
    _range=max(tab8)-min(tab8)
    return _range
#variance 
def calculate_variance(tab9):
    _sum=0
    N=1/len(tab9)
    moy=calculate_mean(tab9)
    for i in tab9:
        _sum+=math.pow((i-moy),2)
    variance=_sum*N
    return  variance
#ecart-type
def calculate_std(tab10):
    ecart_type=math.sqrt(calculate_variance(tab10))
    return ecart_type
mode,occurence=calculate_mode(donnees_test)
print(f"• Moyenne    : {calculate_mean(donnees_test):.2f}")
print(f"• Médiane    : {calculate_median(donnees_test)}")
print(f"• Mode       : {mode} (apparaît {occurence} fois)")
print(f"• Étendue    : {calculate_range(donnees_test)}")
print(f"• Variance   : {calculate_variance(donnees_test):.2f}")
print(f"• Écart-type : {calculate_std(donnees_test):.2f}")


#Exercice3
#1
def is_prime(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(math.sqrt(nombre)) + 1):
        if nombre % i == 0:
            return False          
    return True
print(f"{14 } est t'il premier? : {is_prime(14)}")

#2
def is_unique(tab11):
    if len(tab11)!=len(set(tab11)):
        return "il existe au moins élément dans la liste qui n'est pas unique"
    return "tout les éléments de la liste sont uniques"
print(is_unique(donnees_test))
#3
def is_same_type(tab12):
    if not tab12:
        return "tout les element on le meme type"
    first_item=tab12[0]
    for element in tab12:
        if type(element)!=type(first_item):
            return "il existe au moins un élément qui a un type différent des autres"
    return "tout les element on le meme type"
print(is_same_type(donnees_test))
#4
def is_identifier(param3):
    if not param3.isidentifier():
        return f"{param3} n'est pas est valide comme identifiant"
    return f"{param3} est une valide comme idantifiant"
variable="lol"
print(is_identifier(variable))

#5
#i
def most_spoken_languages(ditcionary,lim=20):
    compteur_langue={}
    langue_nbre=[]
    for i in ditcionary:
        for langue in i.get("languages",[]):
            compteur_langue[langue]=compteur_langue.get(langue,0)+1
    for langue,nombre in compteur_langue.items():
        langue_nbre.append((nombre,langue))
    langue_nbre.sort(reverse=True)
    
    print(f"les {lim} langues les plus parlé sont:\n")
    return langue_nbre[:lim]
for nombre,langue in most_spoken_languages(countr_data):
        print(f"{langue} : {nombre} pays \n")
#ii
def most_populated_countries(dictionary,lim=20):
    pop_pays=[]
    for i in dictionary:
        pays=i.get("name",0)
        pop=i.get("population",0)
        pop_pays.append((pop,pays))
    pop_pays.sort(reverse=True)
    print(f"les {lim} pays les plus peuplés sont:\n")
    return pop_pays[:lim]
for pop,name in most_populated_countries(countr_data,):
    print(f"{name} avec {pop} d'habitants \n")
     














