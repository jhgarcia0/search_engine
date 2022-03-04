""" def cosdis(a='',b=''):
    from math import sqrt
    letters_a = []
    letters_b = []
    letters_ab = []
    dict_a = []
    dict_b = []
    
    count = sqrt1 = sqrt2 = numerator = 0 

    #string to list
    letters_a = list(a)
    letters_b = list(b)

    #seeking for common letters between a and b 
    common = set(a).intersection(set(b))

    #set to list
    common = list(common)

    #counting amount of each unique letter in common
    for letter in letters_a:
        if letter in common:
            dict_a.append((letter,letters_a.count(letter)))
    for letter in letters_b:
        if letter in common:
            dict_b.append((letter,letters_b.count(letter)))
    letters_ab = list(set(a+b))

    #list to dictionary
    dict_a = dict(dict_a)
    dict_b = dict(dict_b)

    #getting the numerator
    for c in common:
        numerator += dict_a[common[count]]*dict_b[common[count]]
        count += 1

    #getting the denominator
    for l in letters_ab:
        sqrt1 += letters_a.count(l)**2
        sqrt2 += letters_b.count(l)**2
    denominator = sqrt(sqrt1) * sqrt(sqrt2)
    return numerator/denominator """

def cosdis(a,b):
    from math import sqrt
    letters_a = []
    letters_b = []
    letters_ab = []
    dict_a = []
    dict_b = []
    dis = 0 
    letters_a = list(a)
    letters_b = list(b)

    letters_ab = letters_a + letters_b
    letters_ab = set(letters_ab)
    letters_ab = list(letters_ab)

    for l in letters_ab:
        dis += (letters_a.count(l) - letters_b.count(l))**2
    try:
        dis = 1/sqrt(dis)
    except ZeroDivisionError:
        if a == b:
            return 1.0
    return dis

    print(letters_ab)
if __name__ == '__main__':
    print(cosdis('liquidificador','liquidificador'))