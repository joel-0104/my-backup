# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#EXERCICE 1

#1
print(len(it_companies))
#2
it_companies.add("Twitter")
print(it_companies)
#3
it_companies.update(["Sony","Steam"])
print(it_companies)
#4
it_companies.discard("Google")
print(it_companies)
#5 la difference entre remove et discard c'est que discard ne renvoie pas d'erreur quand l'objet a supprimer n'existe pas contrairement a remove

#EXO2
print('exo2')
#1
print(A.union(B))
#2
print(A.intersection(B))
#3
print(f"A est t'il un sous-ensemble de B:{A.issubset(B)}")
#4
print(f"A ET B sont-ils disjoints:{A.isdisjoint(B)}")
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#SEPT
del A
del B

#EXO3
print("\n")
print('EXO3')
#1
age_set=set(age)
print(age_set)
print(f"la liste est-elle plus grande que l'ensemble:{len(age)>len(age_set)}")

#2

"""
EXERCICE 3 - Question 2 : Explication des types de données

1. str (String) : Séquence de texte, ordonnée, immutable, autorise les doublons.
2. list : Collection d'éléments ordonnée, MUTABLE (modifiable), autorise les doublons.
3. tuple : Collection d'éléments ordonnée, IMMUTABLE (non modifiable), autorise les doublons.
4. set : Collection d'éléments NON ordonnée, mutable, SANS DOUBLONS (valeurs uniques uniquement).
"""

#3
phrase="I am a teacher and I love to inspire and teach people"
print(phrase)
_list=phrase.split(" ")
list_set=set(_list)
print(f"le nombre de mots unique dans la phrase est:{len(list_set)}")
print(list_set)