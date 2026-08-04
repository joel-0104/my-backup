#1
thirty="Thirty "
days="Days "
of="Of "
python="Python"
phrase=thirty+days+of+python
print(phrase)

#2
coding="Coding"
_for="For"
tous="All"
phrase2=coding+_for+tous
print(phrase2)

#3 et 4 et 5
company="Coding For All"
print(company)
print(len(company))

#6 ET SEPT
print(company.upper())
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[0:5].split())

#10
print(company.find("Coding"))

#11
print(company.replace("Coding","Python"))

#12
phrase3="Python for Everyone"
print(phrase3)
print(phrase3.replace("for Everyone","for All"))

#13
print(company.split())

#14
phrase4="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(phrase4.split(","))

#15
print(f"l'element a l'indice 0 est {company[0]}")

#16
print(f"l'indice du  dernier element de {company} est :{len(company)-1}")

#1sept
print(f"l'element a l'indice 10 est: {company[10]}")

#18
phrase_1 = 'Python For Everyone'

# 1. On découpe la phrase à chaque espace pour obtenir une liste de mots
mots = phrase_1.split()  # Donne : ['Python', 'For', 'Everyone']

# 2. On récupère le premier caractère de chaque mot (index 0)
acronyme = mots[0][0] + mots[1][0] + mots[2][0]

print(acronyme)  # Affiche : PFE

#19
word=company.split()
acro=word[0][0]+word[1][0]+word[2][0]
print(acro)

#20
print(company.index("C"))

#21
print(company.index("F"))

#22
print("Coding For All people".rfind("l"))

#23
phrase5='You cannot end a sentence with because because because is a conjunction'
print(phrase5.find("because"))

#24
print(phrase5.rindex("because"))

#25
phrase6='You cannot end a sentence with because because because is a conjunction'
debut=phrase6.find("because")
expr="because because because"
fin=debut+len(expr)
result=phrase6[debut:fin]
print(result)

#26
print(phrase6.find("because"))

#2sept
print(f"est ce que{company} comence par \"coding\"?:{company.startswith('Coding')}")

#28
print(f"est ce que{company} comence par \"coding\"?:{company.endswith('Coding')}")

#29
phrase_sept='&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
print(phrase_sept.strip("&nbsp "))

#30
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python")

#31
liste=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(liste))

#32
print("I am enjoying this challenge.\n I just wonder what is next.")

#33
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#34
radius=10
area=3.14*radius**2
print(f"The are of circle with radius {radius} is {area} meters square.")

#35
a=8
b=6
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")
print(f"{a}//{b}={a//b}")
print(f"{a}**{b}={a**b}")