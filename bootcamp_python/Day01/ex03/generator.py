def shuffle(lst):
    ret = []
    i = 1
    for l in lst:
        ret.insert(i % len(lst), l)
        i += i
    return ret


def sort(lst):
    lst.sort()
    return lst


def unique(lst):
    ret = []
    for l in lst:
        if l not in ret:
            ret.append(l)
    return ret


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    ret = text.split(sep=sep)
    options = {
        "shuffle": shuffle,
        "ordered": sort,
        "unique": unique
    }
    if option:
        if option not in options:
            return 'ERROR'
        else:
            ret = options[option](ret)
    for word in ret:
        yield word


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="ordered"):
        print(word)