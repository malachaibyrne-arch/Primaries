# Start of program ---

## Libraries and module installs
import socket
from cryptography.fernet import Fernet


#Spacing and syntax --
TAB1 = '\n'
TAB2 = '\n\n'
TAB3 = '\n\n\n'
Tab4 = '\n\n\n\n'


def main():
    # Either Load or generate the cryptographic key
    try:
        with open("secret.key", "rb") as Key_File:
            key = Key_File.read()
            print("Checking for existing key... ")
            print("\nKey Found: ")


    except FileNotFoundError:
        print(f"{TAB1} Checking for existing key... ")
        print("Key Not Found: ")
        print("\nGenerating...")
        
        key = Fernet.generate_key()
        with open("secret.key", "wb") as Key_File:
            Key_File.write(key)

    
    Scramble = Fernet(key)

    # Client-Side Config
    host = input(f'{TAB3} Host Address --> ')
    port = int(input("Port -->"))
    print("\nInitialising Server Configurations... ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"{TAB2}Connecting to server...")
    client_socket.connect((host, port))
    print("Connected! Message - or ('exit' to quit): ")

    # Bi-directional Comm-loop -
    while True:
        # Message to server
        message = input("\nClient [Send.] -> ")
        if message.lower() == 'exit':
            break
        
        encrypted_message = Scramble.encrypt(message.encode('utf-8'))
        client_socket.sendall(encrypted_message)

        # Receive encrypted response from server
        encrypted_data = client_socket.recv(1024)
        if not encrypted_data:
            break
        
        decrypted_message = Scramble.decrypt(encrypted_data).decode('utf-8')
        print(f"\nServer [Recv.] -> {decrypted_message}")

    client_socket.close()

if __name__ == '__main__':
    main()

# End of program ---