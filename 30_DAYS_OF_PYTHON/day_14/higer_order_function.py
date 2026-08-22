from functools import reduce
from listedepays import pays
from countries_data import*

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#3,4,5
def affichage(liste):
    for i in liste:
        print(i)
    print()    
affichage(names)
affichage(countries)
affichage(numbers)
#EXO2
#1
upper_countries=list(map(lambda x: x.upper(),countries))
print(upper_countries)
print()
#2
squared_nums=list(map(lambda x:x**2,numbers))
print(squared_nums)
print()
#3
upper_names=list(map(lambda x: x.upper(),names))
print(upper_names)
print()
#4
land_countries=list(filter(lambda x: x.endswith('land'),countries))
print(land_countries)
print()
#5
six_car_countries=list(filter(lambda x: len(x)==6,countries))
print(six_car_countries)
print()
#6
more_than_six_c=list(filter(lambda x: len(x)>=6,countries))
print(more_than_six_c)
print()
#7
start_with_E=list(filter(lambda x:x.startswith("E"),countries))
print(start_with_E)
print()
#8
end_with_LAND=reduce( lambda acc,val:f"{acc} {val}",list(filter(lambda x: x.endswith('LAND'),list(map(lambda x: x.upper(),countries)))))
print(end_with_LAND)
print()
#9
def get_strings_list(liste):
    return [i for i in liste if type(i)==str]
tab_mix=[1,'lol',{"age":16,"married":False},'i miss school']
print(get_strings_list(tab_mix))
print()
#10
addition=reduce(lambda acc,val:acc+val,numbers)
print(addition)
print()
#11
concartenate=reduce(lambda acc,val:f"{acc} , {val} ",countries[:-1])
last=countries[-1]
final=f"{concartenate} et {last} sont des pays d'Europe du Nord"
print(final)
print()
#12
def categorize_countries(liste,):
    return list(filter(lambda i: i if 'ia' in i else None,liste))
print(categorize_countries(pays))
print()
#13
def dic_maker(liste):
    return reduce(lambda acc,val:{**acc,val[0]:acc.get(val[0],0)+1},liste,{})
print(dic_maker(pays))
print()
#14 
def get_first_ten_countries(liste):
    return liste[:10]
print(get_first_ten_countries(pays))
print()
#15
def get_last_ten_countries(liste):
    return liste[-10:]
print(get_last_ten_countries(pays))
print()

#exo3
sort_countries_by_name=sorted(info_pays,key=lambda pays:pays.get("name"))
print(sort_countries_by_name)
print()
sort_countries_by_cap=sorted(info_pays,key=lambda cap:cap.get("capital"))
print(sort_countries_by_cap)
print()
sort_countries_by_pop=sorted(info_pays,key=lambda pop:pop.get("population",0))
print(sort_countries_by_pop)
print()
#top10 languages
languages_list=list(map(lambda x: x.get("languages",[]),info_pays))
all_languages=reduce(lambda acc,langs:acc+langs,languages_list,[])
uniques_language=set(all_languages)
language_pop_1=list(map(lambda lang:(all_languages.count(lang),lang),uniques_language))
top_ten_languages=sorted(language_pop_1,reverse=True)[:10]
print(top_ten_languages)
#
most_habitated_count=list(map(lambda x:(x.get("population",0),x.get("name",None)),info_pays))
top_ten_habitated=sorted(most_habitated_count,reverse=True)[:10]
final_top_ten_h=[(name,pop) for pop,name in top_ten_habitated]
print(f"les dix pays les plus peuplés sont: \n {final_top_ten_h}")



    

    



