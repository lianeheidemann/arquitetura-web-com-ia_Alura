# Prompts - Aula 2


1. Crie um ambiente virtual em Python usando a venv e faça a ativação


<!-- O Uvicorn é um servidor web ASGI (Asynchronous Server Gateway Interface) ultrarrápido para Python. Ele é o motor padrão de frameworks assíncronos modernos como o FastAPI e o Starlette, projetado para suportar conexões persistentes, como WebSockets e HTTP/1.1.Ele é frequentemente utilizado para iniciar aplicativos e APIs localmente ou em ambientes de produção 

Rodando direto usando a pasta do ambiente virtual (Recomendado no Windows):
.venv\Scripts\uvicorn main:app --reload

Ver no Chrome a aplicação: http://127.0.0.1:8000 
Ver a Documentação: http://127.0.0.1:8000/redoc 
Abrir -->
2. Instale o uvicorn na venv deste projeto


3. Você vai criar o primeiro servidor de uma API de álbum de figurinhas.

   Crie um arquivo main.py com um servidor FastAPI que tenha apenas 1 endpoint:

   1. GET "/" → retorna o JSON {"mensagem": "Olá, mundo! 🌍"}
   (use uma função chamada hello\_world)

   Requisitos:

   * Use apenas Python com FastAPI (import: from fastapi import FastAPI)
   * Crie a aplicação com app = FastAPI()
   * Adicione comentários em português explicando cada parte
   * Não adicione nenhum outro endpoint


4. No mesmo arquivo main.py, adicione um segundo endpoint, mantendo o endpoint "/" que já existe:

   2. GET "/figurinhas" → retorna uma lista com 2 figurinhas de exemplo
(use uma função chamada listar\_figurinhas)
Cada figurinha é um objeto com os campos:

      * id (número inteiro)
      * nome (texto)
      * categoria (texto)
Use estas duas figurinhas:
      * {id: 1, nome: "Alan Turing",   categoria: "IA"}
      * {id: 2, nome: "John McCarthy", categoria: "IA"}

   Requisitos:

   * Mantenha tudo que já existe no arquivo
   * Adicione comentários em português
   * Não adicione nenhum endpoint além desses dois







   \---



   Abrir ambiente virtual:

   .\\.venv\\Scripts\\Activate.ps1


<!-- Se você estiver vendo uma linha ondulada vermelha ou amarela (um aviso/erro de importação) no main.py perto do import fastapi ou FastAPI, mas o servidor está rodando normalmente, isso acontece porque o seu editor de código (como o VS Code) não está usando o ambiente virtual (.venv) do projeto.

Como o pacote fastapi está instalado dentro da pasta .venv, o editor de código precisa saber que deve procurar os pacotes lá.

Como resolver no VS Code:
Abra o painel de comandos com o atalho: Ctrl + Shift + P (ou Cmd + Shift + P se estiver no Mac).
Digite: "Python: Select Interpreter" (ou Python: Selecionar Interpretador).
Na lista que aparecer, escolha a opção que aponta para a sua pasta .venv, por exemplo:
.\.venv\Scripts\python.exe (ou algo que contenha ('.venv': venv))
Depois: "Developer: Reload Window"
Após selecionar o interpretador correto e recarregar a janela, o editor de código passará a reconhecer o fastapi e o erro desaparecerá do arquivo. -->
