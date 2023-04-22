# Pedimos las palabras al usuario
string1= input("Ingresa la primera palabra: ")
string2= input("Ingresa la segunda palabra: ")

# Si la longitud de las palabras es diferente imprimir error
if len(string1) != len(string2):
    print ("error")
    exit()

#Si la longitud de las palabras coincide, se intercalan según el rango establecido
else: 
    intercal = []
    for i in range(0, 4):
        intercal.append ( string1[i])
        intercal.append ( string2[i])

    print(intercal)

