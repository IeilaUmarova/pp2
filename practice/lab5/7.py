import re
def s_to_c(txt):
    ccase = ""
    v = re.compile(r"[_]")
    word = v.split(txt)
    for i, word in enumerate(word):
        if i != 0:
            ccase += word.capitalize()
    else:
        ccase += word
    return ccase