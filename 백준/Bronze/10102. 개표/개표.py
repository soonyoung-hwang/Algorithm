N = int(input())
votes = input().rstrip()
A, B = 0, 0
for i in range(N):
    if votes[i] == 'A':
        A += 1
    else:
        B += 1

if A == B:
    print("Tie")
elif A > B:
    print("A")
else:
    print("B")