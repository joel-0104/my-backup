from datetime import*
now=datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp)
print()
#2
now_one=now.strftime("%m/%d/%Y,%H:%M:%S")
print(now_one)
print()
#3
today="5 december 2019"
today_objet=datetime.strptime(today,"%d %B %Y")
print(today_objet)
print()
#4
courent_date=date(year=2026,month=8,day=8)
next_year=date(year=2027,month=1,day=1)
diff_one=next_year-courent_date
print(diff_one)
#5
previous_date=date(year=1970,month=1,day=1)
now_date=date(year=2026,month=8,day=8)
diff_two=now_date-previous_date
print(diff_two)

