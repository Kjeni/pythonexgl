zdanie = str(input("Podaj swoje zdanie: "))
rozdziel = zdanie.split()[::-1]
list=[]
for i in rozdziel:
    list.append(i)
print(" ".join(list))