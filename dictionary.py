dict1={2:"orange",3 :"banana",1 :"apple"}
print(f"Dictionary 1: {dict1}")
l=list(dict1.items())
l.sort()
print('Asending order is :',1)
l=list(dict1.items())
l.sort(reverse=True)
print('Desending order is :',1)

dict2={4 :"plum",5 :"cherry"}
print(f"Dictionary 1: {dict2}")
dict1.update (dict2)
print(f"Dictionary after merging:{dict1}")
