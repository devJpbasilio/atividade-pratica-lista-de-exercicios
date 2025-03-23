

# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma determinada empresa X que vende em atacado. 
# Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, conforme a listagem abaixo:

#     • Se valor for menor que 2500 o desconto será de 0%;
#     • Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
#     • Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
#     • Se valor for igual ou maior que 10000 o desconto será de 11%;



print('Bem-vindo a loja do João Silva') # Mensagem de boas-vindas

# Entrada do valor do produto
valor_produto = float(input('Entre com o valor do produto: ')) 

# Entrada da quantidade do produto
quantidade_produto = int(input('Entre com a quantidade do produto: ')) 

# Variável recebe o valor total dos produtos
valor_total_produtos = valor_produto * quantidade_produto

print(f'o valor SEM desconto: R${valor_total_produtos:.2f}') 

# Descontos
desconto_4 = 0.04   # 4%
desconto_7 = 0.07   # 7%
desconto_11 = 0.11  # 11%

# Calculando e exibindo o valor com desconto
if 2500 <= valor_total_produtos < 6000:
    valor_com_desconto_4 = valor_total_produtos * (1 - desconto_4)
    print(f'O valor COM desconto: R${valor_com_desconto_4:.2f}')
elif 6000 <= valor_total_produtos < 10000:
    valor_com_desconto_7 = valor_total_produtos * (1 - desconto_7)
    print(f'O valor COM desconto: R${valor_com_desconto_7:.2f}')
elif valor_total_produtos >= 10000:
    valor_com_desconto_11 = valor_total_produtos * (1 - desconto_11)
    print(f'O valor COM desconto: R${valor_com_desconto_11:.2f}')
else:
    print('Desconto não aplicado!') 