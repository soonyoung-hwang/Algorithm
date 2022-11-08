N = int(input())

prime = [[2,3,5,7]]

def is_prime(num):
    ans = True
    for i in range(2,int(num**0.5)+1):
        if(num%i == 0):
            ans = False
            break
    
    return ans

for i in range(N-1):
    temp = []
    for p in prime[i]:        
        for j in range(1,10):
            t = p*(10)+j
            if(is_prime(t)):
                temp.append(t)
    
    prime.append(temp)
            
for i in range(len(prime[-1])):
    print(prime[-1][i])
    