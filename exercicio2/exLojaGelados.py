
# Mensagem de boas-vindas
print('        Bem-vindo a loja de Gelados do João Silva!        ')

print('-------------------------Cardápio-------------------------')
print('----------------------------------------------------------')
print('---|  TAMANHO  |---|  CUPUAÇU (CP)  |---|  AÇAÍ (AC)  |---')
print('---|     P     |---|    R$  9.90    |---|  R$ 11.00   |---')
print('---|     M     |---|    R$ 14.00    |---|  R$ 16.00   |---')
print('---|     G     |---|    R$ 18.00    |---|  R$ 20.00   |---')
print('----------------------------------------------------------')

#Definindo o cardápio através de um dicionário
cardapio = {
    "cp": {"P": 9.00, "M": 14.00, "G": 18.00},
    "ac": {"P": 11.00, "M": 16.00, "G": 20.00}
}

#Lista para validar sabores e tamanhos permitidos
sabores_validos = ["cp", "ac"]
tamanhos_validos = ["P", "M", "G"]

#Variável acumuladora para somar os valores dos pedidios
pedido_total = 0

#Criando o loop principal para repetir o pedido
while True:
    
    #Entrada do sabor
    sabor = input('Entre com o sabor desejado (CP/AC): ').lower() #Converte entrada para minúscula
    if sabor not in sabores_validos:
        print('Sabor inválido. Tente novamente!') # Exibe mensagem de erro
        continue
    #Entrada do tamanho
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper() #Converte entrada para maiúscula
    if tamanho not in tamanhos_validos:
        print('Tamanho inválido. Tente novamente!') #Exibe mensagem de erro para o tamanho
        continue
    
    preco = cardapio[sabor][tamanho] #Acessa o preço correto com base no sabor e no tamanho
    
    if sabor == 'cp': #Se o sabor for Cupuaçu
        print(f'Voçe pediu um Cupuaçu no tamanho {tamanho}: R$ {preco:.2f}')
    else: #Caso contrário, o sabor é Açaí
        print(f'Você pediu um Açaí no tamanho {tamanho}: R$ {preco:.2f}')
        
    pedido_total += preco #Somando o preço do pedido ao acumulador
    
    #Perguta ao usuário se deseja mais alguma coisa
    mais_alguma_coisa = input('Deseja pedir mais alguma coisa? (S/N): ').lower()
    if mais_alguma_coisa == 'n':
        break

#Exibindo o valor total acumulado e finalizando o pedido
print(f'\nO valor total a ser pago: R$ {pedido_total:.2f}')