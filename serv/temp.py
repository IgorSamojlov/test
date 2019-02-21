def aaa(num):
    return (num[0])


a = {'SDFd': ['sdfsdfd', 'fsdf'], 'sss': ['smkjs', 's.kxk']}
d = list(a.values())
print(d[0])

b=list(map(aaa, d))

print((b))

a = set(['aaa'])
print (a)

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
