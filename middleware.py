from servidor import start_servidor
from cliente import start_cliente
from multiprocessing import Process


def inicia_servidor():
    start_servidor()


def inicia_cliente():
    start_cliente()


def paralelismo(*funcoes):
    proc = []
    for funcao in funcoes:
        processo = Process(target=funcao)
        processo.start()
        proc.append(processo)
    for processo in proc:
        processo.join()


if __name__ == '__main__':
    paralelismo(inicia_servidor, inicia_cliente)
