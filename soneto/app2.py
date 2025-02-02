from sys import exit
from traceback import print_exc
from core.soneto_core import processa_soneto
from decouple import config

def main():

    total_ocorrencias, \
        remove_duplicidade, \
        conta_palavras, \
        gera_lista_palavras = processa_soneto(config('ARQUIVO_POEMA'))

    palavras = total_ocorrencias(remove_duplicidade(
        conta_palavras(gera_lista_palavras())))

    for palavra in palavras:
        palavra_, total = palavra.split(':')

        if int(total) > 1:
            print(f"Palavra: {palavra_:13} = {total}")

if __name__ == "__main__":

    try:

        main()

        exit(0)

    except Exception:

        print_exc()

        exit(1)
