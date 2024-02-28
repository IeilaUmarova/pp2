import re
def spaces(txt):
    v = ""
    a = re.compile(r"[A-Z][a-z]+")
    word = a.findall(txt)
    for i, words in enumerate(word):
        if i != 0:
            v += " " + words
        else:
            v += words
    return v