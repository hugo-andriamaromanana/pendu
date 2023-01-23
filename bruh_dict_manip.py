testdic={
    "hugo":34,
    "Martin":464,
    "Jose":23,
    "Pablo":34,
    "Luis":23,
    "Juan":34,
    "Pedro":23,
    "Raul":34,
}

def get_4_best(dic):
    arr=[]
    for i in dic:
        arr.append(f'{i} : {dic[i]}')
    return arr[:3]

print ('; '.join(get_4_best(testdic)))