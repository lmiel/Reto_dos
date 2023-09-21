n = int(input())

#queremos ver cual es el numero mas pequeño en valor absoluto
#para ello convertimos todos los numeros a valor absoluto y cogemos el minimo y lo printeamos

for numero in range(n):
    lista = []
    absoluto = abs(numero)
    lista.append(absoluto)
    print(min(lista))

#solucion del profesor
#n = int(input())
#a = map(int,input().split())
#m = abs(a[0])
#for x in range(1:):
# if abs(x) < m:
#   m = abs(x)
#print(m)

