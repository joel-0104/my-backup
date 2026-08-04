from countrie import countries
#1
list_vide=[]
#2
five_elmnt=["item1","item2","item3","item4","item5"]
print(five_elmnt)

#3
print("la longuer de la liste est:",len(five_elmnt))

#4
print(five_elmnt[0])
print(five_elmnt[(len(five_elmnt))//2])
print(five_elmnt[len(five_elmnt)-1])

#5
mixed_data_type=["joel",19,1.89,"single","maison"]

#6
it_companies=["Facebook","Google","Microsift","Apple","IBM","Oracle","Amazon"]

#SEPT
print(it_companies)

#8
print(f"le nombre d'entreprise dans la liste est {len(it_companies)}")

#9
print(it_companies[0])
print(it_companies[(len(it_companies))//2])
print(it_companies[len(it_companies)-1])

#10
it_companies[3]="samsung"
print(it_companies)

#11
it_companies.append("Redmagic")
print(it_companies)

#12
it_companies.insert((len(it_companies))//2,"redmagic")
print(it_companies)

#13
it_companies[3]=it_companies[3].upper()
print(it_companies)

#14
sony=["sony"]
it_companies.extend(sony)
print(it_companies)

#15
print("steam" in it_companies)

#16
it_companies.sort()
print(it_companies)

#1sept
it_companies.sort(reverse=True)
print(it_companies)

#18
print(it_companies[0:3])

##19
print(it_companies[-3:])

#20
index_milieux=len(it_companies)//2 -1
elmt_milieux=it_companies[index_milieux]
print(elmt_milieux)

#21,22,23
del it_companies[0]
del it_companies[index_milieux]
del it_companies[len(it_companies)-1]
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end ,"\n", back_end)
full_stack=front_end + back_end
print(full_stack)

#2sept
indice_redux=full_stack.index("Redux")
full_stack.insert(indice_redux+1,"Python")
full_stack.insert(indice_redux+2,"SQL")
print(full_stack)
#EXERCICE2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(max(ages))
ages.append(min(ages))
ages.sort()
id_mil=len(ages)//2
age_med1=ages[id_mil]//2
age_med2=ages[id_mil+1]//2
print(age_med1,age_med2)
age_moyen=sum(ages)/len(ages)
print(age_moyen)
print(f"l'etendu est{max(ages)-min(ages)}")
print(abs(min(ages)-age_moyen)<=abs(max(ages)-age_moyen))

#2
print("le pays du milieux est:",countries[len(countries)//2])

#3
countries_a=countries[0:(len(countries)//2)+1]
countries_b=countries[(len(countries)//2)+1:]
print(f"countries_a:{countries_a}")
print(f"countries_b:{countries_b}")

#4
chine,russie,usa,*pays_scandinaves=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(chine)
print(russie)
print(usa)
print(pays_scandinaves)


