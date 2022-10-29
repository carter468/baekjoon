# 모노톤길

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # x좌표가 같은 카페를 모아둔다
    location_cafe = [[] for _ in range(100001)]
    for _ in range(int(input())):
        x,y = map(int,input().split())
        if x or y:  # 입구 제외
            location_cafe[x].append(y)

    # 경로 순서대로 저장        
    path_cafe = [[0,0]]
    for i in range(100001):
        # 같은 x좌표에 카페가 두개 이상있을때 정렬
        if len(location_cafe[i]) > 1:
            # 첫번째 카페가 y좌표가 같으면 길을 모르기 때문에 다음 카페와 비교
            if location_cafe[i][0] == path_cafe[-1][1]:
                # 위에있으면 오름차순정렬
                if location_cafe[i][1] > path_cafe[-1][1]:
                    location_cafe[i].sort()
                # 아래있으면 내림차순정렬
                else:
                    location_cafe[i].sort(reverse=True)
            elif location_cafe[i][0] > path_cafe[-1][1]:
                location_cafe[i].sort()
            else:
                location_cafe[i].sort(reverse=True)
        
        for j in location_cafe[i]:
            path_cafe.append([i,j])

    query = list(map(int,input().split()))
    for i in range(query[0]):
        print(*path_cafe[query[i+1]-1])