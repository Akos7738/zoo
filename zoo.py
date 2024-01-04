def addAnimal(myName):
    animal = dict()
    found = False
    for a in zoo:
        if myName in a.keys():
            a[myName] += 1
            found = True
    if not found:
        animal[myName] = 1
        zoo.append(animal)

print("Ez egy állatkert.")
print("Állat hozzáadása(1) - Állat törlése(2) - Kilépés(0)")

select = None
zoo = []
animal =dict()

while select != "0":
    select = input("Mit szeretne tenni? ")
    if select != "0":
        if select == "1":
            name = input("Az állat neve: ")
            addAnimal(name)
        elif select == "2":
            removeName = input("Törlendő állat neve: ")
            for a in zoo:
                if name in a.keys():
                    if a[name] > 0:
                        a[name] -= 1
                    else:
                        del a[name]

print(f"Második: {zoo}")