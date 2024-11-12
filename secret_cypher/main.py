#Devin Longtree [Secret Cypher]

word = input("Input a word: ")
wordlist = list(word)


def shift():
    if "a" in word:
        wordlist.remove("a")
        wordlist.append("b")
    if "b" in word:
        wordlist.remove("b")
        wordlist.append("c")
    if "c" in word:
        wordlist.remove("c")
        wordlist.append("d")
    if "d" in word:
        wordlist.remove("d")
        wordlist.append("e")
    if "e" in word:
        wordlist.remove("e")
        wordlist.append("f")
    if "f" in word:
        wordlist.remove("f")
        wordlist.append("g")
    if "g" in word:
        wordlist.remove("g")
        wordlist.append("h")
    if "h" in word:
        wordlist.remove("h")
        wordlist.append("i")
    if "i" in word:
        wordlist.remove("i")
        wordlist.append("j")
    if "j" in word:
        wordlist.remove("j")
        wordlist.append("k")
    if "k" in word:
        wordlist.remove("k")
        wordlist.append("l")
    if "l" in word:
        wordlist.remove("l")
        wordlist.append("m")
    if "m" in word:
        wordlist.remove("m")
        wordlist.append("n")
    if "n" in word:
        wordlist.remove("n")
        wordlist.append("o")
    if "o" in word:
        wordlist.remove("o")
        wordlist.append("p")
    if "p" in word:
        wordlist.remove("p")
        wordlist.append("q")
    if "q" in word:
        wordlist.remove("q")
        wordlist.append("r")
    if "r" in word:
        wordlist.remove("r")
        wordlist.append("s")
    if "s" in word:
        wordlist.remove("s")
        wordlist.append("t")
    if "t" in word:
        wordlist.remove("t")
        wordlist.append("u")
    if "u" in word:
        wordlist.remove("u")
        wordlist.append("v")
    if "v" in word:
        wordlist.remove("v")
        wordlist.append("w")
    if "w" in word:
        wordlist.remove("w")
        wordlist.append("x")
    if "x" in word:
        wordlist.remove("x")
        wordlist.append("y")
    if "y" in word:
        wordlist.remove("y")
        wordlist.append("z")
    if "z" in word:
        wordlist.remove("z")
        wordlist.append("a")
print(word)
shift()
wordlist = ''.join(wordlist)
print(wordlist)