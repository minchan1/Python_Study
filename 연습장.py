def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        if ord(s[i])>=97:
            s[i] = chr((ord(s[i])-97+n)%26 + 97)
        elif ord(s[i])<97:
            s[i] = chr((ord(s[i])-65+n)%26 + 65)
    print(''.join(s))

a=' '
print(ord(a))
