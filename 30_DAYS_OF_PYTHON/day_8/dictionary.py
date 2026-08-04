#1
dog={}
#2
dog["name"]="max"
dog["color"]="black"
dog["breed"]="shiba"
dog["legs"]=4
dog["age"]=15
print(dog)
#3
student={
    "first_name":"gojo",
    "last_name":"satoru",
    "gender":"male",
    "age":34,
    "marital_status":"single",
    "skills":['infinity','blue','red','hollow purple'],
    "country":"japan",
    "city":"tokyo",
    "address":"unknown"
}
#4
print(len(student))

#5
print(student["skills"])
print(type(student["skills"]))

#6
student["skills"].append("kung-fu")
student["skills"].append("aura farm")
print(student["skills"])

#SEPT
keys=list(student.keys())
print(f"les clé sont:{keys}")
#8
values=list(student.values())
print(f"les valeur contenues dans le dictionnaire sont:{values}")

#9
student_list=list(student.items())
print(student_list)

#10
student.pop("address")
print(student)
del dog