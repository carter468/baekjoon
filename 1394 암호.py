# 암호
# Gold 5, 조합론, 해시

M = 900528

key_list = input()
password = input()

len_pw = len(password)
key_dict = {}
for i,k in enumerate(key_list):
    key_dict[k] = i

p = [1]
for _ in range(1,len_pw):
    p.append(p[-1]*len(key_list)%M)
    
result = sum(p)
for idx,c in enumerate(password):
    result += key_dict[c]*p[len_pw-idx-1]

print(result%M)