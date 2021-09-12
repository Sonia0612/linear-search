
def search(li,s):
    for i in range(len(li)):
        if li[i]==s:
            return i
    return -1
li=[int(x) for x in input().split()]
print(li)
s=int(input())
h=search(li,s)
print(h)