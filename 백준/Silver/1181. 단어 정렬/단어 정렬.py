N = int(input())
words = set()

for _ in range(N):
    words.add(input())
    
sorted_words = sorted(words, key=lambda x: (len(x), x))

for ch in sorted_words:
    print(ch)