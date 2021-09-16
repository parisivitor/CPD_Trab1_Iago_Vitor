from xmlrpc.server import SimpleXMLRPCServer
from somatorio import Somatorio

def is_even(vetor):
    somatorio = Somatorio()
    return somatorio.realiza_soma(vetor)

def start_servidor():
    server = SimpleXMLRPCServer(("localhost", 8080))
    print("Ouvindo a porta 8080")
    server.register_function(is_even, "is_even")
    server.serve_forever()





