#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
pos=[i for i in numbers if i <=0]
print(pos)
#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend_list=[number for row in list_of_lists for number in row]
print(flattend_list)
#3
binair=[(i,1,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(binair)
#4
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattend_c=[[country.upper(),country[:3].upper(),cap.upper()] for sublist in countries for country,cap in sublist]
print(flattend_c)
#5
countries_1 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattend_c1=[{'country':country_1.upper(),'city':cap_1.upper()} for subc in countries_1 for country_1,cap_1 in subc ]
print(flattend_c1)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
Names=[firstname+" "+lastname for subliste in names for firstname,lastname in subliste]
print(Names)
