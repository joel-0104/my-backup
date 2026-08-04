from countrie_s import countries
from countries_data import countr_data
#exo1
#1
for i in range(11):
    print(i)
print()
i=0
while i <11:
    print(i)
    i+=1
print()
#2
for i in range(10,-1,-1):
    print(i)
print()
i=10
while i>=0 :
    print(i)
    i-=1
print()

#3
for i in range(1,8):
        print("#"*i)
print()
#4
for i in range(1,9):
    for j in range(1,9):
        print("#",end=" ")
    print()
#5
print()
for i in range(11):
    print(f"{i} x {i} = {i*i}")      
#6
_list=['Python', 'Numpy','Pandas','Django', 'Flask']
print(_list)
for elmt in _list :
    print(elmt)
#7
for i in range(0,101):
    if i%2==0:
        print(i)
#8
for i in range(0,101):
    if i%2==1:
        print(i)
#exo 2
print()
#1
sum=0
for i in range(0,101):
    sum=sum+i
print(f"la somme des nombres de 0 a 100 est : {sum}")
print()
#2
sum_p=0
sum_i=0
for i in range(0,101):
    if i%2==0:
        sum_p=sum_p+i
    if i%2==1:
        sum_i=sum_i+i
   
print(f"The sum of all evens is {sum_p}. And the sum of all odds is {sum_i}.")
print()


#exo3
#1
for i in countries :
    if "land" in i:
        print(i)
print()
#2
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
indx=len(fruits)-1
fruits_inv=[]
for i in range(indx,-1,-1):
    fruits_inv.append(fruits[i])
print(fruits_inv)
print()
#3



#ii
print()
compteur_langues={}
langues_nombres=[]

for i in countr_data:
    for langue in i.get("languages",[]):
        compteur_langues[langue]=compteur_langues.get(langue,0) +1

#i Après avoir rempli compteur_langues :
print(f"Le nombre total de langues uniques est : {len(compteur_langues)}") 

for langue,nombre in compteur_langues.items():
    langues_nombres.append((nombre,langue))

#trie

langues_nombres.sort(reverse=True)

top_10_langues=langues_nombres[:10]

for nombre,langue in top_10_langues:
    print(f"le nombre de pays qui parlent {langue} est : {nombre}\n")
print()
#iii

compteur_pays={}
pays_habitants=[]
for i in countr_data:
    compteur_pays[i.get("name")]=i.get("population",0)

for name,pop in compteur_pays.items():
    pays_habitants.append((pop,name))
pays_habitants.sort(reverse=True)
top_10_pays=pays_habitants[:10]

print(f"les 10 pays les plus peuplé sont:\n")

for pop,name in top_10_pays:
    print(f"{name} avec {pop} d'habitants \n")




    

