# 5211 가단조와 다장조

note = list(map(str,input().split('|')))
note_major = ['C','F','G']
note_minor = ['A','D','E']
cnt_major = 0
cnt_minor = 0
for x in note:
    if x[0] in note_major:
        cnt_major += 1
    elif x[0] in note_minor:
        cnt_minor += 1

if cnt_major == cnt_minor:
    if note[-1][-1] in note_major:
        print('C-major')
    else:
        print('A-minor')
elif cnt_major > cnt_minor:
    print('C-major')
else:
    print('A-minor')