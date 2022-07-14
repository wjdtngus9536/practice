word = 'banana'
def swapCase(word):
    for c in word:
        if 96 < ord(c) < 123:
            print(chr(ord(c)-32), end='')
swapCase(word)