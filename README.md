# Projeto em desenvolvimento!
# Python Auth & Security System

Sistema de autenticação backend desenvolvido em *Python* utilizando *Flask*, com foco em segurança de dados, criptografia de senhas e gerenciamento de sessões.

## 🚀 Tecnologias Utilizadas
* *Python* (Lógica do sistema)
* *Flask* (Microframework web)
* *Flask-Bcrypt* (Hash seguro de senhas)
* *SQLite3* (Banco de dados relacional leve)

## ⚙️ Funcionalidades
* **Cadastro de Usuários (`/register`)**: Registro com validação de duplicidade e proteção de senha utilizando hash Bcrypt.
* **Autenticação de Login (`/login`)**: Validação de credenciais e comparação segura de hashes.
* **Gerenciamento de Sessão (`session`)**: Controle de estado para manter o usuário autenticado.
* **Painel Protegido (`/dashboard`)**: Rota restrita acessível apenas mediante autenticação válida.
* *Segurança de Repositório (.gitignore)*: Exclusão de arquivos sensíveis e bancos de dados locais do versionamento público.
