def word_frequency(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def read_words(filename):
    return open(filename).read().split()


def main(filename):
    k=[]
    frequency = word_frequency(read_words(filename))
    for  count,words in sorted(frequency.items(),key=lambda x: x[1]):
         k.append((count,words))
    for words ,count in k[::-1]:
         print words,count
   
if __name__ == "__main__":
    import sys
    main(sys.argv[1])
