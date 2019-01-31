#Mayor de dos números
def max(num1, num2):
    if num1 > num2:
        return num1
    return num2

#Tamaño de cadena
def length(chain):
    cont = 0
    for i in chain:
        cont = cont + 1
    return cont

#Is this a vowel?
def vowel(key):
    if key == "a" or key == "e" or key == "i" or key == "o" or key == "u": return True
    return False

#Sum of a list
def sum(list):
    whole = 0
    for i in range(len(list)):
        whole = whole + list[i]
    return whole

#Multiplication of a list
def mul(list):
    whole = 1
    for i in range(len(list)):
        whole *= list[i]
    return whole

#Inversa
def truncateAfter(chain, len1, cont):
    if length(len1) == length(chain): 
        return len1
    else:
        cont += 1
        len1 += chain[length(chain) - cont]
        return truncateAfter(chain, len1, cont)

def truncateBefore(chain):
    return truncateAfter(chain, "", 0)

#Function
def _palindromo(chain):
    if chain == truncateBefore(chain): return True
    return False

#Multiplicacion
def nCaracteres(num, character):
    chain = ""
    for i in range(num):
        chain += character
    return chain

def draw(num):
    whole = ""
    for i in range(num):
        whole += "*"
    return whole

def asterics(list):
    for i in range(len(list)):
        print(draw(list[i]))

def mayuscula(chain):
    return len([c for c in chain if c.isupper()])

print ("Mayor {maxNumber}".format(maxNumber = max(41,5)))
print ("Lenght {maxNumber}".format(maxNumber = length("Colombia")))
print ("Is a vowel? {maxNumber}".format(maxNumber = vowel("o")))
print ("Sum {maxNumber}".format(maxNumber = sum([1,2,3,4])))
print ("Mul {maxNumber}".format(maxNumber = mul([1,2,3,4])))
print ("Inverse {maxNumber}".format(maxNumber = truncateBefore("Colombia")))
print ("Palindromo {maxNumber}".format(maxNumber = _palindromo("oso")))
print ("Character {maxNumber}".format(maxNumber = nCaracteres(5, "o")))
print ("Asterics {maxNumber}".format(maxNumber = asterics([4,9,7])))
print ("Upper {maxNumber}".format(maxNumber = mayuscula("ColombiA")))