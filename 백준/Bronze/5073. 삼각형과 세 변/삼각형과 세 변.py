while(True):
    a = list(map(int,input().split()))

    a.sort(reverse=True)
    if a[0]==a[1]==a[2]==0:
        break
    
    if a[0] >= a[1]+a[2]:
        print("Invalid")
    else:
        if a[0]==a[1]==a[2]:
            print("Equilateral")
        elif a [0]==a[1] or a[1]==a[2]:
            print("Isosceles")
        else: print ("Scalene")
    
