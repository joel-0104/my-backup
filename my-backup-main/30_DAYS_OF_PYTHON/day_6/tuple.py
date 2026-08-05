#1
tpl1=tuple()

#2
tpl2=("hanako","shikeo","takeru")
print(tpl2)
tpl3=("nezuko","daki")
print(tpl3)

#3
siblings=tpl2+tpl3
print(siblings)
#4
print(f"le nombres de freres et soeur est{len(siblings)}")

#5
siblings=list(siblings)
siblings.append("minato")
siblings.append("kushina")
family_members=tuple(siblings)
print(f"family members={family_members}")

#EXO2
#1
parents=family_members[-2:]
sib=family_members[:-2]
print(f"parents:{parents}")
print(f"siblings:{sib}")

#2
fruits=("mango","apple","pineapple")
legume=("letus","carote")
prod_animaux=("poisson","poulet")
print(fruits)
print(legume)
print(prod_animaux)
food_stuff=fruits+legume+prod_animaux
print(food_stuff)

#3
food_stuff_lt=list(food_stuff)
print(food_stuff_lt)

#4
ind_mil=len(food_stuff_lt)//2
print(food_stuff_lt[ind_mil])

#5
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

#6
del food_stuff

#SEPT
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"estonia in nordic?{'estonia' in nordic_countries}")
print(f"iceland in nordic?{'Iceland' in nordic_countries}")