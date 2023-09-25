from funciones import * # Importa todas las funciones definidas en el archivo 'funciones'
import hashlib

def algoritmo_cifrado(mensaje):
    mensaje = mensaje.replace(' ', '').lower()	# Se guarda el mensaje en miniscula y sin espacios
    mensaje = rot_cifrado(mensaje,22)# Aplica un cifrado ROT-22 al mensaje
    mensaje_vigenere = vigenere(mensaje,'pamdatata','cifrado')# Aplica un cifrado Vigenere con la clave 'pamdatata'
    mensaje_vigenere2 = vigenere(mensaje_vigenere,'odiohacervideos','cifrado')# Aplica otro cifrado Vigenere con la clave 'odiohacervideos'
    cifrado_completo = rot_cifrado(mensaje_vigenere2,15)# Aplica un cifrado ROT-15 al mensaje
    print('Mensaje cifrado')
    return cifrado_completo

if __name__ == '__main__':
    file = open("mensajedeentrada.txt", "w+")#Abre un archivo del mensaje para introducirle el texto a cifrar
    mensaje = input('Escriba el mensaje a cifrar: ')
    file.write(mensaje)
    file.close()

    file = open("mensajedeentrada.txt", "r")#Abre un archivo del mensaje para cifrar
    mensajeDeEntrada = file.readline().replace(' ', '').lower()#Lee la primera linea y elimina espacios y convierte a minusculas
    hash = hashlib.md5(mensajeDeEntrada.encode('utf-8')).hexdigest() #Calcula el hash del mensaje
    file.close()
    #Abre otro archivo y escribe el mensaje cifrado y el hash en el archivo separados por una linea
    MensajeCodificado = algoritmo_cifrado(mensajeDeEntrada)
    file = open("mensajeseguro.txt", "w+")
    file.write(MensajeCodificado + '\n' + hash)
    file.close()

