sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}



print(sample_dict)

#for k in sample_dict.keys():
# print(f'{k:<10} = {sample_dict[k]:>10)}')


#for k,v  in  sample_dict.items():
# print(f'{k:<10} = {v:>10}')

lista=["name","age", "sds"]
#K={}

#for j in lista:
 #if j in sample_dict:
 # K[j] = sample_dict[j]

K={j: sample_dict[j] for j in lista if j in sample_dict}
print("K= ",K)

#for k in lista:
# if k in sample_dict:
#  sample_dict.pop(k)

#or k in lista:
 #print(sample_dict.pop(k, "Brak klucza i pary"))
 #print()

#if "Johnes"in sample_dict.values():
# print("Jones występuje")
#else:
 #print("Nie występuje")


#print(sample_dict)
sample_dict['location']=sample_dict.pop('city')

print(sample_dict)
