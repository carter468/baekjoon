# nums = [int(input()) for _ in range(9)]
# max=nums[0]
# idx=0
# for i in range(9):
#     if max<=nums[i]:
#         max=nums[i]
#         idx=i
# print(max)
# print(idx+1)

# n=int(input())
# nums = [int(x) for x in input().split()]

# max=0
# for i in nums:
#     if max<i:
#         max=i

# sum=0
# for i in nums:
#     sum+=(i/max*100)

# print(sum/n)

# n = int(input())
# ox = [input() for _ in range(n)]
# print(ox)
# for x in ox:
#     cnt=0
#     pt=0
#     for y in x:
#         if y=='O':
#             cnt+=1
#             pt+=cnt
#         else:
#             cnt=0
#     print(pt)

# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]

# for a in range(n):
#     sum = 0
#     for i in range(data[a][0]):
#         sum+=data[a][i+1]
#     ave = sum/data[a][0]
#     cnt = 0
#     for i in range(data[a][0]):
#         if data[a][i+1]>ave:
#             cnt+=1
#     print("{:.3f}%".format(cnt/data[a][0]*100))

# def d(num):
#     num1=num
#     len=0
#     while num1:
#         num1//=10
#         len+=1

#     ans=num
#     for i in range(len):
#         ans+=int(str(num)[i])
    
#     return ans

# for i in range(1,10001):
#     sn = False
#     for n in range(1,i):     
#         if d(n) == i:
#             sn = True
#             break
#     if sn == False:
#         print(i)    
    
# word = input()
# word = word.upper()

# cnt=[]
# len = len(word)
# for i in range(65,91):
#     cnt.append(word.count(chr(i)))

# max = 0
# for i in range(26):
#     if max==cnt[i]:
#         idx="?"
#     if max<cnt[i]:
#         max=cnt[i]
#         idx=chr(i+65)
# print(idx)
    
# a = input()
# a = a.strip()
# a = a.split()
# print(len(a))

# a = input()
# ca = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# cnt = 0

# while a!="":
#     cut = False
#     for x in ca:
#         if a.find(x) == 0:
#             a = a.replace(x,"",1)
#             cut = True
#             cnt += 1
#             break
#     if cut == False:
#         a = a[1:]
#         cnt += 1
# print(cnt)

# import math

# a,b,c = map(int,input().split())
# if b>=c:
#     d=-1
# else:
#     d = math.floor(a/(c-b))+1

# print(d)

# bd+a<cd
# a<cd-bd
# a/(c-b)<d

# a = int(input())
# sum = 1
# cnt = 1
# while 1:
#     if sum>=a:
#         break
#     sum += 6*cnt
#     cnt += 1

# print(cnt)

# a,b,v = map(int,input().split())

# d = (v-a)//(a-b)-1
# h = (a-b) * d

# while 1:
#     d += 1
#     h += a
#     if h >= v:
#         break
#     h -= b

# print(d)

# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]

# for x in data:
#     b = x[2]%x[0]
#     if b==0:
#         a = x[2]//x[0]
#         floor = x[0]*100 + a
#     else:
#         a = x[2]//x[0]+1
#         floor = b*100 + a
#     print(floor)

# n = int(input())

# k = n%5
# a = n//5

# if (k == 1) and (a > 0):
#     a += 1
# elif (k == 2) and (a > 1):
#     a += 2
# elif (k == 3):
#     a += 1
# elif (k == 4) and (a > 0):
#     a += 2
# elif (k != 0):
#     a = -1

# print(a)
# 5a => a
# 5a+1 => 5(a-1)+6
# 5a+2 => 5(a-2)+12
# 5a+3 => 5a+3
# 5a+4 => 5(a-1)+9



# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True

# n = int(input())

# nums = [int(x) for x in input().split()]
# cnt = 0
# for x in nums:
#     if prime(x) == True:
#         cnt += 1

# print(cnt)

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True

# a = int(input())
# b = int(input())
# sum = 0
# min = -1

# if a==b:
#     if prime(a):
#         sum=a
#         min=a
# else:
#     for i in range(b,a-1,-1):
#         if prime(i):
#             sum += i
#             min = i

# if min == -1:
#     print(min)
# else:
#     print(sum)
#     print(min) 

# import math
# import sys

# while 1:
#     n = int(input())
#     if n==0:
#         break
#     else:
#         cnt = 0
#         a = [False,False] + [True]*(n-1)

#         for i in range(2,n+1):
#             if a[i]:
#                 cnt += 1
#                 for j in range(2*i, n+1, i):
#                     a[j] = False
#         print(cnt)

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True

# p = int(input())
# for i in range(1,p+1):
#     a = int(input())
#     if prime(a//2):
#         print(a//2,a//2)
#     else:
#         for j in range(a//2-1,2,-1):
#             if prime(j) and prime(a-j):
#                 print(j,a-j)
#                 break

# def recursive(cnt,n):
#     if cnt<n:
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print('\"재귀함수가 뭔가요?\"')
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
#         cnt+=1
#         recursive(cnt,n)
#         for i in range(1,cnt):
#             print("____",end="")
#         print("라고 답변하였지.")
#     elif cnt==n:
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print('\"재귀함수가 뭔가요?\"')
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
#         for i in range(1,cnt+1):
#             print("____",end="")
#         print("라고 답변하였지.")
# n = int(input())
# cnt = 1
# print("""어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어." """)
# recursive(cnt,n)
# print("라고 답변하였지.")

# n,black = map(int,input().split())

# nums = [int(x) for x in input().split()]

# max=0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if nums[i]+nums[j]+nums[k]==black:
#                 print(nums[i]+nums[j]+nums[k])
#                 quit()
#             elif (nums[i]+nums[j]+nums[k]<black) and (nums[i]+nums[j]+nums[k]>max):
#                 max = nums[i]+nums[j]+nums[k]
# print(max)
            
# a,b,c=map(int,input().split())

# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

# a = int(input())

# if a>=90:
#     print("A")
# elif a>=80:
#     print("B")
# elif a>=70:
#     print("C")   
# elif a>=60:
#     print("D")
# else:
#     print("F")

# a = int(input())
# b = int(input())

# if a>0:
#     if b>0:
#         print(1)
#     else:
#         print(4)
# else:
#     if b>0:
#         print(2)
#     else:
#         print(3)

# a,b,c=map(int,input().split())

# if a==b and b==c:
#     print(10000+a*1000)
# elif a==b:
#     print(1000+a*100)
# elif b==c:
#     print(1000+b*100)
# elif a==c:
#     print(1000+a*100)
# else:
#     max=0
#     if a<b:
#         max=b
#     else:
#         max=a
#     if max<c:
#         max=c
#     print(100*max)

# n = int(input())
# for i in range(n):
#     a,b=input().split()
#     print(int(a)+int(b))

# n = int(input())
# for i in range(n):
#     a,b=input().split()
#     print("Case #{}: {} + {} = {}".format(i+1,int(a),int(b),int(a)+int(b)))

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# n,x = map(int,input().split())
# nums = [int(x) for x in input().split()]
# for i in nums:
#     if i<x:
#         print(i,end=' ')

# while 1:
#     a,b = map(int,input().split())
#     if a==0 and b==0:
#         break
#     else:
#         print(a+b)

# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except EOFError:
#         break

# a = int(input())
# b = int(input())
# c = int(input())

# d = str(a*b*c)
# for i in range(10):
#     print(d.count(str(i)))

# a=[]
# for i in range(10):
#     a.append(int(input())%42)
# print(len(set(a)))

# a = int(input())
# for i in range(a):
#     s = input()
#     cnt=0
#     sum=0
#     for b in s:
#         if b=="O":
#             cnt+=1
#             sum+=cnt
#         else:
#             cnt=0
#     print(sum)

# def solve(a):
#     sum = 0
#     for i in a:
#         sum+=i
#     return sum

# a = int(input())
# b = input()
# c = []
# for i in b:
#     c.append(int(i))
# print(sum(c))

# a = input()
# for i in range(26):
#     print(a.find(chr(i+97)))

# a = int(input())
# for i in range(a):
#     a,b=input().split()
#     for j in b:
#         print(j*int(a),end="")
#     print()

# a,b = input().split()
# a1 = list(a)
# b1 = list(b)
# a1.reverse()

# b1.reverse()

# a2 = ''.join(a1)
# b2 = ''.join(b1)
# if int(a2)>int(b2):
#     print(a2)
# else:
#     print(b2)

# a = input()
# cnt = 0
# for x in a:
#     if x=="A" or x=="B" or x=="C":
#         cnt+=3
#     elif x=="D" or x=="E" or x=="F":
#         cnt+=4
#     elif x=="G" or x=="H" or x=="I":
#         cnt+=5
#     elif x=="J" or x=="K" or x=="L":
#         cnt+=6
#     elif x=="M" or x=="N" or x=="O":
#         cnt+=7
#     elif x=="P" or x=="Q" or x=="R" or x=="S":
#         cnt+=8
#     elif x=="T" or x=="U" or x=="V":
#         cnt+=9
#     elif x=="W" or x=="X" or x=="Y" or x=="Z":
#         cnt+=10
# print(cnt)

# n = int(input())

# groupword = 0

# for i in range(n):
#     word = input()
#     alphabet = []
#     groupword += 1
#     for j in range(len(word)):
#         if len(word) == 1:
#             break
#         elif (word[j] in alphabet) and (word[j] != word[j-1]):
#             groupword -= 1
#             break
#         else:
#             alphabet.append(word[j])
# print(groupword)
 
# x = int(input())

# for i in range(1,x+1):
#     if i*(i+1)//2 >= x: #군수열의 몇군인지 찾기
#         seq = i # 군
#         term = x-seq*(seq-1)//2 # 항
    
#         if seq%2 == 1:  #홀수 군일때
#             print("{}/{}".format(seq+1-term,term))
#         else:           #짝수 군일때
#             print("{}/{}".format(term,seq+1-term))
#         break

# def family(k,n):
#     if k==1:    # 1층이면 1호~n호 까지의 합
#         return n*(n+1)//2   
#     else:       # 1층이 아니면 바로아래층 1호~n호까지의 합
#         sum = 0
#         for i in range(1,n+1):
#             sum += family(k-1,i)
#         return sum

# T = int(input())

# for i in range(T):
#     k = int(input())
#     n = int(input())
#     print(family(k,n))

# T = int(input())

# for i in range(T):
#     k = int(input())
#     n = int(input())
#     number_family = [x for x in range(1,n+1)]

#     for x in range(k):
#         for y in range(1,n):
#             number_family[y] += number_family[y-1]
            
#     print(number_family[-1])

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# n = int(input())

# print(factorial(n))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n = int(input())

# print(fibonacci(n))

# n = int(input())

# data = []
# for i in range(n):
#     data.append(int(input()))

# for i in range(n-1):
#     for j in range(i,n):
#         if data[i]>data[j]:
#             temp=data[i]
#             data[i]=data[j]
#             data[j]=temp

# for i in data:
#     print(i)

# n = int(input())

# data = []
# for i in range(n):
#     data.append(input())

# sorted_data = sorted(data)
# for i in sorted_data:
#     print(i)

# while 1:
#     a,b = map(int,input().split())
#     if a==0 and b==0:
#         break
#     elif b%a==0:
#         print('factor')
#     elif a%b==0:
#         print('multiple')
#     else:
#         print('neither')

# n = int(input())

# nums = [int(x) for x in input().split()]

# data = sorted(nums)

# print(data[0]*data[n-1])

# a,b = map(int,input().split())

# if a>b:
#     c=b
# else:
#     c=a

# for i in range(c,0,-1):
#     if a%i==0 and b%i==0:
#         gcd = i
#         break

# print(gcd)
# print(a*b//gcd)

# def gcd(a,b):
#     while a!=0:
#         if a<b:
#             a,b=b,a
#         a%=b
#     return b

# n = int(input())

# for i in range(n):
#     a,b = map(int,input().split())
#     print(a*b//gcd(a,b))

# def gcd(a,b):
#     while a!=0:
#         if a<b:
#             a,b=b,a
#         a%=b
#     return b

# n = int(input())

# data = [int(x) for x in input().split()]

# for i in range(1,n):
#     gcd_a_b = gcd(data[0],data[i])
#     print("{}/{}".format(data[0]//gcd_a_b,data[i]//gcd_a_b))

# def factorial(n):
#     result=1
#     for i in range(2,n+1):
#         result*=i
#     return result

# T = int(input())
# for i in range(T):
#     n,m = map(int,input().split())
#     print(factorial(m)//factorial(n)//factorial(m-n))

# def factorial(n):
#     result=1
#     for i in range(2,n+1):
#         result*=i
#     return result

# T = int(input())
# for i in range(T):
#     n = int(input())
#     wearing = []
#     for j in range(n):
#         a,b = input().split()
#         wearing.append(b)
#     set_wearing = set(wearing)
#     n = len(wearing)
#     m = len(set_wearing)
#     print(n*m-1)

# n = int(input())

# print((n//5)+(n//25)+(n//125))

# def zerocount(n):
#     result = 0
#     div = 5
#     while div<=n:
#         result += n//div
#         div *= 5
#     return result

# n,m = map(int,input().split())

# print(zerocount(n)-zerocount(m)-zerocount(n-m))

# x,y,w,h = map(int,input().split())

# if x>w/2:
#     x = w-x
# if y>h/2:
#     y = h-y
# if x<y:
#     print(x)
# else:
#     print(y)

# point = []

# for i in range(3):
#     point.append(input().split())

# if point[0][0]==point[1][0]:
#     x = point[2][0]
# elif point[1][0]==point[2][0]:
#     x = point[0][0]
# else:
#     x = point[1][0]
# if point[0][1]==point[1][1]:
#     y = point[2][1]
# elif point[1][1]==point[2][1]:
#     y = point[0][1]
# else:
#     y = point[1][1]

# print(x,y)

# while True:
#     a,b,c = map(int,input().split())
#     if a==0:
#         break  
#     triangle = []
#     triangle.append(a)
#     triangle.append(b)
#     triangle.append(c)
#     triangle.sort()
#     if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
#         print('right')
#     else:
#         print('wrong')

# import math
# n,w,h = map(int,input().split())

# for i in range(n):
#     x = int(input())
#     diagonal = math.sqrt(w*w+h*h)
#     if x<=diagonal:
#         print('DA')
#     else:
#         print('NE')

# k = int(input())

# direction = []
# length = []

# for i in range(6):
#     a,b = map(int,input().split())
#     direction.append(a)
#     length.append(b)

# if direction[0] == direction[2]:
#     big_x = length[4]
#     small_x = length[0]
# else:
#     big_x = length[0]
#     small_x = length[4]
# if direction[1] == direction[3]:
#     big_y = length[5]
#     small_y = length[1]
# else:
#     big_y = length[1]
#     small_y = length[3]

# print(big_x,big_y,small_x,small_y)
# print((big_x*big_y - small_x*small_y)*k)

# import math

# r = int(input())

# print("{:.6f}".format(r*r*math.pi))
# print("{:.6f}".format(r*r*2))

# n,m = map(int,input().split())

# data = [int(x) for x in input().split()]

# for i in range(n-1):
#     data[i+1] += data[i]

# for x in range(m):
#     i,j = map(int,input().split())
#     if i==1:
#         print(data[j-1])
#     else:
#         print(data[j-1]-data[i-2])

# def d(num):
#     num1=num
#     len=0
#     while num1:
#         num1//=10
#         len+=1

#     ans=num
#     for i in range(len):
#         ans+=int(str(num)[i])
    
#     return ans

# self_number = []
# for i in range(1,10001):
#     self_number.append(d(i))

# for i in range(1,10000):
#     if i in self_number:
#         continue
#     else:
#         print(i)

# def hansu(n):
#     if n < 100:
#         return True
#     else:
#         hundreds = n // 100
#         tens = (n - hundreds * 100) // 10 % 10
#         ones = n % 100 % 10

#         if (hundreds - tens) == (tens - ones):
#             return True
#         else:
#             return False

# n = int(input())

# cnt = 0
# for i in range (1,n+1):
#     if hansu(i):
#         cnt += 1

# print(cnt)

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True

# m = int(input())
# n = int(input())

# data_prime = []
# for i in range(m,n+1):
#     if prime(i):
#         data_prime.append(i)

# if data_prime == []:
#     print(-1)
# else:
#     print(sum(data_prime))
#     print(data_prime[0])

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True
# n = int(input())

# curr_prime = 2
# while n != 1:
#     for i in range(curr_prime,n+1):
#         if n%i ==0:
#             n //= i
#             curr_prime = i
#             print(i)
#             break

# print('''|\_/|
# |q p|   /} 
# ( 0 )"""\ 
# |"^"`    |
# ||_/=\\\__|''')

# n = 123456 * 2

# prime_table = [False,False]+[True]*(n-1)

# for i in range(2,int(n ** 0.5)+1):
#     if prime_table[i] == True:
#         for j in range(2 * i,n+1,i):
#             prime_table[j] = False

# while True:
#     n = int(input())

#     if n == 0:
#         break
    
#     print(prime_table[n+1:2*n+1].count(True))


# def dcs(n):
#     num_len = len(str(n))
#     sum = n
#     for i in range(num_len):
#         sum += n%10
#         n = n - n%10
#         n //= 10
#     return sum

# n = int(input())

# ctor = 0

# for i in range(1,n+1):
#     if n == dcs(i):
#         print(i)
#         ctor = i
#         break

# if ctor == 0:
#     print(0)

# n = int(input())

# weight = []
# height = []

# for _ in range(n):
#     a,b = map(int,input().split())
#     weight.append(a)
#     height.append(b)

# for i in range(n):
#     loses = 0
#     for j in range(n):
#         if weight[i]<weight[j] and height[i]<height[j]:
#             loses += 1
#     print(loses + 1,end=' ')

# n,m = map(int,input().split())

# chess = []
# w_chess=['WBWBWBWB','BWBWBWBW'] * 4
# b_chess=['BWBWBWBW','WBWBWBWB'] * 4

# for _ in range(n):
#     chess.append(input())

# min = 64
# for i in range(0,n-7):
#     for j in range(0,m-7):
#         cnt = 0
#         for p in range(8):
#             for q in range(8):
#                 if chess[p+i][j+q] != w_chess[p][q]:
#                     cnt += 1
#         if min > cnt:
#             min = cnt
        
#         cnt = 0
#         for p in range(8):
#             for q in range(8):
#                 if chess[p+i][j+q] != b_chess[p][q]:
#                     cnt += 1
#         if min > cnt:
#             min = cnt

# print(min)

# n = int(input())

# cnt = 0
# num = 665
# while cnt != n:
#     num += 1
#     if '666' in str(num):
#         cnt += 1

# print(num)

# n = int(input())

# data = []
# for i in range(n):
#     data.append(input())

# for i in range(n):  
#     child = i
#     while child != 0:
#         root = (child - 1) // 2
#         if data[root] < data[child]:
#             data[root],data[child] = data[child],data[root]
#         child = root

# for j in range(n-1,-1,-1):
#     data[0],data[j] = data[j],data[0]
#     root = 0
#     child = 1
#     while child < j:
#         child = 2*root + 1
#         if (child < j-1) and (data[child] < data[child+1]):
#             child += 1
#         if (child < j) and (data[root] < data[child]):
#             data[root],data[child] = data[child],data[root]
#         root = child

# for i in data:
#     print(i)

# import sys
# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(sys.stdin.readline()))
# for i in sorted(data):
#     print(i)

# from collections import Counter
# import sys

# n = int(input())
# nums = []

# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))

# print(round(sum(nums)/n))       #평균

# nums.sort()
# print(nums[n//2])           #중앙값

# cnt = Counter(nums).most_common(2)  #최빈값
# if len(cnt) == 2:
#     if cnt[0][1] == cnt[1][1]:  
#         print(cnt[1][0])        
#     else:
#         print(cnt[0][0])        
# else:
#     print(cnt[0][0])

# print(max(nums)-min(nums))      #범위

# n = input()
# l = len(n)
# m = sorted(n)
# for i in range(l):
#     print(m[l-i-1],end='')

# import sys

# n = int(input())

# coordinates = [[0 for col in range(2)] for row in range(n)]

# for i in range(n):
#     a,b = sys.stdin.readline().split()
#     coordinates[i][0] = int(b)
#     coordinates[i][1] = int(a)

# coordinates.sort()

# for i in range(n):
#     print(coordinates[i][1],coordinates[i][0])

# import sys

# n = int(input())

# words = [[0 for _ in range(2)] for _ in range(n)]

# for i in range(n):
#     a = sys.stdin.readline()
#     words[i][0] = len(a)
#     words[i][1] = a

# words.sort()
# for i in range(n):
#     if i != n-1:
#         if words[i][1] == words[i+1][1]:
#          continue
#     sys.stdout.write(words[i][1])

# import sys

# n = int(input())

# members = []
# for i in range(n):
#     a, b = sys.stdin.readline().split()
#     members[i][0] = int(a)
#     members[i][1] = b

# members.sort(key = lambda x:x[0])

# for i in members:
#     print(i[0],i[1])

# import sys

# n = int(input())
# c = list(map(int, sys.stdin.readline().split()))

# d = sorted(list(set(c)))

# e = {}
# for i in range(len(d)):
#     e[d[i]]=i
# for x in c:
#     print(e[x],end=' ')
            
# import sys

# n = int(input())
# nums = [0]*10000
# for _ in range(n):
#     nums[int(sys.stdin.readline())-1] += 1

# for i in range(10000):
#     if nums[i] != 0:
#         for _ in range(nums[i]):
#             print(i+1)

# nums_s = sorted(list(set(nums)))
# dict = {}
# for i in range(len(nums_s)):
#     dict[nums_s[i]] = 0

# for i in range(n):
#     dict[nums[i]] += 1

# for i in dict:
#     for _ in range(dict[i]):
#         print(i)

# m = max(nums)
# cnt = [0]*m

# for i in range(n):
#     cnt[nums[i]-1] += 1

# for i in range(m):
#     if cnt[i] != 0:
#         for _ in range(cnt[i]):
#             print(i+1)

# import sys
# input = sys.stdin.readline

# def bs(data,target):
#     start = 0
#     end = len(data)-1
#     mid = (start+end)//2

#     while(end-start>=0):
#         if data[mid] == target:
#             return 1
#         elif data[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#         mid = (start+end) // 2
    
#     return 0

# n = int(input())
# a = list(map(int,input().split()))
# a1 = sorted(a)

# m = int(input())
# b = list(map(int,input().split()))

# print(a1)
# print(b)
# for x in b:
#     print(bs(a1,x),end=' ')

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# s = [0]*n
# p = [0]*m
# for i in range(n):
#     s[i] = input()
# for i in range(m):
#     p[i] = input()

# cnt = 0
# for x in p:
#     if x in s:
#         cnt += 1
# print(cnt)

# import sys
# input = sys.stdin.readline
# n ,m = map(int,input().split())

# dict = {}
# for i in range(1,n+1):
#     a = input().strip()
#     dict[i] = a
#     dict[a] = i

# for _ in range(m):
#     quiz = input().strip()
#     if quiz.isdigit():
#         print(dict[int(quiz)])
#     else:
#         print(dict[quiz])

# import sys
# input = sys.stdin.readline

# def bs(data,target):
#     start = 0
#     end = len(data)-1
#     mid = (start+end)//2

#     while(end-start>=0):
#         if data[mid] == target:
#             return mid
#         elif data[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#         mid = (start+end) // 2
    
#     return 0

# n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
# b = list(map(int,input().split()))

# a1 = sorted(a)

# for x in b:
#     c = bs(a1,x)
#     if c == 0:
#         print(0,end=' ')
#     else:
#         cnt = 1
#         for i in range(c+1,n):
#             if a1[c] == a1[i]:
#                 cnt += 1
#             else:
#                 break
#         for i in range(c-1,-1,-1):
#             if a1[c] == a1[i]:
#                 cnt += 1
#             else:
#                 break
#         print(cnt,end=' ')

# [-10, -10, 2, 3, 3, 6, 7, 10, 10]

# import sys 
# n = sys.stdin.readline()
# N = map(int,sys.stdin.readline().split())
# m = sys.stdin.readline()
# M = map(int,sys.stdin.readline().split())

# hashmap = {}
# for x in N:
#     if x in hashmap:
#         hashmap[x] += 1
#     else:
#         hashmap[x] = 1

# for x in M:
#     if x in hashmap:
#         print(hashmap[x],end=' ')
#     else:
#         print(0,end=' ')

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())

# N = {}
# for i in range(n):
#     N[input().strip()] = i

# idx = []
# cnt = 0

# for i in range(m):
#     M = input().strip()
#     if N[M] >= 0:
#         cnt += 1
#         idx.append(N[M])

# print(cnt)
# for i in idx:
#     print(M[i])

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())

# dict = {}
# cnt = 0
# for i in range(n+m):
#     a = input().strip()
#     if a in dict:
#         dict[a] += 1
#         cnt += 1
#     else:
#         dict[a] = 1

# print(cnt)
# a = []
# for x in dict:
#     if dict[x] == 2:
#         a.append(x)

# a.sort()
# for x in a:
#     print(x)

# import sys
# input = sys.stdin.readline

# a,b = map(int,input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# C = A+B     #합
# D = set(C)  #합집합
# E = len(D)  #n(합집합)
# F = a+b-E   #n(교집합)
# G = E-F     #n(대칭차집합)
# print(G)

# s = input()

# part = []

# for i in range(1,len(s)+1):     #i:부분문자열의길이
#     for j in range(len(s)-i+1): #j:부분문자열시작위치
#         part.append(s[j:j+i])

# print(len(set(part)))

# n, m = map(int, input().split())

# a = []
# def p(k):
#   if len(a) == m:
#     print(' '.join(map(str, a)))
#     return

#   for i in range(k,n+1):
#     # if i in a:
#     #   continue
#     a.append(i)
#     p(i)
#     a.pop()

# p(1) 

# def attack(x):
#     for i in range(x):
#         if chess_x[x] == chess_x[i] or abs(chess_x[x] - chess_x[i]) == abs(x-i):
#             return True
#     return False

# def chess(x):
#     global cnt
#     if x==n:
#         cnt += 1
#         return
#     else:
#         for y in range(n):
#             chess_x[x] = y
#             if attack(x) == False:
#                 chess(x+1)

# n = int(input())
# chess_x = [0] * n
# cnt = 0
# chess(0)
# print(cnt)

# def fib(n):
#     f[1] = 1
#     f[2] = 1
#     for i in range(3,n+1):
#         f[i] = f[i-1]+f[i-2]
#     return f[n]

# n = int(input())
# f = [0]*(n+1)
# print(fib(n),n-2)

# import sys
# input = sys.stdin.readline
# n = int(input())

# s = []
# idx = 0
# for _ in range(n):
#     order = input().rstrip().split()
#     if order[0] == 'push':  
#         s.append(order[1])
#         idx += 1
#     elif order[0] == 'pop':
#         if idx == 0:
#             print(-1)
#             continue
#         else:
#             print(s[idx-1])
#             idx -= 1
#             s.pop()
#     elif order[0] == 'size':
#         print(idx)
#     elif order[0] == 'empty':
#         if idx == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         if idx == 0:
#             print(-1)
#         else:
#             print(s[idx-1])

# k = int(input())

# a = []
# for _ in range(k):
#     b = int(input())
#     if b==0:
#         a.pop()
#     else:
#         a.append(b)

# print(sum(a))

# import sys

# n = int(sys.stdin.readline())
# for _ in range(n):
#     data = sys.stdin.readline().strip()
#     stack = 0
#     vps = 1
#     for x in data:
#         if x == '(':
#             stack += 1
#         else:
#             if stack == 0:
#                 vps = 0
#                 break
#             else:
#                 stack -= 1
#     if vps == 0 or stack != 0:
#         print('NO')
#     else:
#         print('YES') 

# import sys
# while True:
#     s = sys.stdin.readline().rstrip()
#     if s == '.':
#         break

#     a = [0]
#     ans = 'yes'

#     for x in s:
#         if x == '[':
#             a.append(1)          
#         elif x == '(':
#             a.append(2)        
#         elif x == ']':
#             if a[len(a)-1] == 1:
#                 a.pop()
#             else:
#                 ans = 'no'
#                 break
#         elif x == ')':
#             if a[len(a)-1] == 2:
#                 a.pop()
#             else:
#                 ans = 'no'
#                 break
#         else:
#             continue
#     if len(a) != 1:
#         ans = 'no'   
#     print(ans)

# import sys
# n = int(sys.stdin.readline())

# a = []
# ans = []
# p = ''
# idx = 0
# for i in range(n):
#     x = int(sys.stdin.readline())

#     while idx < x:
#         idx += 1
#         a.append(idx)
#         ans.append('+')

#     if a[-1] == x:
#         a.pop()
#         ans.append('-')
#     else:
#         p = 'NO'
#         break

# if p == 'NO':
#     print(p)
# else:
#     print("\n".join(ans))

# n = int(input())
# a = list(map(int,input().split()))
# ans = [-1]*n
# stack = []

# for i in range(n):
#     while stack and a[stack[-1]] < a[i]:
#         ans[stack.pop()] = a[i]
#     stack.append(i)
# print(*ans)

#18258번 큐2

# import sys
# input = sys.stdin.readline

# n = int(input())
# q = []
# idx = 0

# for _ in range(n):
#     a = input().rstrip().split()
#     empty = (not q) or (len(q) - idx <= 0)

#     if a[0] == 'push':
#         q.append(a[1])
#     elif a[0] == 'pop':
#         if empty:
#             print(-1)
#         else:
#             print(q[idx])
#             idx += 1
#     elif a[0] == 'size':
#         if empty:
#             print(0)
#         else:
#             print(len(q)-idx)
#     elif a[0] == 'empty':
#         if empty:
#             print(1)
#         else:
#             print(0)
#     elif a[0] == 'front':
#         if empty:
#             print(-1)
#         else:
#             print(q[idx])
#     else: # back
#         if empty:
#             print(-1)
#         else:
#             print(q[-1])

#2164번 카드2

# n = int(input())
# cards = [i for i in range(1,n+1)]
# idx = 0

# while True:
#     idx += 1 # 1장 버리기
#     if len(cards) == idx: # 1장 남을때 종료
#         break
#     cards.append(cards[idx]) # 카드 옮기기
#     idx += 1

# print(cards[-1])

#11866번 요세푸스

# n,k = map(int,input().split())
# c = [i for i in range(1,n+1)] 
# jsps = []
# idx = -1

# while len(jsps) < n:
#     for i in range(idx+1,idx+k): # k-1 명 뒤로 붙이기
#         c.append(c[i])
#         idx += 1
#     idx += 1
#     jsps.append(c[idx]) # 제거된 번호 저장

# print('<'+', '.join(map(str,jsps))+'>')

#1966번 프린터 큐
# t = int(input())
# for _ in range(t):
#     n,q = map(int,input().split())
#     a = [i for i in range(n)]           #문서번호
#     b = list(map(int,input().split()))  #중요도
#     cnt = 0                             #인쇄매수
#     idx = 0                             #queue의 front index

#     while True:
#         if len(b[idx:]) == 1:   # 문서가 한개남았을때 인쇄
#             cnt += 1
#             break
#         elif len(b[idx:]) == 2: # 문서가 두개남았을때 
#             if b[idx] < b[-1]:  # 앞이 중요도가 낮고 문제의 문서라면 카운트+2 아니면 +1
#                 if a[idx] == q: 
#                     cnt += 2
#                 else:
#                     cnt += 1
#             else:               # 앞이 중요도가 낮지 않고 문제의 문서라면 카운트 +1 아니면 +2
#                 if a[idx] == q: 
#                     cnt += 1
#                 else:
#                     cnt += 2
#             break
#         elif b[idx] < max(b[idx:]): # 현재 순서의 중요도가 뒤의 중요도보다 낮다면 뒤에 재배치
#             a.append(a[idx])
#             b.append(b[idx])
#             idx += 1
#         else:   # 인쇄하는데 문제의 문서를 인쇄한다면 인쇄후 종료 , 아니라면 인쇄후 반복
#             if a[idx] == q:
#                 cnt += 1
#                 break
#             else:
#                 idx += 1
#                 cnt += 1
        
#     print(cnt)

#1920번 수 찾기
# import sys
# input = sys.stdin.readline
# n = int(input())
# N = list(map(int,input().split()))
# m = int(input())
# M = list(map(int,input().split()))

# hashmap = {}
# for x in N:
#     if x not in hashmap:
#         hashmap[x] = 1

# for x in M:
#     if x in hashmap:
#         print(1)
#     else:
#         print(0)

#11399번 ATM

# n = int(input())
# a = [int(x) for x in input().split()]

# a.sort()
# for i in range(1,n):
#     a[i] += a[i-1]
# for i in range(1,n):
#     a[i] += a[i-1]

# print(a[-1])

# 1541번 잃어버린 괄호

# a = input()
# m = 1       # 더할때의 계수 -부호가 나오면 -1
# ans = 0     # 계산결과
# temp = ''   # 숫자
# for x in a:
#     if x == '-':    # 계수를 곱하고 더하고 계수는 -1
#         ans += int(temp)*m
#         m = -1
#         temp = ''
#     elif x == '+':  # 계수를 곱하고 더한다
#         ans += int(temp)*m
#         temp = ''
#     else:
#         temp += x
# ans += int(temp)*m #마지막 숫자계산
# print(ans)

# 13305번 주유소

# n = int(input())
# len = list(map(int,input().split()))           
# price = list(map(int,input().split()))       
# low = price[0]
# sum = 0
# for i in range(n-1):
#     if low>price[i]:
#         low = price[i]
#     sum += low*len[i]
# print(sum)

# 11407번 동전 0

# n,k = map(int,input().split())
# a = [0]*n
# for i in range(n):
#     a[i] = int(input())
# cnt = 0

# for i in range(n-1,-1,-1):
#     print(a[i])
#     if a[i]<=k:
#         cnt += k//a[i]
#         k %= a[i]
#     if k==0:
#         break

# print(cnt)

# 4375번 1

# import sys
# for num in sys.stdin.readlines():
#     if int(num) == (10**len(num.rstrip())-1)//9:    # 1,11,111,1111 
#         print(len(num.rstrip()))
#         continue
#     ans = 3
#     while True:
#         if ((10**ans - 1)//9)%(int(num)) == 0: # 1이 ans개인 수를 주어진 수로 나눠본다
#             break
#         ans += 1   
#     print(ans)

# 6588번 골드바흐의추측

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#     return True

# 2309번 일곱 난쟁이

# h = []
# for i in range(9):
#     h.append(int(input()))
# h.sort()
# p = sum(h)-100      

# for i in range(9):
#     for j in range(i+1,9): 
#         if h[i]+h[j] == p:
#             a=i
#             b=j

# for i in range(9):
#     if i != a and i != b:
#         print(h[i])

#1476번 날짜계산

# e,s,m = map(int,input().split())
# ans = s
# k = 28

# while True:
#     if ans % 19 == m:
#         if ans % 15 == e:
#             print(ans)
#             break
#         else:
#             k = 28*19
#     elif ans % 15 == e:
#         k = 28*15
#     ans += k

#2447번 별찍기-10

# def draw_star(n):
#     global map

#     if n == 3:
#         map[0][:3] = map[2][:3] = [1]*3
#         map[1][:3] = [1,0,1]
#         return
    
#     a = n // 3
#     draw_star(n//3)

#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 map[a*i + k][a*j:a*(j+1)] = map[k][:a]

# n = int(input())
# map = [[0 for _ in range(n)] for _ in range(n)]

# draw_star(n)

# for i in map:
#     for j in i:
#         if j:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

#9093번 단어 뒤집기

# n = int(input())
# for _ in range(n):
#     sentence = list(map(str,input().split()))
#     for word in sentence:
#         for i in range(len(word)):
#             print(word[len(word)-1-i],end='')
#         print(' ',end='')
#     print()

#9375번 패션왕신혜빈

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     wearings = []
#     for i in range(n):
#         wearings.append(input().split())
#     hashmap = {}
#     for x in wearings:
#         if x[1] not in hashmap:
#             hashmap[x[1]] = 1
#         else:
#             hashmap[x[1]] += 1
#     ans = 1
#     for x in hashmap:
#         ans *= hashmap[x]+1
#     print(ans-1)

#2559번 수열

# n,k = map(int,input().split())
# t = list(map(int,input().split()))

# max = s = sum(t[:k])

# for i in range(k,n):
#     s += t[i] - t[i-k]
#     if s > max:
#         max = s

# print(max)

#1748번 수 이어 쓰기 1

# n = int(input())
# ans = 0
# k = 0
# while True:
#     if 10**k * 9 < n:   
#         ans += (10**k * 9) * (k+1)
#         n -= 10**k * 9
#         k += 1
#     else:
#         ans += n * (k+1)
#         break

# print(ans)

#11729번 하노이 탑
                                
# def move(n,a,b):   #n개를 a에서 b로 옮겨라             
#     if n == 1:                  
#         print(a,b) 
#         return                                   
#     move(n-1,a,6-a-b)
#     move(1,a,b)
#     move(n-1,6-a-b,b)

# n = int(input())
# ans = 0
# for _ in range(n):
#     ans = ans*2+1
# print(ans)

# move(n,1,3)


#17413번 단어 뒤집기

# s = input()
# temp = ""
# for x in s:
#     if x == "<" :
#         print(''.join(list(reversed(temp))),end='')
#         temp = x
#     elif x == ">":
#         print(temp,end='>')
#         temp = ""
#     else:
#         if x == ' ' and temp[0] != '<':
#             print(''.join(list(reversed(temp))),end=' ')
#             temp = ''
#         else:
#             temp += x

# if len(temp) != 0:
#     print(''.join(list(reversed(temp))),end=' ')

#11656번 접미사 배열

# s = input()
# suffix = []
# for i in range(len(s)):
#     suffix.append(s[i:])
# suffix.sort()
# for x in suffix:
#     print(x)

#3053번 택시 기하학

# import math

# n = int(input())
# print("{:.6f}".format(n**2*math.pi))
# print("{:.6f}".format(n**2*2))

#1358번 하키
# import sys
# input = sys.stdin.readline

# w,h,x,y,p = map(int,input().split())
# # w,h,x,y,p = 20, 10, 0, 0, 14
# r = h//2
# players = [list(map(int,sys.stdin.readline().split())) for i in range(p)]
# # players = [[-5,5],[-4,2],[-4,8],[-3,1],[-3,9],[0,0],[0,10],[20,0],[20,10],[23,1],[23,9],[24,2],[24,8],[25,5]]
# cnt = 0

# for a in players:
#     if a[0] >= x and a[0] <= x + w:
#         if a[1] >= y and a[1] <= y + h:
#             cnt += 1   
#     elif a[0] < x and a[1] > y and a[1] < y + h:
#         if ((a[0]-x)**2 + (a[1]-y-r)**2) ** 0.5 <= r:
#             cnt += 1
#     elif a[0] > x + w and a[1] > y and a[1] < y + h:
#         if ((a[0]-x-w)**2 + (a[1]-y-r)**2) ** 0.5 <= r:
#             cnt += 1
            
# print(cnt)

#1100 하얀 칸

# first = 0
# cnt = 0

# for _ in range(8):
#     data = input()
#     for i in range(first,8,2):
#         if data[i] == 'F':
#             cnt += 1
#     if not first:
#         first = 1
#     else:
#         first = 0

# print(cnt)

#2477번 참외밭

# #큰 직사각형 - 작은 직사각형을 이용한 넓이구하기
# k = int(input())
# data = [list(map(int,input().split())) for i in range(6)]
# max_w = 0
# max_h = 0
# #큰 직사각형의 가로세로 길이와 위치 저장
# for i in range(6):          
#     if data[i][0] == 1 or data[i][0] == 2:
#         if max_w < data[i][1]:
#             max_w = data[i][1]
#             max_w_i = i
#     if data[i][0] == 3 or data[i][0] == 4:
#         if max_h < data[i][1]:
#             max_h = data[i][1]
#             max_h_i = i
# # 큰 직사각형의 가로세로 위치와 인접한 양변의 길이의 차
# if max_w_i == 5:       
#     area_small = abs((data[max_w_i-1][1]-data[0][1]) * (data[max_h_i+1][1]-data[max_h_i-1][1]))
# elif max_h_i == 5:
#     area_small = abs((data[max_h_i-1][1]-data[0][1]) * (data[max_w_i+1][1]-data[max_w_i-1][1]))
# else:
#     area_small = abs((data[max_h_i-1][1]-data[max_h_i+1][1]) * (data[max_w_i+1][1]-data[max_w_i-1][1]))

# print(k*(max_h*max_w-area_small))

#1002번 터렛

# #두 점 사이의 거리와 반지름을 이용한 풀이
# # x1,y1,r1,x2,y2,r2 = 0,0,13,40,0,37
# # x1,y1,r1,x2,y2,r2 = 0,0,3,0,7,4
# # x1,y1,r1,x2,y2,r2 = 1,1,1,1,1,5
# T = int(input())
# for _ in range(T):
#     x1,y1,r1,x2,y2,r2 = map(int,input().split())
#     d = ((x1-x2)**2 + (y1-y2)**2)**0.5  #두점사이의거리
#     if d==0 and r1==r2:     # 완전히 같은 원
#         print(-1)
#     elif d < abs(r1-r2) or d > r1+r2:    # 한 원이 내부에 포함돼있거나 외부에서 만나지 않는경우
#         print(0)
#     elif d == abs(r1-r2) or d == r1+r2:  # 내접하는 경우와 외접하는 경우
#         print(1)
#     else:                # 두점에서 만나는 경우
#         print(2)

#1004번 어린왕자

# x1,y1,x2,y2 = -5,1,12,1
# n = 7
# planets = [[1,1,8],[-3,-1,1],[2,2,2],[5,5,1],[-4,5,1],[12,1,1],[12,1,2]]
# # 주어진 두 점이 몇개의 원 내부에 있는가 / 같은 원 내부에 있는 경우 제외
# T = int(input())
# for _ in range(T):
#     x1,y1,x2,y2 = map(int,input().split())
#     n = int(input())
#     cnt = 0
#     for i in range(n):
#         p = list(map(int,input().split()))
#         d1 = ((x1-p[0])**2 + (y1-p[1])**2) ** 0.5
#         d2 = ((x2-p[0])**2 + (y2-p[1])**2) ** 0.5
#         p1_in = (d1<p[2])
#         p2_in = (d2<p[2])
#         if p1_in and p2_in:     
#             continue
#         elif p1_in or p2_in:    
#             cnt += 1
#     print(cnt)

#2981번 검문
# def gcd(a,b):
#     while a!=0:
#         if a<b:
#             a,b=b,a
#         a%=b
#     return b

# # n = 5
# # nums = [5,17,23,14,83]
# n = int(input())
# nums = [int(input()) for _ in range(n)]
# g = abs(nums[0]-nums[-1])
# for i in range(n-1):
#     g = gcd(g,abs(nums[i]-nums[i+1]))
#     # if abs(nums[i]-nums[i+1]) > g:
#     #     if (nums[i]-nums[i+1]) % g == 0:
#     #         continue
#     #     else:
#     #         g = gcd(abs(nums[i]-nums[i+1]),g)
#     # elif abs(nums[i]-nums[i+1]) < g:
#     #     if  g % (nums[i]-nums[i+1]) == 0:
#     #         g = abs(nums[i]-nums[i+1])
#     #     else:
#     #         g = gcd(abs(nums[i]-nums[i+1]),g)
# d = []
# for i in range(2,int(g**0.5)+1):
#     if g%i == 0:
#         d.append(i)
#         if i != g//i:
#             d.append(g//i)
# d.sort()
# for x in d:
#     print(x,end=' ')
# print(g)

#2004번 조합 0의 개수

# def cnt_5(x):   # x!의 5의 개수 카운팅
#     cnt = 0
#     exp = 1
#     while x//(5**exp) != 0:
#         cnt += x//(5**exp)
#         exp += 1
#     return cnt

# def cnt_2(x):   # x!의 2의 개수 카운팅
#     cnt = 0
#     exp = 1
#     while x//(2**exp) != 0:
#         cnt += x//(2**exp)
#         exp += 1
#     return cnt

# n,m = map(int,input().split())
# cnt5 = cnt_5(n) - cnt_5(n-m) - cnt_5(m)
# cnt2 = cnt_2(n) - cnt_2(n-m) - cnt_2(m)
# print(min(cnt5,cnt2))           

#2580번 스도쿠

# table = []
# for _ in range(9):
#     table.append(list(map(int,input().split())))
# # table = [[0, 3, 5 ,4 ,6 ,9, 2 ,7 ,8],[7 ,8 ,2, 1, 0, 5 ,6 ,0, 9],
# # [0 ,6, 0 ,2, 7, 8 ,1, 3 ,5],[3, 2, 1, 0 ,4, 6, 8 ,9, 7],[8, 0 ,4 ,9, 1 ,3 ,5, 0, 6]
# # ,[5, 9, 6 ,8 ,2 ,0 ,4,1 ,3],[9, 1, 7, 6 ,5 ,2, 0, 8, 0],[6, 0, 3 ,7 ,0 ,1, 9 ,5 ,2]
# # ,[2 ,5, 8 ,3, 9 ,4 ,7 ,6, 0]]
# blank = []
# for i in range(9):
#     for j in range(9):
#         if table[i][j] == 0:
#             blank.append((i,j))

# def check_x(x,a):
#     for i in range(9):
#         if table[x][i] == a:
#             return False
#     return True

# def check_y(y,a):
#     for i in range(9):
#         if table[i][y] == a:
#             return False
#     return True

# def check_rec(x,y,a):
#     x = x//3*3
#     y = y//3*3
#     for i in range(3):
#         for j in range(3):
#             if table[x+i][y+j] == a:
#                 return False
#     return True

# def dfs(idx):
#     if idx == len(blank):
#         for x in table:
#             for y in x:
#                 print(y,end=' ')
#             print()
#         quit()
#     for i in range(1,10):
#         x = blank[idx][0]
#         y = blank[idx][1]

#         if check_x(x,i) and check_y(y,i) and check_rec(x,y,i):
#             table[x][y] = i
#             dfs(idx+1)
#             table[x][y] = 0

# dfs(0)

#14888번 연산자 끼워넣기

# n = int(input())
# a = list(map(int,input().split()))
# o = list(map(int,input().split()))   # + - * /

# max_result = -10**9
# min_result = 10**9

# def dfs(idx,ans):
#     global o,max_result,min_result
#     if idx == n:
#         max_result = max(max_result,ans)
#         min_result = min(min_result,ans)
    
#     if o[0] > 0:    # +
#         o[0] -= 1
#         dfs(idx+1,ans+a[idx])
#         o[0] += 1
#     if o[1] > 0:  # - 
#         o[1] -= 1
#         dfs(idx+1,ans-a[idx])
#         o[1] += 1 
#     if o[2] > 0:  # *
#         o[2] -= 1
#         dfs(idx+1,ans*a[idx])
#         o[2] += 1
#     if o[3] > 0:  # /
#         o[3] -= 1
#         if ans > 0:
#             dfs(idx+1,ans//a[idx])
#         else:
#             dfs(idx+1,(ans*-1)//a[idx]*-1)
#         o[3] += 1

# dfs(1,a[0])
# print("{}\n{}".format(max_result,min_result))

#14889번 스타트와 링크

# n = 4
# score = [[0,1,2,3],[4,0,5,6],[7,1,0,2],[3,4,5,0]]
# n = 6
# score = [[0,1,2,3,4,5],[1,0,2,3,4,5],[1,2,0,3,4,5],[1,2,3,0,4,5],[1,2,3,4,0,5],[1,2,3,4,5,0]]
# min_diff = 10000
# n = int(input())
# score = []
# for _ in range(n):
#     score.append(list(map(int,input().split())))
# team_start = []
# team_link = [x for x in range(n)]
# def dfs(cnt):
#     global min_diff
#     if cnt == n//2:
#         score_start = 0
#         score_link = 0
#         for i in range(cnt):
#             for j in range(i+1,cnt):
#                 score_start += score[team_start[i]][team_start[j]] + score[team_start[j]][team_start[i]]
#                 score_link += score[team_link[i]][team_link[j]] + score[team_link[j]][team_link[i]]
#         min_diff = min(min_diff,abs(score_start-score_link))
#         print(team_start)
#         return
    
#     for i in range(n):
#         if i in team_link:
#             if cnt != 0:
#                 if team_start[cnt-1] > i:
#                     continue
#             team_start.append(i)
#             team_link.remove(i)
#             dfs(cnt+1)
#             team_start.remove(i)
#             team_link.append(i)

# dfs(0)
# print(min_diff)

#9184번 신나는 함수 실행

# w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
# for i in range(1,21):
#     for j in range(1,21):
#         for k in range(1,21):
#             if i<j and j<k:
#                 w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
#             else:
#                 w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]

# while True:   
#     a,b,c = map(int,input().split())
#     if a==-1 and b==-1 and c==-1:
#         break
#     if a<=0 or b<=0 or c<=0:
#         print('w({}, {}, {}) = {}'.format(a,b,c,1))
#     elif a>20 or b>20 or c>20:
#         print('w({}, {}, {}) = {}'.format(a,b,c,w[20][20][20]))
#     else:
#         print('w({}, {}, {}) = {}'.format(a,b,c,w[a][b][c]))

#1904번 01타일

# n = int(input())
# cnt = [0 for _ in range(n)]
# for i in range(n):
#     if i==0:
#         cnt[i] = 1
#     elif i==1:
#         cnt[i] = 2
#     else:
#         cnt[i] = (cnt[i-2] + cnt[i-1]) % 15746
# print(cnt[n-1])

#9461번 파도반 수열
    
# padovan = [1,1,1,2,2]+[0]*95
# for i in range(5,100):
#     padovan[i] = padovan[i-1]+padovan[i-5]

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(padovan[n-1])

#1912번 연속합

# n = 10
# nums = [10,-4,3,1,5,6,-35,12,21,-1]
# nums = [2 ,1, -4 ,3 ,4, -4 ,6 ,5, -5 ,1]
        # 3   -1 2   6 2   8  13  8  9  
# n = 5
# nums = [-10,50,100,100,100]
# n = int(input())
# nums = list(map(int,input().split()))
# ps = [0]*n
# ps[0] = nums[0]
# for i in range(1,n):
#     ps[i] = max(ps[i-1] + nums[i],nums[i])
# print(max(ps))

#1149번 RGB거리

# n = int(input())
# data_rgb=[]
# for _ in range(n):
#     data_rgb.append(list(map(int,input().split())))

# price = [[0 for _ in range(3)] for _ in range(n+1)]

# for i in range(1,n+1):
#     price[i][0] = min(price[i-1][1],price[i-1][2]) + data_rgb[i-1][0]
#     price[i][1] = min(price[i-1][2],price[i-1][0]) + data_rgb[i-1][1]
#     price[i][2] = min(price[i-1][0],price[i-1][1]) + data_rgb[i-1][2]

# print(min(price[n][0],price[n][1],price[n][2]))

#1932번 정수 삼각형

# n = 5
# triangle = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
# n = int(input())
# triangle = []
# for _ in range(n):
#     triangle.append(list(map(int,input().split())))
# result = [[0 for _ in range(i+2)] for i in range(n)]
# result[0][0] = triangle[0][0]
# for i in range(1,n):
#     for j in range(i+1):
#         result[i][j] = max(result[i-1][j-1] , result[i-1][j]) + triangle[i][j]
# print(max(result[n-1]))

#2579번 계단 오르기

# n = 6
# score_floor = [10,20,15,25,10,20]
# n = int(input())
# score_floor = []
# for _ in range(n):
#     score_floor.append(int(input()))
# if n==1:
#     print(score_floor[0])
# elif n==2:
#     print(score_floor[0]+score_floor[1])
# else:
#     dp = [0]*n          
#     dp[0] = score_floor[0]
#     dp[1] = score_floor[0]+score_floor[1]
#     dp[2] = max(score_floor[0]+score_floor[2] , score_floor[1]+score_floor[2])
#     for i in range(3,n):
#         dp[i] = max(dp[i-2]+score_floor[i],dp[i-3]+score_floor[i-1]+score_floor[i])
#     print(dp[n-1])

#1463번 1로 만들기

n = 10
