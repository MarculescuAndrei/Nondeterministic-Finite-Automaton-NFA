f = open("Source.txt", 'r')
poz = f.readline()
poz = poz[:-1]

Final = f.readline().split()
L = f.readline().split()
Adjacency = {}

while L:
    if L[0] not in Adjacency.keys():
        Adjacency[L[0]] = [(L[1], L[2])]

    else:
        Adjacency[L[0]].append((L[1], L[2]))
    L = f.readline().split()

print(Adjacency)
Word = input("The word is: ")

StateSet = []
StateSetChange = []
StateSet.append(poz)

if Word == '':
    if poz in Final:
        print("The word is valid")
    else:
        print("The word is invalid")
else:
    for i in Word:
        for State in StateSet:
            if State in Adjacency:
                for Arc in Adjacency[State]:
                    if i == Arc[1]:
                        StateSetChange.append(Arc[0])
        StateSet = StateSetChange
        StateSetChange = []

Found = False
for State in Final:
    if State in StateSet:
        print("The word is valid")
        Found = True
        break
if Found == False:
    print("The word is invalid")
