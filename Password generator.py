#Password generator by @m4rxhs_cyber
import random
resposta = 'S'

while resposta == 'S': 
    print("\n-------------------------------")
    print("\n------GERADOR DE SENHAS------")
    print("\n-------------------------------")

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "[]{~^}+§!@#$%¨&*().,/-_"
    numbers = "0123456789"

    juncao = lower + upper + symbols + numbers

    tamanho = int(input("\nQual a quantidade de caracteres você deseja?(LIMITE 85 CARACTÉRES): ")) 

    senha = "".join(random.sample(juncao, tamanho))

    print("\n-------------------------------")
    print("\nA senha gerada é : ", senha)
    print("\n-------------------------------")

resposta = str(input("\nRun again? [S/N] "))
