#인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

s = input().strip()
# n = int(input())
az = [[0]*26]  #s[i]까지의 알파벳 개수 카운팅
az[0][ord(s[0])-97] += 1
print(az)
az.append(az[0])
az[1][0] += 1
print(az)
# for i in range(1,len(s)):
#     az[i] = az[i-1]
#     az[i][ord(s[i])-97] += 1    
# print(az)
# for _ in range(n):
#     a,l,r = map(str,input().split())
#     print(az[int(r)][ord(a)-97]-az[int(l)-1][ord(a)-97])