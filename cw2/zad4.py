#zwraca string ze znakami o parzystym numerze indeksu w podanym stringu;

def zad4(string):
        srtWyjsciowy = ""
        for i in range(1,len(string)):
            if i % 2 == 0:
                srtWyjsciowy += string[i]
        return srtWyjsciowy
#zwraca n (podano, domy±lne 1) ostatnich znaki w podanym stringu
def zad5(string,n):
    srtWyjsciowy = ""
    for i in range(1,n+1):
        srtWyjsciowy += string[-i]
    return srtWyjsciowy

#pobiera string i zwraca string, powstaªy z odwrócenia kolejno±ci znaków
def zad6(string):
    srtWyjsciowy = ""
    for i in range(1,len(string)+1):
        srtWyjsciowy += string[-i]
    return srtWyjsciowy
#pobiera 2 stringa i zwraca, które jest dªu»szy (1 czy 2)
def zad7(string1,string2):
    if len(string1) > len(string2):
        return "pierwszy"
    elif len(string1) == len(string2):
        return "rowne"
    else: return "drugi"
#Napisz program (program23.py), który na wej±ciu dostaje napis
#postaci W Roku Pa«skim 1345, wªadca Henryk 12, na rzecz swoich 143209 poddanych uchwaliª dekret o 20 procentowej zni»ce podatków. Twoim zadaniem jest
#wyªuska¢ wszystkie liczby (niech b¦d¡ tylko caªkowite) i wy±wietli¢ ich sum¦
def zad8(text):
    listaliczb = []
    count = [0,0]
    suma = 0
    flag = False
    j = 0
    for i in text:
        j+=1
        if i.isdigit() == True and flag == False :
            count[0] = j-1
            flag = True
        if (i.isdigit() == False) and (flag == True):
            count[1] = j-1
            flag = False
            listaliczb.append(text[count[0]:count[1]])
    for i in listaliczb:
        suma += int(i)

    return listaliczb,suma

print(zad8("W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków.")[0])
print(zad8("W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków.")[1])

print(zad4("qwertyuiop"))
print(zad5("qwertyuiop",4))
print(zad6("qwertyuiop"))
print(zad7("qwertyuiop","qwerty"))
