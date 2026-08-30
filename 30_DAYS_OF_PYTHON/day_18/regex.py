import re 
#1
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
dot_less=re.sub(r"\.","",paragraph)
list_par=re.split(" ",dot_less)
def count(l):
    dic={}
    for i in l:
        dic[i]=dic.get(i,0)+1
    return dic.items()
print(count(list_par))
#2
txt="La position de certaines particules sur l'axe horizontal x sont -12, -4, -3 et -1 dans la direction négative, 0 à l'origine, 4 et 8 dans la direction positive."
matches=re.findall(r"-?\d+",txt)
num=[int(x) for x in matches]
mini=min(num)
maxi=max(num)
print(f"la distance est : {maxi-mini}")
#exo2
#1
def is_valid_variable(word):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(regex_pattern,word):
        return True
    return False
mot=input("Entrez un nom de variable: ")
print(is_valid_variable(mot))
#exo3
sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"
def clean_sentence(word):
    reg_pattern=r"[^\w\s]"
    cleaned=re.sub(reg_pattern,"",word)
    return cleaned
cleaned_text=clean_sentence(sentence)
print(cleaned_text)
sent_list=re.split(" ",cleaned_text)
def most_frequent_word(liste):
    dic={}
    top=[]
    for i in liste:
        dic[i]=dic.get(i,0)+1
    sorted_top=sorted([(number,word) for word,number in dic.items()],reverse=True)
    return sorted_top[:3]
print(most_frequent_word(sent_list))









