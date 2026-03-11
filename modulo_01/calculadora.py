''' 
Aqui vamos criar uma calculadora simples que pode realizar operações básicas 
como adição, subtração, multiplicação e divisão.

'''

print("\n=== Calculadora ===")

# Inicia o laço de repetição infinito para a calculadora continuar rodando
while True:
    
    try:

         print('\n=== Nova Operação ===')
         print('Escolha a operação: ')
         print('1 -> + | 2 -> - | 3 -> * | 4 -> / | 0 -> Sair')

         opcao= int(input('Sua escolha: '))
        
        # Condição para encerrar o programa
         if opcao == 0:
             print('Encerrando a calculadora. Até mais!')
             break
         
         # Verificar se a opção digitada está  dentro do intervalo de 1 a 4
         if opcao < 1 or opcao > 4:
             print('Opção inválida! Tente novamente.')
             continue
         
        # Recebe os números para o cálculo e converte para float, permitindo números decimais
         n1= float(input('Digite um valor: '))
         n2= float(input('Digite outro valor: '))
 
         if opcao == 1:
             print(f'O resultado da soma é: {n1 + n2}')

         elif opcao == 2:
             print(f'O resultado da subtração é: {n1 - n2}')
         
         elif opcao == 3:
             print(f'O resultado da multiplicação é: {n1 * n2}')
         
         elif opcao == 4:
             if n2 != 0:
              print(f'O resultado da divisão é: {n1 / n2}')
             else:
              print('Erro: Divisão por zero não é permitida.')

    # Captura erros de digitação (ex: quando o usuário digita uma letra em vez de um número)
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido.')    