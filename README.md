# 📚 API de Gestão Escolar

Este repositório contém a **API de Gestão Escolar**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Gestão Escolar é um **microsserviço** na qual é responsável pelo gerenciamento de alunos, professores e turmas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (Para os testes unitários)
- Unittest (para testes unitários da API)

---

## 🐳 Como Executar as APIs com Docker

Este guia mostra como executar a API em Docker.

## 📥 Clonando o Repositório

O ProjetoApi é responsável pelo gerenciamento de alunos, professores e turmas. Para executar corretamente, você deve clonar o repositório:

```
git clone https://github.com/seu-usuario/ProjetoApi.git
```

---

### 1º Passo - Construa a imagem api-gestão-escolar da [api de gestão](https://github.com/gortin1/ProjetoApi.git) 

``` bash
cd ProjetoApi
docker build -t api-gestao-escolar .
``` 

### 2º Passo - Rode a imagem criada na network que você criou

``` bash
docker run -d -p 5000:5000 --name api-gestao-escolar api-gestao-escolar
```

#### Pronto! Você já pode utilizar a API tranquilamente!

⚠️ Aviso: A API de Reservas estará acessível em:

* [http://localhost:5000/swagger](http://localhost:5000/swagger)
* [http://localhost:5000/api/alunos/](http://localhost:5000/api/alunos/)
* [http://localhost:5000/api/professores/](http://localhost:5000/api/professores/)
* [http://localhost:5000/api/turmas/](http://localhost:5000/api/turmas/)

---

## 📡 Endpoints Principais

### Alunos
- `GET / alunos` – Lista todos os alunos
- `POST / alunos` – Cria um novo aluno
- `GET / alunos/<id>` – Mostra os dados de um aluno específico
- `PUT / alunos/<id>` – Atualiza um aluno (é necessário preencher todos os campos para atualizar o aluno)
- `DELETE / alunos/<id>` – Remove um aluno

### Exemplo de corpo JSON para POST(alunos) :

```json
{
  "nome": "string",
  "data_nascimento": "string",
  "nota_primeiro_semestre": 0,
  "nota_segundo_semestre": 0,
  "turma_id": 0
}
```

### Professores
- `GET / professores` – Lista todos os professores
- `POST / professores` – Cria um novo professor
- `GET / professores/<id>` – Mostra os dados de um professor específico
- `PUT / professores/<id>` – Atualiza um professor (é necessário preencher todos os campos para atualizar o professor)
- `DELETE / professores/<id>` – Remove um professor

### Exemplo de corpo JSON para POST(professores) :

```json
{
  "nome": "string",
  "idade": 0,
  "materia": "string",
  "observacoes": "string"
}
```

### Turmas
- `GET / turmas` – Lista todas as turmas
- `POST / turmas` – Cria uma nova turma
- `GET / turmas/<id>` – Mostra os dados de uma turma em específico
- `PUT / turmas/<id>` – Atualiza uma turma (é necessário preencher todos os campos para atualizar a turma)
- `DELETE / turmas/<id>` – Remove uma turma

### Exemplo de corpo JSON para POST(turmas) :

```json
{
  "descricao": "string",
  "ativo": true,
  "professor_id": 0
}
```

---

## 📦 Estrutura do Projeto

```
api/
├── aluno/
│   ├── aluno_model.py
│   └── aluno_route.py
├── professor/
│   ├── professor_model.py
│   └── professor_route.py
├── swagger/
│   └── swagger_config.py
├── namespaces/
│   ├── aluno_namespace.py
│   ├── professor_namespace.py
│   └── turma_namespace.py
├── test/
│   └── test.py
├── turma/
│   ├── turma_model.py
│   └── turma_route.py
├── app.py
├── config.py
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
     
```

---

## 🛠️ Futuras Melhorias

- Integração via fila (RabbitMQ) com outros microsserviços
- Autenticação de usuários
  
---

## 🧑‍💻 Autores

- [Camila Ribeiro](https://github.com/camilasribeiro)
- [Fernando Storel](https://github.com/Fernandostorel)
- [Gabriel Nathan](https://github.com/gortin1)
- [Nicolas Lima](https://github.com/nicolas-liima)


Projeto de arquitetura com Flask e microsserviços.
