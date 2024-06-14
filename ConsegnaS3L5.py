
#il programma deve inviare pachetti di 1 KB casuali

import random
import socket


def crea_il_pacchetto():
    return random.randbytes(1024) #questa funzione crea il pacchetto da 1024 byte

ip_target = input ("Scrivi l'IP target: ") #scegli l'ip target, fatto
porta_target = int (input ("Scrivi la porta target: ")) #scegli la porta target, fatto
numero_pacchetti = int (input ("Inserisci il numero di pacchetti da inviare: ")) #scegli quanti pacchetti inviare, fatto

sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM) #socket UDP

for i in range (numero_pacchetti):   #funzione per inviare i pacchetti
    pacchetto = crea_il_pacchetto ()
    sock.sendto (pacchetto, (ip_target, porta_target))

    print (f'Pacchetto {i+1} inviato a {ip_target}:{porta_target}')


print ("Invio dei pacchetti completato.") #mostrare che il programma ha finito di inviare i pacchetti