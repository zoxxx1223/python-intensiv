"""
Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""
url = "www.web.de"
url[0:3]  # 3 ist exclusive
print("url[0:3]:", url[0:3]) # www
print("url[:3]:", url[:3]) # www
print("url[3:]:", url[3:]) # .web.de
print("url[:-1]:", url[:-1]) # www.web.d
"""
# Übung
# Schneide jeweils alle A aus den Strings
AAAAB => AAAA
BBAAABBB => AAA
AAAABBBB => AAAA
ABBBBB => A
"""
string = "AAAAB"
print("AAAAB => AAAA: ", string[:-1])

string = "BBAAABBB"
print("BBAAABBB => AAA: ", string[2:5])

string = "AAAABBBB"
print("AAAABBBB => AAAA: ", string[:-4])

string = "ABBBBB"
print("ABBBBB => A: ", string[:1])

# Schrittweite
string = "123456789"
print(string[::2])
print(string[1::2])

# String umdrehen
city = "Hamburg"
print(city[::-1])