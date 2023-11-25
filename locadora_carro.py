import os
import time

portifolio = [["Chevrolet Tracker", 120], 
              ["Chevrolet Onix", 90], 
              ["Chevrolet Spin", 150],
              ["Hyundai HB20", 85],
              ["Hyundai Tucson", 120],
              ["Fiat Uno", 60],
              ["Fiat Mobi", 70],
              ["Fiat Pulse", 130]]

alugados = []

selecao1 = 4

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========")
    print("Bem vindo à locadora de carros!")
    print("==========")
    print("O que deseja fazer?")
    print("1 - Mostrar portifólio | 2 - Alugar um carro | 3 - Devolver um carro | 0 - Sair da aplicação")
    try:
        selecao1 = int(input())
        while selecao1 not in [0, 1, 2, 3]:
            print('Erro: a opção selecionada é inválida')
            print("1 - Mostrar portifólio | 2 - Alugar um carro | 3 - Devolver um carro | 0 - Sair da aplicação")
            selecao1 = int(input())
            print('Erro: o caracter digitado deve ser um número')
        
        if selecao1 == 0:
            print("Muito obrigado e até a próxima!")
            time.sleep(3)
            break

        elif selecao1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')   
            for i in range(len(portifolio)):
                print("[{}] {} - R$ {} /dia".format(i, portifolio[i][0], portifolio[i][1]))
            print('')
            print("==========")
            print("1 - Continuar | 0 - Sair da aplicação")
            selecao2 = int(input())
            while selecao2 not in [0, 1]:
                print('Erro: a opção selecionada é inválida')
                print("1 - Continuar | 0 - Sair da aplicação")
                selecao2 = int(input())
            if selecao2 == 0:
                print("Muito obrigado e até a próxima!")
                time.sleep(3)
                break
                
        elif selecao1 == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ALUGAR] Dê uma olhada em nosso portifólio.')
            print('')
            for i in range(len(portifolio)):
                print("[{}] {} - R$ {} /dia".format(i, portifolio[i][0], portifolio[i][1]))
            print('')
            print("==========")
            print("Escolha o código do carro:")
            codigo_carro = int(input())
            while codigo_carro not in range(len(portifolio)):
                print('Erro: a opção selecionada é inválida')
                print("Escolha o código do carro:")
                codigo_carro = int(input())
            print("Escolha por quantos dias deseja alugar:")
            dias_aluguel = int(input())
            while dias_aluguel < 1:
                print('Erro: o tempo mínimo de aluguel é de 1 dia')
                print("Escolha por quantos dias deseja alugar:")
                dias_aluguel = int(input())
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Você escolheu {} por {} dias.".format(portifolio[codigo_carro][0], dias_aluguel))
            print("O aluguel totalizaria R$ {:.2f}. Deseja alugar?".format(portifolio[codigo_carro][1] * dias_aluguel))
            print('')
            print('1 - Sim | 0 - Não')
            confirmacao_aluguel = int(input())
            while confirmacao_aluguel not in [0, 1]:
                print('Erro: a opção selecionada é inválida')
                print('1 - Sim | 0 - Não')
                confirmacao_aluguel = int(input())
            if confirmacao_aluguel == 1:
                carro_alugado = portifolio.pop(codigo_carro)
                alugados.append(carro_alugado)
                print("Parabéns você alugou o {} por {} dias.".format(carro_alugado[0], dias_aluguel))
                print('')
                print("==========")
                print("1 - Continuar | 0 - Sair da aplicação")
                selecao2 = int(input())
                while selecao2 not in [0, 1]:
                    print('Erro: a opção selecionada é inválida')
                    print("1 - Continuar | 0 - Sair da aplicação")
                    selecao2 = int(input())
                if selecao2 == 0:
                    print("Muito obrigado e até a próxima!")
                    time.sleep(3)
                    break
                
        elif selecao1 == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            if len(alugados) == 0:
                print('Não há nenhum carro alugado para ser devolvido.')
                time.sleep(1)
                print('Você será redirecionado para o menu principal.')
                time.sleep(2)
            else:
                print("Segue lista de carros alugados. Qual você deseja devolver?")
                print('')
                for i in range(len(alugados)):
                    print("[{}] {} - R$ {} /dia".format(i, alugados[i][0], alugados[i][1]))
                print('')
                print("Escolha o código do carro que deseja devolver:")
                codigo_devolucao = int(input())
                while codigo_devolucao not in range(len(alugados)):
                    print('Erro: a opção selecionada é inválida')
                    print("Escolha o código do carro que deseja devolver:")
                    codigo_devolucao = int(input())
                carro_devolvido = alugados.pop(codigo_devolucao)
                portifolio.append(carro_devolvido)
                print("O {} foi devolvido, obrigado.".format(carro_devolvido[0], dias_aluguel))
                print('')
                print("==========")
                print("1 - Continuar | 0 - Sair da aplicação")
                selecao2 = int(input())
                while selecao2 not in [0, 1]:
                    print('Erro: a opção selecionada é inválida')
                    print("1 - Continuar | 0 - Sair da aplicação")
                    selecao2 = int(input())
                if selecao2 == 0:
                    print("Muito obrigado e até a próxima!")
                    time.sleep(3)
                    break
    except:
        print('Erro: o caracter digitado deve ser um número. Você será redirecionado ao menu inicial')
        time.sleep(3)