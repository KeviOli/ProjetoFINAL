=====================================================================
                     COXINHA'S LIBRARY - DOCUMENTAÇÃO                  
=====================================================================

===============================
      VISÃO GERAL
===============================

A Coxinha's Library é uma aplicação web desenvolvida em Flask que permite que os usuários visualizem um catálogo de livros, filtrem os livros por título, autor ou gênero, e realizem empréstimos e devoluções de livros.

===============================
      INSTALAÇÃO
===============================

1. Clone o repositório do GitHub:

    git clone https://github.com/KeviOli/ProjetoFINAL.git

2. Navegue até o diretório do projeto:

    cd coxinhas-library

3. Instale as dependências utilizando pip:

    pip install -r requirements.txt

4. Inicie a aplicação Flask:

    python main.py

5. Acesse a aplicação em seu navegador web em http://localhost:5000.

===============================
      USO
===============================

Após iniciar a aplicação, você será redirecionado para a página inicial da Coxinha's Library. A partir daí, você pode:

- Visualizar o Catálogo: Clique em "Catálogo" na barra de navegação para ver todos os livros disponíveis.
- Filtrar Livros: Use os campos de filtro na página do catálogo para encontrar livros por título, autor ou gênero.
- Realizar Empréstimos: Selecione um livro no catálogo e clique em "Emprestar" para fazer um empréstimo.
- Devolver Livros: Selecione um livro em "Meus Empréstimos" e clique em "Devolver" para devolver um livro emprestado.

===============================
      USANDO A API VIA POSTMAN
===============================

Para interagir com a API da Coxinha's Library via Postman, siga os passos abaixo:

1. **Instalar o Postman:** Baixe e instale o Postman em https://www.postman.com/downloads/

2. **Importar a Coleção:** Importe a seguinte coleção JSON no Postman:
    ```json
    {
      "info": {
        "name": "Coxinha's Library API",
      },
      "item": [
        {
          "name": "Listar Livros",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "http://localhost:5000/livros",
              "protocol": "http",
              "host": [
                "localhost"
              ],
              "port": "5000",
              "path": [
                "livros"
              ]
            }
          }
        },
        {
          "name": "Adicionar Livro",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"titulo\": \"O Senhor dos Anéis\",\n  \"autor\": \"J.R.R. Tolkien\",\n  \"genero\": \"Fantasia\",\n  \"ano\": 1954,\n  \"copias\": 5\n}"
            },
            "url": {
              "raw": "http://localhost:5000/livros",
              "protocol": "http",
              "host": [
                "localhost"
              ],
              "port": "5000",
              "path": [
                "livros"
              ]
            }
          }
        },
        {
          "name": "Filtrar Livros",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "http://localhost:5000/livros/filtrar?filtroTitulo=Senhor",
              "protocol": "http",
              "host": [
                "localhost"
              ],
              "port": "5000",
              "path": [
                "livros",
                "filtrar"
              ],
              "query": [
                {
                  "key": "filtroTitulo",
                  "value": "Senhor"
                }
              ]
            }
          }
        },
        {
          "name": "Registrar Empréstimo",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"livro_id\": 1\n}"
            },
            "url": {
              "raw": "http://localhost:5000/emprestimos",
              "protocol": "http",
              "host": [
                "localhost"
              ],
              "port": "5000",
              "path": [
                "emprestimos"
              ]
            }
          }
        },
        {
          "name": "Devolver Livro",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"livro_id\": 1\n}"
            },
            "url": {
              "raw": "http://localhost:5000/livros/devolver",
              "protocol": "http",
              "host": [
                "localhost"
              ],
              "port": "5000",
              "path": [
                "livros",
                "devolver"
              ]
            }
          }
        }
      ]
    }
    ```

3. **Listar Livros:**
    - Método: GET
    - URL: http://localhost:5000/livros

4. **Adicionar Livro:**
    - Método: POST
    - URL: http://localhost:5000/livros
    - Headers: Content-Type: application/json
    - Body (raw, JSON):
      ```json
      {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "genero": "Fantasia",
        "ano": 1954,
        "copias": 5
      }
      ```

5. **Filtrar Livros:**
    - Método: GET
    - URL: http://localhost:5000/livros/filtrar?filtroTitulo=Senhor

6. **Registrar Empréstimo:**
    - Método: POST
    - URL: http://localhost:5000/emprestimos
    - Headers: Content-Type: application/json
    - Body (raw, JSON):
      ```json
      {
        "livro_id": 1
      }
      ```

7. **Devolver Livro:**
    - Método: POST
    - URL: http://localhost:5000/livros/devolver
    - Headers: Content-Type: application/json
    - Body (raw, JSON):
      ```json
      {
        "livro_id": 1
      }
      ```
