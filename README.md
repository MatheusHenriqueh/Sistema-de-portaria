# 🏢 Sistema de Portaria
**Autor:** Matheus Ruivo  
**Data:** 21/10/2025  
**Linguagem:** Python 🐍  

---

## 📖 Sobre o projeto
Este é um **sistema de portaria** desenvolvido em **Python**, com o objetivo de praticar **condições lógicas (`if`, `and`, `or`)**, comparação de **strings e números**, e entrada de dados pelo teclado (`input()`).

O sistema simula o funcionamento de uma portaria real:  
ele pergunta se o usuário quer **entrar ou sair**, solicita **nome, senha e número do apartamento**,  
e decide se o portão deve ser aberto com base nas informações digitadas.

---

## ⚙️ Funcionalidades
✅ Identifica se o usuário quer **entrar** ou **sair**  
✅ Verifica **nome, senha e número do apartamento**  
✅ Usa **`and` e `or`** corretamente  
✅ Mensagens de **erro personalizadas**  
✅ Comparação de tipos (`int` e `str`)  

---

## 💻 Código principal
```python
# Sistema de Portaria
# Autor: Matheus Ruivo
# Data: 21/10/2025

entrada = input("Digite 'entrar' ou 'sair': ").lower()

if entrada == 'entrar':
    print("Bem-vindo(a)!")
    nome = input("Digite seu nome: ")
    ap = input("Digite o número do seu apartamento: ")
    senha = input("Digite sua senha: ")

    n = 'Matheus'
    a = '123'
    s = '1234'

    print("Carregando...")

    if (nome == n and senha == s) or ap == a:
        print(f"✅ Portão aberto, olá {nome}!")
    else:
        print("❌ Algo está errado!")

elif entrada == 'sair':
    print("👋 Ops, você saiu do sistema!")

else:
    print("⚠️ Digite apenas 'entrar' ou 'sair'.")
