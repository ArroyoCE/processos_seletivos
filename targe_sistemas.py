import xml.etree.ElementTree as ET








# Questão 01
indice = 13
k = 0
soma = 0
while k < 13:
    k += 1
    soma += k
print(f"O valor que será imprimido na tela é o {soma}")




# Questão 02
n = int(input("\n\nEscreva o número que deseja verificar se faz parte da sequência Fibonacci: "))
k = 0
fibonacci = [0, 1]

for k in range (1, 120):
    if n == 0 or n == 1:
        print("O número faz parte da sequência Fibonacci.")
        break
    soma = fibonacci[k-1] + fibonacci[k]
    fibonacci.append(soma)
    if n in fibonacci:
        print(f"O número faz parte da sequência Fibonacci. É o número de posição {k+2} na sequência.")
        break

if n not in fibonacci:
    print("O número não faz parte da sequência Fibonacci.")








#Questão 03
import xml.etree.ElementTree as ET


file_path = 'dados.xml'


with open(file_path, 'r') as file:
    xml_content = file.read()


if not xml_content.strip().startswith('<root>'):
    xml_content = f'<root>{xml_content}</root>'


root = ET.fromstring(xml_content)


data = []
for row in root.findall('row'):
    day = int(row.find('dia').text)
    value = float(row.find('valor').text)
    data.append({'dia': day, 'valor': value})
menor = 0
dia = 0
# Print the extracted data
for item in data:
    if menor == 0 and item['valor'] != 0:
        menor = item['valor']
        dia = item['dia']
    if item['valor'] != 0 and menor != 0:
        if menor > item['valor']:
            menor = item['valor']
            dia = item['dia']
print(f"\n\nO menor faturamento foi no dia {dia}, no valor de R$ {menor:.2f}.")
for item in data:
    if menor == 0 and item['valor'] != 0:
        menor = item['valor']
        dia = item['dia']
    if item['valor'] != 0 and menor != 0:
        if menor < item['valor']:
            menor = item['valor']
            dia = item['dia']
print(f"\nO maior faturamento foi no dia {dia}, no valor de R$ {menor:.2f}.")
total = 0
dias_uteis = 0
for item in data:
    if item['valor'] != 0:
        total += item['valor']
        dias_uteis += 1

media = total/dias_uteis

print("\nDias em que o faturamento foi maior do que a média:")
for item in data:
    if item['valor'] > media:
        print(f"Dia {item['dia']}: R$ {item['valor']:.2f}")



#Questão 04
total = 0
faturamentos = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
for valor in faturamentos.values():
    total += valor

for estado, valor in faturamentos.items():
    print(f"\n\n\nO Estado {estado} representa {(valor/total)*100:.2f}% do total.")



#Questão 05
string_invertida = ""
string = input("\n\n\nInforme a string que deseja inverter: ")
tamanho = len(string)
for i in range(tamanho-1, -1, -1):
    string_invertida += string[i]
print(f"\nA string invertida fica: {string_invertida}")
