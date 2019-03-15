import socket

PORT = 8085
IP = "10.108.33.49"
MAX_OPEN_REQUESTS = 5

# RMB is the China currency: Renminbi is the currency, Yuan is the unit



def process_client(clientsocket):
    #adress[0]=direcciión IP del cliente
    #add=int(add)
    import random
    numero=random.randint(0,99)
    # utf8 supports all lanaguages chars
    #send_message = 'HEY'
    # Serializing the data to be transmitted
    #send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    #clientsocket.send(send_bytes)
    condition = True
    while condition:
        numero_recibido = int(clientsocket.recv(2048).decode("utf-8"))
        if numero_recibido == numero:
            send_message = 'Felicidades'
            condition = False
            send_bytes = str.encode(send_message)
            clientsocket.send(send_bytes)
            clientsocket.close()
        elif (numero-10) < numero_recibido < (numero + 10):
            send_message = 'Caliente caliente'
        elif (numero-10) > numero_recibido:
            send_message = 'Frio frio por abajo'
        elif (numero +10) < numero_recibido:
            send_message='Frio frio por arriba'


        send_bytes = str.encode(send_message)
        clientsocket.send(send_bytes)



# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
