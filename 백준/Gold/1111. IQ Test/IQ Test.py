# 답 여러개 -> A
# 답 불가능 -> B
N = int(input())
numbers = list(map(int,input().split()))

candidates=[]

if N == 1:
    print("A")

elif N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[0])
    else:
        print("A")

else:
    # 반복 수
    # 혹은 a,b는 하나로 정해진다.
    # case 1) 반복수
    if numbers[0] == numbers[1]:
        if numbers[0] == numbers[2]:
            for i in range(3,N):
                if numbers[i] != numbers[0]:
                    print("B")
                    break
            else:
                print(numbers[0])
        else:
            print("B")
    else: # case 2) a,b 정해짐
        a = (numbers[2]-numbers[1])/(numbers[1]-numbers[0])
        b = numbers[1] - (numbers[0]*a)
        if (a != int(a)) or (b != int(b)):
            print("B")
        else:
            for i in range(3,N):
                if numbers[i] != numbers[i-1]*a+b:
                    print("B")
                    break
            else:
                print(int(numbers[N-1]*a+b))