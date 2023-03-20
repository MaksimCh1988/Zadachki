###Functions 7.3###

#7.4
def check_password (st , chars = "$%!?@#"):
    if len(st) >= 8 and set(st).intersection(set(chars)):
        return True
    else:
        return False
   
#7.5
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def my_func(st, sep='-' ):
    ls=list(st.lower())
    t[' '] = sep
    result=[]
    for i in ls:
        if i in t:
            result.append(t[i])
        else:
            result.append(i)
            
            
    return ''.join(result)

st=input()
print(my_func(st))
print(my_func(st, sep='+' ))
