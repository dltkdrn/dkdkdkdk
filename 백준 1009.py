import sys
T=int(sys.stdin.readline())
for _ in range (T):
    a,b= map(int, sys.stdin.readline().split())
    rst= [(a**i)%10 for i in range(1,5)][(b%4)-1]
    print(rst if rst !=0 else 10)