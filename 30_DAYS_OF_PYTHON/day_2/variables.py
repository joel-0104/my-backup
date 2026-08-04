# Day 2: 30 Days of python programming
prenom = "satoru"
nom_famille = "gojo"
nom_complet = "satoru gojo"
pays = "japan"
city = "tokyo"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False
nom, classe = "joel", "L2"

# EXERCICE 2
print(type(prenom))
print(type(nom_famille))
print(type(nom_complet))
print(type(pays))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(nom))
print(type(classe))

# 2. Longueur du prénom
print(len(prenom))

# 3. Comparaison (Parfait !)
print(len(prenom) > len(nom_famille))

# 4 & 5. Addition
num_one, num_two = 5, 4
total = num_one + num_two
print(total)

# 6. Soustraction
print(num_one - num_two)

# 7. Multiplication
product = num_one * num_two
print(product)

# 8. Division
division = num_one / num_two
print(division)

# 9. Modulo
remainder = num_two % num_one
print(remainder)

# 10. Puissance
exp = num_one ** num_two
print(exp)

# 11. Division entière
floor_division = num_one // num_two
print(floor_division)

# 12. Cercle (Rayon = 30)
area_of_circle = 3.14 * (30 ** 2)
print('area =', area_of_circle)

circum_of_circle = 2 * 3.14 * 30
print("circum =", circum_of_circle)

# 12. Part ii (Cercle avec input)
rayon = int(input("Entrez le rayon : "))
aire = 3.14 * (rayon ** 2)
print("Nouvelle aire =", aire)

# 13. Inputs utilisateur
NOM = input("Entrez votre nom : ")
country = input("Entrez votre pays : ")
AGE = int(input("Entrez votre âge : "))

# 14. Mots-clés
help('keywords')