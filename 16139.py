#인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
az = [[0]*26 for _ in range(len(s)+1)]  #s[i]까지의 알파벳 개수 카운팅
az[0][ord(s[0])-97] += 1
for i in range(1,len(s)):
    az[i] = az[i-1][:]
    az[i][ord(s[i])-97] += 1   
for _ in range(n):
    a,l,r = map(str,input().split())
    print(az[int(r)][ord(a)-97]-az[int(l)-1][ord(a)-97])