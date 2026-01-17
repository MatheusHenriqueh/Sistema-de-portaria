#Sistema de Portaria.
#Autor: Matheus Henrique
#Data: 21/10/25

entrada = input("Digite entrar, se quiser sair digite sair:")

if entrada == 'Entrar' or entrada =='entrar' or entrada == 'ENTRAR':#Sempre colocar o valor das variável.
    print("Bem-vindo(a)!")
    nome = input("Digite seu nome:")
    ap = (input("Digite seu número do apartamento:"))#Sem int!
    senha = (input("Digite sua senha:"))
    n = 'Matheus'
    a =  123#Números sem aspas!!
    s = 1234
    print("Carregando...")
    if (nome == n and senha == s) or ap == a:
        print(f"Portão aberto, olá {nome}!")   
    else:
        print("Algo está errado!!")
elif entrada == 'Sair' or 'sair' or 'SAIR':
    print("Ops, você saiu do sistema!")
else:

    print("Digite entrar ou sair!")
