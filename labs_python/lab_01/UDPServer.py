import socket

SERVER_PORT = 9877

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('localhost', SERVER_PORT))
        print(f"Servidor UDP escuchando en el puerto {SERVER_PORT}...")
        while True:
            message, client_address = server_socket.recvfrom(1024)
            response = f"Respuesta del servidor: {message.decode().upper()}"
            server_socket.sendto(response.encode(), client_address)

