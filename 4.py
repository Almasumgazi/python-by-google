from operator import itemgetter 


def initials(phrase):
    words = phrase.upper()
    words__list=words.split()
    return "".join(list(map(itemgetter(0), words__list)))
 	

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS