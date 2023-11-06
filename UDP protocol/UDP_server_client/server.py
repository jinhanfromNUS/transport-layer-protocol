import socket
import sys

def server(port, host="127.0.0.1"):
    full_address = (host, port)
    server_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_udp_socket.bind(full_address)  # Bind the socket to the server's address

    print(f"Server is listening on {host}:{port} using UDP protocol!")

    while True:
        try:
            received_message, sender_addr = server_udp_socket.recvfrom(1024)
            decoded_received_message = received_message.decode("utf-8")
            print(f"Received from {sender_addr[0]}:{sender_addr[1]}: {decoded_received_message}")
            if decoded_received_message == "Client: Exit":
                break
        except ConnectionResetError:
            print("Client forcibly closed the connection.")
        except KeyboardInterrupt:
            break

    server_udp_socket.close()
    print("Connection ended!")

if __name__ == "__main__":
    # format: python server.py [host] [port]
    # format: python server.py [port]

    if len(sys.argv) == 2:
        port_number = int(sys.argv[1])
        server(port_number)
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port_number = int(sys.argv[2])
        server(port_number, host)
