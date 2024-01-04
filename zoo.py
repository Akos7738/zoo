print("Ez egy állatkert.")
print("Állat hozzáadása(1) - Állat törlése(2) - Kilépés(0)")

select = None
zoo = []

while select != "0":
    select = input("Mit szeretne tenni? ")
    if select != "0":
        if select == "1":
            name = input("Az állat neve: ")
            if name not in animal.keys():
                animal[name] = 1
                zoo.append(animal)
            else:
                for a in zoo:
                    a[name] += 1
            animal = dict()
            
for a in zoo:
    print(a)