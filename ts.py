def expand_text(sl):
    if type(sl) != str:
        return "type Error"
    else:
        list = sl.split()
        text = ""
        for word in list:
            sl = {}
            for i in range(len(word)):
                if word[i].isalpha() == False:
                    sl[i] = word[i]
            word = [c for c in word if c.isalpha()]
            word = word[::-1]
            for i,j in sl.items():
                word.insert(i,j)
            text += "".join(word)+" "
        text = text[:-1]
        return(text)

if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', '')
    ]
    for text, reversed_text in cases:
        assert expand_text(text) == reversed_text