#port-scanner // main.py
import socket

def receber_ip():
    ip = input("Digite o IP alvo: ")
    return(ip)
   
def receber_porta_inicial():

    while True:
        try:
            initial_port = int(input("Digite a porta inicial (1 à 65535): "))

            if 1 <= initial_port <= 65535:
                return initial_port
            else:
                print("The number needs to be between 1 and 65535")

        except ValueError:
            print("error: type only integer numbers")


def receber_porta_final(initial_p):
    while True:
        try:
            final_port = int(input(f"Digite a porta final ({initial_p+1} à 65535): "))

            if initial_p <= final_port <= 65535:
                return final_port
            else:
                print(f"The number needs to be between {initial_p+1} and 65535")

        except ValueError:
            print("error: type only integer numbers")

             
def scanner(ip_alvo, initial_p, final_p):
    print(f"Escaneando o IP: {ip_alvo}")

    portas_abertas = []

    for porta in range(initial_p, final_p+1):
        socket_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_temp.settimeout(0.5)
        resultado = socket_temp.connect_ex((ip_alvo,porta))

        print(f"Trying to connect to port {porta}...")

        if resultado == 0:
            portas_abertas.append(porta)
            print(f"[+] Port {porta} OPEN!") 
        
        else:
            print(f"[-] Port {porta} CLOSED (code {resultado})\n")

        socket_temp.close()


    print(f"\n--- SCAN COMPLET ---")
    print(f"Ports found open: {portas_abertas}")

if __name__ == "__main__":
    ip_alvo = receber_ip()
    initial_p = receber_porta_inicial()
    final_p = receber_porta_final(initial_p)
    scanner(ip_alvo, initial_p, final_p)
