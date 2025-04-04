# Maximum Submatrix Sum
# Gold 3, prefix sum, DP(kadane)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[0]*M]+[list(map(int,input().split())) for _ in range(N)]

result = 0
for j in range(M):
    for i in range(N):
        A[i+1][j] += A[i][j]
for t in range(1,N+1):
    for b in range(t,N+1):
        cursum = 0
        for j in range(M):
            x = A[b][j]-A[t-1][j]
            cursum = max(cursum+x,x)
            result = max(result,cursum)
print(result)

# pypy로 시간초과 나서 c++로 통과
# #include <iostream>
# #include <vector>
# #include <algorithm>

# using namespace std;

# int main() {
#     ios::sync_with_stdio(false);
#     cin.tie(0);

#     int N, M;
#     cin >> N >> M;

#     vector<vector<int>> A(N + 1, vector<int>(M, 0));

#     for (int i = 1; i <= N; ++i) {
#         for (int j = 0; j < M; ++j) {
#             cin >> A[i][j];
#         }
#     }

#     int result = 0;

#     for (int j = 0; j < M; ++j) {
#         for (int i = 1; i <= N; ++i) {
#             A[i][j] += A[i - 1][j];
#         }
#     }

#     for (int t = 1; t <= N; ++t) {
#         for (int b = t; b <= N; ++b) {
#             int cursum = 0;
#             for (int j = 0; j < M; ++j) {
#                 int x = A[b][j] - A[t - 1][j];
#                 cursum = max(cursum + x, x);
#                 result = max(result, cursum);
#             }
#         }
#     }

#     cout << result << "\n";
#     return 0;
# }
