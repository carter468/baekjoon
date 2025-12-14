# 순열 뒤집기
# Platinum 4, ad hoc, stack

input()
st = []
for n in map(int,input().split()):
    st.append((n,n))
    while len(st) > 1:
        a,b = st.pop()
        c,d = st.pop()
        if b+1 == c:
            st.append((a,d))
        elif d+1 == a:
            st.append((c,b))
        else:
            st.append((c,d))
            st.append((a,b))
            break
print(['YES','NO'][len(st) > 1])