oppgave = input("Oppgi '1' for gange, '2' for dele: ")
x1 = int(input("Første tall: "))
x2 = int(input("Andre tall: "))


def multiplication(n1, n2):
    return n1*n2


def division(n1, n2):
    return n1/n2


if oppgave == 1:
    result = multiplication(x1, x2)
    print("løsningen på gangestykket ", x1, " * ", x2, " er: ", result)
else:
    result = division(x1, x2)
    print("løsningen på delestykket ", x1, " / ", x2, " er: ", result)




# noe fra en fil
# with open("data.txt") as file_name:
#    for line in file_name:
#        bw.append(line.split()[0])
# print(bw)
