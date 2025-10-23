# SISMARKET
---
![GitHub last commit](https://img.shields.io/github/last-commit/cainavieira/sismarket?style=for-the-badge)  
![Python](https://img.shields.io/badge/python-3.13.5-blue?style=for-the-badge&logo=python)  
![License](https://img.shields.io/github/license/leoinfnet/sisrel?style=for-the-badge)  
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge) 
![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

---

## 📌 Descrição
**sismarket** é um projeto em **Python** criado como base de aprendizado no curso de Fundamentos de Python e se propõe a simular um caixa de atendimento de supermercado com atualização de estoque devido a compras e vendas.
O repositório reúne código, documentação e conhecimentos que vão evoluir ao longo das minhas aulas na universidade.

## 📂 Estrutura do Projeto
```
sismarket/
    src/
        ├── banco.py          # Administra o banco de dados do estoque.
        ├── caixa.py          # Arquivo onde o programa roda.
        └── crud.py           # Funções principais do programa.
        └── menu.py           # Gera as opções disponíveis ao caixa e ao estoque.
        └── util.py           # Funções auxiliares ao codigo.
    docs/
        └── CONTRIBUTING.md   # Arquivo que mostra regras de boas práticas de contribuição.
        └── README.md         # Arquivo que explica a proposta do projeto.
        └── LICENSE           # Licença MIT.
    .github/
        └── .gitignore        # Arquivo padrão Git para ignorar certos documentos# 
```
---
## 🚀 Como Executar
Clone este repositório e rode o arquivo principal:

```bash
git clone https://github.com/SEU_USUARIO/sismarket.git
cd sismarket
cd src
python /caixa.py
```

---

## 🖇️ Database Integration
💾 Agora o sistema utiliza um banco de dados PostgreSQL hospedado na Neon.tech para garantir a persistência dos dados.

---


## ⚙️ Configuração do Banco de Dados

Para executar o projeto corretamente, siga os passos abaixo:

Crie uma conta gratuita em **Neon.tech** e gere um novo banco PostgreSQL.
Copie as credenciais de conexão fornecidas (dbname,host,user,password,sslmode,channel_binding).

No diretório raiz do projeto, crie um arquivo chamado credentials.env contendo:

```
PGDATABASE=nome_do_seu_banco
PGHOST=seu_host_da_neon
PGUSER=seu_usuario
PGPASSWORD=sua_senha
PGSSLMODE=require
PGCHANNELBINDING=prefer
```

- Garanta que o arquivo credentials.env não seja versionado:
- O .gitignore já está configurado para ignorar esse arquivo.
- Depois de configurar o .env, execute novamente:
- python caixa.py

**🧠 Dica**

Se quiser usar um banco local em vez do Neon, basta criar um banco PostgreSQL local e atualizar os valores do .env com suas credenciais.

--- 

## 🛠️ Tecnologias Utilizadas
- [Python 3.13.5](https://www.python.org/)  
- GitHub (controle de versão e colaboração)  


---

## 🗺️ Roadmap
- [x] Criar repositório inicial no github.
- [x] Implementação de .env e pathlib para gestão de segredos.
- [x] Conexão do sistema ao SGBD PostgreSQL para persistência de dados.
- [ ] Refatorar o código seguindo conceitos SOLID e Clean Code.
- [ ] Fazer tratamento de erro no código onde necessário.
- [ ] Adicionar testes automaticos.
- [ ] Configurar GitHub actions para CI/CD.

---

## 🤝 Contribuição
Padrão de commits: [Conventional Commits](https://www.conventionalcommits.org/)
[Dicas](CONTRIBUTING.md)

---
## 🧑‍💻 Author 
CVT
[Perfil do Github](https://github.com/cainavieira)

---
## Licença
Este projeto está licenciado sob a **MIT LICENSE** - veja o arquivo: 
[LICENSE](LICENSE) para mais detalhes
