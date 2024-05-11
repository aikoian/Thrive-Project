
# Passo 1 : Adicionar ao meu código algumas funções que serão uteis para o desenvolvimento do projeto.
# Passo 2 : Importar e configurar as bibliotecas necessárias
# Passo 3 : Criar um menu de opções para o usuário escolher o que deseja fazer.
# Passo 4 : Estruturando o código e o seu funcionamento.
'''******************************************************************************************************************'''
# Passo 1 : Implementando algumas funções que serão úteis para o projeto.

def leiaint (msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO ! Digite um número inteiro válido . \033[m')
        if ok:
            break
    
    return valor
          
def leiastr(msg):
    while True:
        try:
            mensagem = str(input(msg)).strip()
            if mensagem == '':
                raise ValueError('\033[0;31m Entrada vazia, Por gentileza só utilize letras ! \033[m')
            elif all(c.isalpha() or c.isspace() for c in mensagem):
                break
            else:
                raise ValueError('\033[0;31m Caráctere Inválido, Por gentileza só utilize letras ! \033[m')
        except ValueError as e:
            print(e)
    return mensagem

def color (msg , color = 0):
    '''
               ___________________
              |.  MENU DE AJUDA  .|
     _____________________________________________________________________________________
    | -- > Descrição :                                                                    |
    |                                                                                     |                                            |
    | 'color()' é um função utilizada para colorir texto em geral.                        |
    | ela comtempla até o momento as cores (red , blue , green , yellow , purple , cyan)  |
    |_____________________________________________________________________________________|
     ____________________________________________
    |--> Funcionamento geral da função 'color()':|_________________________________          
    |                                                                              |
    | -Ela recebe um parâmetro obrigatório (msg) e um parametro opcional (color).  |
    |                                                                              |_____________________________________ 
    |                     _________________________________________________________________________________________      |
    |                    |- No entanto eu acho que se você está tentando usar este pacote para colorir o seu texto |     |
    |                    | recomendo fortemente que você utilize o parâmetro 'color()'                             |     |
    |                    |_________________________________________________________________________________________|     | 
    |                                                                                                                    |
    | - Primeiramente deve se digitar o nome da função 'color' seguido de '()'.                                          |
    | - Depois disso deve-se digitar o parâmetro obrigatório (msg) entre aspas duplas. / ou simples ;) /                 |
    | * Exemplo :                                                                                                        | 
    |          color('  Hello World ! ')                                                                                 |
    |                                                                                                                    |
    | - Por fim adicione o segundo parâmetro (color = 'color of your choice') e escreva a cor entre parênteses.          |
    | * Exemplo :                                                                                                        |
    |                   color('Hello World' , color = 'red' )                                                            |
    |                                                                                                                    |
    |                O exemplo acima exibe o texto na cor vermelha!                                                      |
    |                                                                                                                    |
    |* ------------------------------------------------------------------------------------------------------------------*
    |   * Observações:                                                                                                   |
    |                                                                                                                    |
    | - É impportante lembrar de usar a vírgula , caso contrário o parâmetro opcinal vai ser anulado                     |
    |    e consequentemente o seu texo vai ser exibido na cor padrão do seu terminal.                                    |
    |                                                                                                                    |
    | ->  Atente-se também a utilização da sintaxe correta de modo geral ( '' , () , = )                                 |
    |                                                                                                                    |
    |                                                                                                                    |
    |____________________________________________________________________________________________________________________|
    |  Atenciosamente , Aiko Ian. |
    |_____________________________|

    '''
    if color == 0:
        print(msg)
    if color == "red":
        print (f'\033[31m {msg} \033[m')
    if color == "green":
        print(f'\033[32m {msg} \033[m')
    if color == "yellow":
        print(f'\033[33m {msg} \033[m')
    if color == "cyan":
        print(f'\033[36m {msg} \033[m')
    if color  == "blue":
        print(f'\033[34m {msg} \033[m')
    if color == "purple":
        print(f'\033[35m {msg} \033[m')
    
def leiafloat(x):
    while True:
        escolha = input(f'{x}')
        if escolha.isdigit():
            return int(escolha)
        elif '.' in escolha and escolha.count('.') == 1 and escolha.replace('.', '', 1).isdigit():
            try:
                escolha = float(escolha)
                return escolha
            except ValueError:
                print('Por favor digite apenas números. Separados por (.) caso necessário.')
        else:
            print('Por favor digite apenas números. Separados por (.) caso necessário.')

# Passo 2: Importando a biblioteca do GEMINI.

import google.generativeai as genai

# Passo 2.1 : Configurando a biblioteca.

genai.configure(api_key = "AIzaSyDYsTvxJkwUDllcvZ58lbLjJd6hzhWCFOY")
model = genai.GenerativeModel('gemini-pro')

# Passo 2.2 : Testando o funcionamento da lib.

# response = model.generate_content("teste")
# print(response.text)

# Passo 3: Começando o código e criando um menu.

opc = 0
nome = ''
while True:
    
    print(''' 
                                                                 ________________
                                                                |_MENU DE OPÇÕES_|
                                                     _______________________________________________    
                                                    | • 1) Informações de Funcionamento.            |
                                                    | • 2) Analisar o sono.                         |
                                                    | • 3) Calcular IMC.                            |              
                                                    | • 4) Informações nutricionais do alimento.    |
                                                    | • 5) Receitas Saudáveis                       |
                                                    | • 6) Acessar Material Auxiliar.               |
                                                    | • 7) Sair do Sistema.                         |
                                                    |_______________________________________________|
                                                   
       ''')
    opc = leiaint('Digite a opção desejada: ')
    while opc not in range(1,8):
        color ('Opção Inválida! Tente Novamente.',color='red')
        opc = leiaint('Digite a opção desejada: ')
    
    if nome == '':
        print()
        nome = leiastr('Olá,qual o seu nome ? ').title()
    if opc == 1:
        print()
        print('''
              
              Thrive: Seu Guia para uma Vida Mais Saudável

    O Thrive é um sistema inovador que utiliza inteligência artificial para ajudar você a alcançar seus objetivos de saúde e bem-estar.
 Com uma interface simples e interativa, o Thrive oferece uma variedade de ferramentas para analisar seu sono,
 calcular seu IMC, descobrir informações nutricionais e até mesmo encontrar receitas saudáveis personalizadas.

              
              Como o Thrive Funciona:

    Análise de Sono: 
              
Responda a algumas perguntas sobre seus hábitos de sono e o Thrive, com a ajuda da avançada API Gemini do Google,
irá avaliar a qualidade do seu sono e oferecer dicas personalizadas para melhorar seus padrões de descanso.
              
    Cálculo de IMC: 
              
Descubra seu Índice de Massa Corporal de forma rápida e precisa. O Thrive analisa seu peso e altura para fornecer uma avaliação
completa do seu IMC e seus possíveis impactos na saúde.
              
    Informações Nutricionais:
               
Curioso sobre o valor nutricional de um alimento específico? Basta perguntar ao Thrive! Ele fornecerá informações detalhadas 
sobre calorias, macronutrientes, vitaminas e minerais, ajudando você a fazer escolhas alimentares mais conscientes.
              
    Receitas Saudáveis Personalizadas:
        
Deseja explorar novas opções culinárias? O Thrive gera receitas deliciosas e saudáveis com base em suas 
preferências de refeição e ingredientes disponíveis.

        Thrive: Seu Parceiro na Jornada para o Bem-Estar
              
Com o Thrive, você tem um guia personalizado para uma vida mais saudável ao seu alcance.
Explore as funcionalidades, aprenda com as informações e dicas, e descubra como pequenos
ajustes podem fazer uma grande diferença em sua saúde e qualidade de vida.''')
        
        print()
    elif opc == 2 : 
        print()
        print(f'Seja Bem Vindo(a) {nome},  Vamos começar !')
        print()
        print('Para calcular a qualidade do seu sono, vamos precisar de alguns dados.')
        print()
        print()
        qtd = str(input('Escreva de forma resumida quantas horas você costuma dormir por dia : '))
        print()
        efic = str(input('Você possui alguma dificuldade de pegar no sono após se deitar?'))
        print()
        reg = str(input(f'{nome}, você possui uma rotina regular de sono, com horários consistentes para dormir e acordar, mesmo nos finais de semana?'))
        print()
        sent = str(input('Como você avalia a qualidade do seu sono em geral? (De muito ruim a excelente) : '))
        print()
        color('Estou processando as informações...',color = 'yellow')
        print()
        response = model.generate_content(f"""                                      
Haja como um profissional da saúde,especializado em ciência do sono.

Faça uma análise do sono de um paciente chamado {nome}.{nome} respondeu um questionário com algumas perguntas para facilitar o seu trabalho.

Perguntas :      

 1 - Escreva de forma resumida quantas horas você costuma dormir :
 resposta --> {qtd}
2 - Você possui alguma dificuldade de pegar no sono após se deitar?
 resposta --> {efic}
3 - você considera sua rotina de sono regular?
 resposta --> {reg}
4 - Como você avalia a qualidade do seu sono em geral? (De muito ruim a excelente):
 resposta --> {sent}

Por fim avalie a qualidade das informações presente no questionário e caso sejam irrelevantes apenas faça um resumo de uma rotina de sono 
saudável explicitando que as informações disponibilizadas no questionário não foram as esperadas,pedindo para que o usuário tente novamente.

caso as informações do questionário façam sentido,faça uma avaliação dos hábitos de sono do paciente e de 3 dicas para
a melhora da qualidade de sono do paciente.
Você deve usar entre 5 a 10 linhas.Onde 7 seria o ideal e 10 será o limite.
Também considere se basear no livro "Por que nós dormimos" do Matthew Walker
                                          
                                          """)
        print(response.text)


    elif opc == 3:
        print()
        print(f'Olá {nome}, para fazer um calculo preciso do seu IMC iremos precisar de algumas informações.')
        print()
        peso = str(input('Digite o seu peso aproximado :'))
        print()
        altura = str(input('Digite a sua altura aproximada : '))
        print()
        color('Estou processando as informações...',color = 'yellow')
        print()
        response = model.generate_content(f"""
Haja como um profissional de nutrição. Seu trabalho é calcular o IMC de um paciente chamado {nome}.

{nome} respondeu um questionário para lhe auxiliar a fazer esse calculo.

QUESTIONÁRIO : 

Pergunta 1 -- >  Digite o seu peso aproximado :
Resposta -- > {peso}
------------------------------------------------
Pergunta 2 -- > Digite a sua altura aproximada :
Resposta -- > {altura}

Agora você deve analisar se as informações disponibilizadas no questionário  são úteis para o cálculo do IMC do paciente.

Se as respostas do questionário  não forem o úteis informe o paciente que não foi possível fazer o calculo do seu IMC pois 
as informações disponiveis não foram o suficiente.

Se as informações forem o suficiente,faça o calculo do IMC do paciente e informe um breve detalhamento da sua situação do paciente
enfatizando o resultado e seus possíveis impactos.

Você deve usar entre 5 a 10 linhas.Onde 7 seria o ideal e 10 será o limite.

""")
        print(response.text)

    elif opc == 4: 
        print()
        alimento=str(input(('Qual o alimento que você deseja saber a informação nutricional? ')))
        print()
        color('Analisando o alimento digitado...',color='yellow')
        print()
        response = model.generate_content(f"""
Haja como um profissional de nutrição. Seu trabalho é mostrar a informação nutricional de um alimento,com base na resposta do questionário abaixo.

Pergunta -->  Qual o alimento que você deseja saber a informação nutricional?                                        
Resposta --> {alimento}

É fundamental ser breve e didático. Utilize no máximo 15 linhas.

caso o nome do alimento não faça sentido,mostre uma mensagem de erro que instrua o usuário 
a tentar novamente.
""")
       
        print(response.text)
    elif opc == 5:
        print()
        print('Para melhor atender suas necessidades, vamos dividir as possiveis receitas em refeições.')
        print()
        escolha = str(input("Você precisa de uma receita para o Café da Manhã,Almoço ou Jantar ?"))
        print()
        ingredientes = str(input('Digite pelo menos 3 ingredientes que você deseja utilizar:'))
        print()
        color('Estou processando as informações...',color = 'yellow')
        print('---------------------------------------------------------------------------------------------------------')
        print()
        response = model.generate_content(f"""
Haja como um profissional de nutrição que têm profundos conhecimento culinários. Seu objetivo é promover uma receita simples e saudável
de acordo com a escolha da refeição de um cliente chamado {nome}.

Deve ser uma receita de : {escolha}

Contendo os ingredientes : {ingredientes}

Seja detalhado sobre a receita e trate de mencionar os beneficios dela.

use no máximo 15 linhas.

""")
        print(response.text)
    elif opc == 6:
        print(f""" 
    {nome}, Fico muito feliz em saber que você se interressou pelo material extra ! 
               
    O que esperar do material ? 
              
       - O material vai conter pdf's sobre educação do sono e saúde nutricional como um todo.
       - Recomendações de livros.
       - Uma sessão para contato.
       - Recomendações de sites que podem auxiliar o seu estudo sobre o sono.
       - Recomendações de sites que irão lhe auxiliar na dieta.
       - Alguns vídeos no youtube relacionados. 
              
    Como ter acesso ao material ?

       -- > Basta copiar o link do drive abaixo :)
    
       https://drive.google.com/drive/folders/1ShVfeIdX_Wrec8GzZI5-FfSGcxIV4e4S?usp=sharing 
""")
    elif opc == 7:
        break
    