n=int(input("Ingrese un número: "))
factorial=1

for i in range(1,n+1):
    factorial=factorial *i
print(factorial)
if n<0:
    print("error") 
    


