

def escolha_servico():
    
    while True:
        
        print('\nEntre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>> ').lower()
        
        if servico == 'dig':
            return 1.10
        elif servico == 'ico':
            return 1.00
        elif servico == 'ipb':
            return 0.40
        elif servico == 'fot':
            return 0.20
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente!')

  
def num_pagina():
    
    while True:
        
        try:
            paginas = int(input('\nEntre com o número de páginas: '))
            
            if paginas >= 20000:
                print('Não é aceitamos tantas páginas de uma vez!')
            elif paginas >= 2000:
                return paginas * 0.75
            elif paginas >= 200:
                return paginas * 0.80
            elif paginas >= 20:
                return paginas * 0.85
            elif paginas > 0:
                return paginas
            else:
                print('Por favor, entre com o número de páginas novemente!')
        except ValueError:
            print('Valor inválido! Digite um valor inteiro.')

def servico_extra():
    
    while True:
        
        print('\nDeseja adicionar algum serviço?')
        print('1 - Encadernação Simple - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        adicional = input('>> ')
        
        if adicional == '1':
            return 15
        elif adicional == '2':
            return 40
        elif adicional == '0':
            return 0
        else:
            print('Opção inválida! Tente novamente.')
            
if __name__ == "__main__":

    print('\nBem-vindo a copiadora do João Silva')
    
    servico = escolha_servico()
    paginas_com_desconto = num_pagina()
    extra = servico_extra()
    
    total = (servico * paginas_com_desconto) + extra
    
    print(f'Total: R$ {total:.2f} (serviço: {servico:.2f} * páginas: {paginas_com_desconto:.2f} + extra: {extra:.2f})')