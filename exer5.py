def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

# String definida diretamente no código
string = "Exemplo de string"  # Você pode alterar essa string

print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}")
