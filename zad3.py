zdanie = str(input("Podaj swoje zdanie: "))
rozdziel = zdanie.split()
list=[]
for i in rozdziel:
    list.append(i)
print(len(list))