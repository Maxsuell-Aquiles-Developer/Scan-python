import socket #import the socket library

for port in range(1, 8080): #Loop
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = input('Put the ip here: ') #Interactive program
    resultado = s.connect_ex ((ip, port))
    print(format(ip))
    try:
        if resultado == 0 :
           print('OPEN: '.format(port))
        else:
            print('CLOSED: ', port)
    except Exception as erro:
        print('Erro: ', erro)




