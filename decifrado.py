from funciones import *
import hashlib
# Define la funcion para descifrar un mensaje
def algoritmo_descifrado(mensaje):
    # Aplica un cifrado ROT-22 al mensaje
    Mensajecodificado = rot_descifrado(mensaje,15)#Descifra el mensaje ROT15(se hace al contrario de como se cifro)
    mensaje_vigenere = vigenere(Mensajecodificado,'odiohacervideos','descifrado')# Descifra el mensaje Vigenere con la clave 'odiohacervideos'
    mensaje_vigenere2 = vigenere(mensaje_vigenere,'pamdatata','descifrado')# Descifra el mensaje Vigenere con la clave 'pamdatata'
    descifrado_completo = rot_descifrado(mensaje_vigenere2,22)#Descifra el mensaje ROT22
    print('Mensaje decrifrado')
    return descifrado_completo

if __name__ == '__main__':
    archivo = open("mensajeseguro.txt",'r')
    archivo_leido = archivo.readlines()
    archivo.close()
    mensaje = archivo_leido[0].replace('\n',"")#Lee el mensaje cifrado desde el archivo 
    hash_cifrado = archivo_leido[1] #Lee el hash cifrado desde el archivo
    
    MensajeCodificado = algoritmo_descifrado(mensaje) #Llama a la funcion para descifrar
    print('El mensaje decifrado es:', MensajeCodificado)
    ##detectar si el mensaje ha sido modificado o no
    hash_decifrado = hashlib.md5(MensajeCodificado.encode('utf-8')).hexdigest()#Calcula el hash del mensaje descifrado
    # Compara el hash cifrado y el hash calculado del mensaje descifrado
    if hash_cifrado == hash_decifrado: 
        print('Mensaje no modificado')
    else: 
        print('Mensaje modificado')

print('')
print('')
print('')
####################################################### comprobacion de modificacion
mensaje_modificado = MensajeCodificado[:2] + 'jiji' + MensajeCodificado[3:]
# Calcula el hash del mensaje adulterado
hash_modificado = hashlib.md5(mensaje_modificado.encode('utf-8')).hexdigest()
print('Mensaje adulterado:', mensaje_modificado)
# Compara el hash cifrado y el hash calculado del mensaje adulterado
if hash_cifrado == hash_modificado:
    print('Mensaje no modificado')
else:
    print('Mensaje modificado')