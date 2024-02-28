import re
def camel_to_snake(txt):
    v = ""
    a = re.compile(r"[A-Z][a-z]+")
    word = a.findall(txt)
    for i, words in enumerate(word):
        if i == 0:
            v += words.casefold()
        else:
            v += "_" + words.casefold()
    return v