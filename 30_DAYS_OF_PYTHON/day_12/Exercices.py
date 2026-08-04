from random import randint,random
import string
#EXO1
#1

def random_user_id():
    caractere=string.ascii_letters+string.digits
    user_id=""
    for i in range(6):
        indx_rand=int(random()*len(caractere))
        user_id+=caractere[indx_rand]
    return user_id
print(random_user_id())
print()
#2

def user_id_gen_by_user():
    caractere=string.ascii_letters+string.digits
    user_id=""
    users_id=[]
    nb_u=int(input("entrez le nombre d'utilisateurS que vous voulez generer: "))
    nb_car=int(input("entrez le nombre de caracteres de vos/votre utilisateur(s)"))
    for i in range(nb_u):
        for j in range(nb_car):
            indx_rand=int(random()*len(caractere))
            user_id+=caractere[indx_rand]
        users_id.append(user_id)
        user_id=""
    return '\n'.join(users_id)
print(user_id_gen_by_user())
print()
#3
def rgb_color_gen():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return f"rgb({r},{g},{b})"
print()

#EXO2
#1
def list_of_hexa():
    carac="abcdef"+string.digits
    color_code="#"
    liste_hex=[]
    for i in range(randint(1,30)):
        for j in range(6):
            indx_color=int(random()*len(carac))
            color_code+=carac[indx_color]
        liste_hex.append(color_code)
        color_code="#"
    return liste_hex
print(list_of_hexa())
print()

#2
def list_of_rgb_colors():
    tab_colors=[]
    for i in range(randint(1,25)):
        tab_colors.append(rgb_color_gen())
    return tab_colors
print(list_of_rgb_colors())

#3
def generate_colors(colors_type,number=None):
    if number is None:
        number = randint(1, 30)
    carac="abcdef"+string.digits
    color_code="#"
    tab_hexa=[]
    tab_rgb=[]
    if colors_type.lower()=="hexa":
        if number==1:
            for i in range(6):
                    indx_color=int(random()*len(carac))
                    color_code+=carac[indx_color]
            return color_code
        elif 1<number:
            for i in range(number):
                for j in range(6):
                    indx_color=int(random()*len(carac))
                    color_code+=carac[indx_color]
                tab_hexa.append(color_code)
                color_code="#"
            return tab_hexa
    elif colors_type.lower()=="rgb":
        res=rgb_color_gen()
        if number==1:
            return res
        elif 1<number:
            for i in range(number):
                tab_rgb.append(rgb_color_gen())
            return tab_rgb
print(generate_colors("rgb"))

#EXO3
#1
_list=list(range(10))
def shuffle_list(liste):
    copy_l=liste.copy()
    rand_l=[]
    while len(copy_l)>0:
        indx_element=randint(0,len(copy_l)-1)
        element_c=copy_l.pop(indx_element)
        rand_l.append(element_c)
    return rand_l
print(shuffle_list(_list))
print()
#2
def rand_tab():
    numbers = list(range(10))
    tab_seven = []
    for _ in range(7):
        indx = randint(0, len(numbers) - 1)
        tab_seven.append(numbers.pop(indx))
    return tab_seven









