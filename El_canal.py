
t = int(input())
l = input().split()
n = l[0]  #numero de subs
a = l[1]  #numero de subs online 
q = l[2]  #numero de notificaciones

notifs = input()


for i in notifs:
    if i == "+":
        a += 1
    else:
        a -= 1
        
    if a == n:
        print("YES")
        break
    