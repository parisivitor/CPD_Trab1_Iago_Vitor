import xmlrpc.client


def start_cliente():
    with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
        vetor = [1, 2, 3, 4, 5]
        print("A somatoria do vetor é: %s" % str(proxy.is_even(vetor)))
        vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("A somatoria do vetor é: %s" % str(proxy.is_even(vetor)))
