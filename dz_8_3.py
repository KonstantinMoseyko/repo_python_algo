
def reversePrefix(word: str, ch: str) -> str:

    if ch in word:

        l= -1
        s = word[:(word.index(ch)+1)]
        s2 = word[(word.index(ch))+1:]
        s3= []
        while abs(len(s)+1) != abs(l):
            s3.append(s[l])
            l-=1
        s3 = ''.join(s3)+s2

        return (s3)
print(reversePrefix("abcdefd",'d'))
