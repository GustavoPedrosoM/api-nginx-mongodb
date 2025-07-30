# 📚 API Escolar com FastAPI, MongoDB e Deploy com NGINX na AWS EC2

Este projeto é uma **API escolar** desenvolvida em **Python com FastAPI** e banco de dados **MongoDB**, com objetivo de simular um sistema simples de gerenciamento de **alunos e turmas**. A aplicação realiza operações básicas de CRUD e foi implantada em um servidor EC2 na AWS, utilizando o **NGINX como proxy reverso**.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI** – Framework web moderno para APIs com Python
- **MongoDB** – Banco de dados NoSQL
- **Uvicorn** – Servidor ASGI para rodar a aplicação FastAPI
- **Docker** – Testes locais e isolamento de ambiente
- **AWS EC2** – Hospedagem da API em nuvem
- **NGINX** – Proxy reverso para servir a API de forma segura e escalável
- **Linux (Amazon Linux 2023)** – Sistema operacional do servidor

---

## 📌 Funcionalidades

- CRUD de **alunos**:
  - Cadastro de aluno
  - Listagem de todos os alunos
  - Consulta por ID
  - Atualização e exclusão

- CRUD de **turmas**:
  - Cadastro de turma
  - Listagem de turmas
  - Associação entre alunos e turmas
  - Consulta de alunos por turma

---

## 🐳 Rodando Localmente com Docker

> Para testes em ambiente local:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio  
```

2. Execute o MongoDB e a API com Docker Compose
```bash
docker-compose up --build
```

3. Acesse a API em:
http://localhost:8000/docs

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

☁️ Deploy na AWS EC2
O processo de deploy incluiu:

1. Criação de instância EC2 (Amazon Linux 2023)

2. Instalação do Python, Uvicorn e dependências

3. Instalação do MongoDB local ou conexão com cluster externo

4. Execução da API com Uvicorn na porta 8000

5. Instalação do NGINX

6. Configuração do NGINX como proxy reverso para redirecionar as requisições da porta 80 para 8000


🔁 Exemplo de bloco do arquivo de coniguração do NGINX:
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}


🔧 Endpoints principais
Após o deploy, os endpoints estarão disponíveis em:
GET    /alunos
POST   /alunos
GET    /alunos/{id}
PUT    /alunos/{id}
DELETE /alunos/{id}

GET    /turmas
POST   /turmas
GET    /turmas/{id}
GET    /turmas/{id}/alunos

Acesse a documentação interativa da API em:
http://<seu-ip-publico>/docs

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📚 Aprendizados
Esse projeto foi construído com foco em consolidar conhecimentos em backend com FastAPI, além de explorar ferramentas e práticas de infraestrutura como:

Deploy em servidores Linux com EC2

Gerenciamento de servidores com SSH

Instalação e configuração de MongoDB

Utilização do NGINX como proxy reverso

Testes e versionamento com Docker


👨‍💻 Autor
Gustavo Pedroso
https://www.linkedin.com/in/gustavopedroso19/



