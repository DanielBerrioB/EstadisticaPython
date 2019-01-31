import math

#This function allow to return the factorial of a number
def factorial(keyValue):
    return math.factorial(keyValue)

def permutation(size, sizePermutation):
    return factorial(size) / factorial(size - sizePermutation)

def combination(size, sizePermutation):
    return factorial(size) / (factorial(sizePermutation) * factorial(size - sizePermutation))

#This function represents a binomial distribution
def formulaNormal(size, sizePermutation, porcentaje):
    return combination(size, sizePermutation) * porcentaje**sizePermutation * (1-porcentaje)**(size-sizePermutation)

def onlyProff(size, tamano, porcentaje):
    sum = 0.0
    for i in range(tamano):
        sum += formulaNormal(size, i, porcentaje)
    return sum

def distribucionHipergeometrica(tamanoN , r, tamanoM, size):
    return combination(r,size) * combination(tamanoN-r, tamanoM - size) /  combination(tamanoN, tamanoM)

answer = True
while answer == True:

    option = input("Deseas realizar:\n1- Permutación\n2- Combinación\n3- Distribución binomial\n4- Distribución binomial acumulada\n5- DistribucionHipergeometrica -- ")
    if option == "1":
        size = input("\nEntry the size ")
        sizePermutation = input("Entry the size of the permutation ")
        print ("Répondre {res}".format(res = permutation(int(size), int(sizePermutation))))
    else:
        if option == "2":
            size2 = input("\nEntry the size ")
            sizePermutation2 = input("Entry the size of the combination ")
            print ("Répondre {res}".format(res = combination(int(size), int(sizePermutation))))
        else: 
            if option == "3":
                size3 = input("\nIngrese el tamaño de la muestra ")
                sizePermutaion3 = input("Ingrese el valor al que desea encontrar la probabilidad ")
                porcentaje = input("Ingrese la probabilidad de ingreso (pi) ")
                print ("Répondre {res}".format(res = formulaNormal(int(size3), int(sizePermutaion3), float(porcentaje))))
            else: 
                if option == "4":
                    size4 = input("\nIngrese el tamaño de la muestra ")
                    sizePermutaion4 = input("Ingrese el numero limite (ejemplo < o igual a 5) ")
                    porcentaje = input("Ingrese la probabilidad de ingreso (pi) ")
                    print ("Secundario {res}".format(res = onlyProff(int(size4), int(sizePermutaion4), float(porcentaje))))
                else: 
                    if option == "5":
                        size5 = input("\nEntry N ")
                        sizePermutaion5 = input("Entry m ")
                        porcentaje = input("Entre r ")
                        porcentajeMuestra = input("Entre x ")
                        print ("Répondre {res}".format(res = distribucionHipergeometrica(int(size5), int(porcentaje), int(sizePermutaion5), int(porcentajeMuestra))))


    key = input("Deseas seguir operando\n")
    if key == "si": answer = False