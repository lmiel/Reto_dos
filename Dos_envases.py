t = int(input())

for i in range(t):
    a,b,c = input().split()
    a,b,c = int(a),int(b),int(c)
    #tambien se podria poner como a,b,c = map(int,input().split())
    d = abs(a-b)
    print(d//(2*c))
    
