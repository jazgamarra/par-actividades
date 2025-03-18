import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9876

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_ADDRESS, SERVER_PORT))
        while True:
            message = input("Ingrese un mensaje para enviar al servidor: ")
            sock.sendall(message.encode())
            response = sock.recv(1024).decode()
            print(f"Respuesta del servidor: {response}")

tcp_client()
