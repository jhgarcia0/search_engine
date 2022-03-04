from cosdis import cosdis
from time import time
try: 
    meant = ""
    aprox_num = 0
    ini = time()
    user_input=str(input('Digite uma palavra: '))
    first_letter = user_input[0]
    #abre o arquivo que começa com a primeira letra (tentantiva de otimização)
    try:
        with open("projeto-searchengine\\letters\\" + first_letter + ".txt",'r',encoding = 'utf-8') as pv:
            data = pv.readlines()
    except:
    #caso o usuário erre a primeira letra
        with open("projeto-searchengine\letters\palavras.txt",'r',encoding = 'utf-8') as pv:
            data = pv.readlines()
    #comparação do input com cada palavra no arquivo
    if not any(word.startswith(user_input) for word in data):
        for c in data:
            dis = 100*cosdis(user_input,c)
            if dis > 0.95:
                if dis > aprox_num:
                    aprox_num = dis
                    meant = c
        if meant != '':            
            print("Você quis dizer:",meant)
        else: 
            print("Não achamos um resultado para sua pesquisa.")
    else:
        print('Essa palavra existe no dicionário!')
    fim = time()
    """
    #Tempo de execução
    print(fim-ini)
    """
    
except Exception as error: 
    print(error)