t = int(input())

def diferencia(a,b,c):
    for i in range(t):
        a,b,c = input().split()
        a,b,c = int(a),int(b),int(c)
        #tambien se podria poner como a,b,c = map(int,input().split())
        d = abs(a-b)
        resultado = (d/(2*c)) #hay que redondear hacia arriba
    
    return resultado

print(diferencia(17,4,3))
    
