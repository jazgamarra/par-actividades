import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9877

def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            message = input("Ingrese un mensaje para enviar al servidor: ")
            client_socket.sendto(message.encode(), (SERVER_ADDRESS, SERVER_PORT))
            response, _ = client_socket.recvfrom(1024)
            print(f"Respuesta del servidor: {response.decode()}")