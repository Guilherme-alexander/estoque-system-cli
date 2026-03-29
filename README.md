# 📦 Sistema de Gestão de Estoque (CLI)

```
┌──────────────────────────────────────────────┐
│   SISTEMA DE ESTOQUE • PYTHON • CLI v1.0     │
│        Produtos • Vendas • Usuários          │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│                    LOGIN                     │
├──────────────────────────────────────────────┤
│  [1] Entrar                                  │
│  [2] Criar conta                             │
│  [3] Sair                                    │
└──────────────────────────────────────────────┘

➤ Escolha:
```

## 📌 Sobre o Projeto

Sistema de gestão de estoque desenvolvido em **Python + MySQL**, com interface em terminal (CLI), focado em boas práticas de arquitetura e organização de código.
O projeto simula um ambiente real de controle de produtos, vendas e usuários.

---

## 🚀 Funcionalidades

### 🔐 Autenticação
- Cadastro de usuários
- Login com senha criptografada (SHA-256)

### 📦 Produtos
- Criar produtos
- Listar produtos
- Atualizar estoque
- Remover produtos

### 💰 Vendas
- Registro de vendas
- Baixa automática no estoque
- Controle de produtos vendidos

### 📊 Relatórios
- Cálculo de lucro mensal

---

## 🧱 Arquitetura do Projeto

```

src/
├── config/        # configurações
├── database/      # conexão com banco
├── models/        # entidades
├── services/      # regras de negócio
├── ui/            # interface CLI
├── utils/         # utilitários
└── main.py        # fluxo principal

````

### ✔ Padrões utilizados
- Separação por camadas (Layered Architecture)
- Service Layer
- Código modular e escalável

---

## 🛠️ Tecnologias

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv
- pytest

---

## ⚙️ Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/estoque-system-cli.git
cd estoque-system-cli
````

---

### 2. Criar banco de dados

Execute o script:

```bash
sql/schema.sql
```

---

### 3. Configurar variáveis de ambiente

Crie o arquivo `.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=estoque_db
```

---

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 5. Rodar o sistema

```bash
python run.py
```

---

## 🧪 Testes

```bash
pytest
```

---

## 📊 Exemplo de Interface

```
+--------------------------------------------------+
|                  MENU PRINCIPAL                  |
+--------------------------------------------------+
| [1] Cadastrar Produto                            |
| [2] Listar Produtos                              |
| [3] Vender Produto                               |
| [4] Lucro do Mês                                 |
| [5] Sair                                         |
+--------------------------------------------------+
```

---

## 🔐 Segurança

* Senhas armazenadas com hash SHA-256
* Queries parametrizadas (proteção contra SQL Injection)

---

## 💎 Diferenciais do Projeto

✔ Arquitetura organizada
✔ Separação de responsabilidades
✔ Interface CLI estilizada
✔ Controle de estoque real
✔ Sistema de autenticação
✔ Testes automatizados

---

## 🚀 Melhorias Futuras

* Interface com cores (Colorama)
* Dashboard web (FastAPI + React)
* Docker
* Logs com logging
* Permissões avançadas (admin vs funcionário)

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Alexander**

---

## 📄 Licença

Este projeto é livre para uso educacional.
