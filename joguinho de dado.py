print("""\nBem vindo! Eis o desafio, tente descobrir entre 1 e 6, em qual número o dado vai cair!
ATENÇÃO! DIGITE APENAS NÚMEROS DE 1 a 6!""")

from random import randint
from time import sleep

dice = randint(1, 6)

user = int(input("\nFaça sua aposta: "))
print("(Jogando o dado...)")
sleep(2)

if user == dice:
    print(f"\nCORRETO! O dado caiu em {dice}.\n")

elif (user > 0) & (user <= 6) & (user != dice):
    print(f"\nERRADO! Você apostou no número {user} e o dado caiu em {dice}. Mais sorte na próxima!\n")

else:
    print("TECLA INVÁLIDA\n")
