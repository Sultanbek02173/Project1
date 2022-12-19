from homework4 import *
from colorama import *
init()

num = Num5('Bob', 11)
print(Fore.RED, Back.GREEN, Style.BRIGHT, num, Style.RESET_ALL)
num.prim1()
num.prim2()


print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')