texto = input("Digite a mensagem: ")
chave = input("Digite a chave: ").lower()
texto_resultado = ""
tamanho_chave = len(chave)
chave_i = 0


for i in range(len(texto)):
    char = texto[i]
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        
        chave_char = chave[chave_i % tamanho_chave]
        chave_valor = ord(chave_char) - ord('a')

        #Criptografia
        if 'A' <= char <= 'Z':
            valor = (ord(char) - ord('A') + chave_valor) % 26
            texto_resultado += chr(valor + ord('A'))
        elif 'a' <= char <= 'z':
            valor = (ord(char) - ord('a') + chave_valor) % 26
            texto_resultado += chr(valor + ord('a'))        
        chave_i += 1
    else:
        # Pula os caracteres de espaço e icones
        texto_resultado += char

#Rainiciar e printar texto criptografado
print(texto_resultado)
texto = texto_resultado
texto_resultado = ""
chave_i = 0

    #Descriptografia
for i in range(len(texto)):     
    char = texto[i]
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':   

        chave_char = chave[chave_i % tamanho_chave]
        chave_valor = ord(chave_char) - ord('a')
        
        if 'A' <= char <= 'Z':
            valor = (ord(char) - ord('A') - chave_valor + 26) % 26
            texto_resultado += chr(valor + ord('A'))
        elif 'a' <= char <= 'z':
            valor = (ord(char) - ord('a') - chave_valor + 26) % 26
            texto_resultado += chr(valor + ord('a'))
        chave_i += 1
    else:
        # Pula os caracteres de espaço e icones
        texto_resultado += char
#printar a mensagem descriptografada
print(texto_resultado)