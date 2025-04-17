t = int(input())
for t in range(t):
    words = input().split()
    modernName = ''.join(word[0] for word in words)
    print(modernName)
