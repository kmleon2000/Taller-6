mayor = int(input("Ingrese el primer numero: "))
middle = int(input("Ingrese el segundo numero: "))
minor = int(input("Intrese el tercer numero: "))
aux = None
print('\033c')

# organizar números
# mayor>middle>minor

if(mayor > minor and minor > middle):
    # mayor>minor>middle
    aux = minor
    minor = middle
    middle = aux
    aux = None
elif(middle > mayor and mayor > minor):
    # middle>mayor>minor
    aux = mayor
    mayor = middle
    middle = aux
    aux = None
elif(middle > minor and minor > mayor):
    # middle>minor>mayor
    aux = middle
    middle = mayor
    mayor = aux
    aux  = None

    aux = minor
    minor = middle
    middle = minor
    aux = None
elif(minor > mayor and mayor > middle):
    # minor>mayor>middle
    aux = minor
    minor = middle
    middle = aux
    aux =  None

    aux = middle
    middle = minor
    minor = aux
    aux = None
elif(minor > middle and middle > mayor):
    # minor>middle>mayor
    aux = mayor
    mayor = minor
    minor = aux
    aux = None

print("El numero mayor es:",mayor)
print("El numero de en medio es:", middle)
print("El numero menor es:", minor)


if(mayor%2 == 0):
    print(mayor);

if(minor%5 == 0 and minor < 30):
    print(minor)

if(minor > 4 or minor < 10):
    print(minor)