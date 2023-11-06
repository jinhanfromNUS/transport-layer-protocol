import socket
import sys

def client(port, host="127.0.0.1"):
    full_address = (host, port)
    client_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Client has successfully connected to {host}:{port} using UDP protocol!")

    print("You can start to communicate now!")
    print("Please note that if the server is not ready, it will not receive your message.")

    while True:
        message = input("")
        appended_message = "Client: " + message
        encoded_message = appended_message.encode("utf-8")
        client_udp_socket.sendto(encoded_message, full_address)
        if message == "Exit":
            break

        # received_message, sender_addr = client_udp_socket.recvfrom(1024)
        # decoded_received_message = received_message.decode("utf-8")
        # print(f"{decoded_received_message}")

    print("Connection ended!")
    client_udp_socket.close()

if __name__ == "__main__":
    # format: python client.py [host] [port]
    # format: python client.py [port]

    if len(sys.argv) == 2:
        port_number = int(sys.argv[1])
        client(port_number)
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port_number = int(sys.argv[2])
        client(port_number, host)
