# BiblioteKA

## Idealização do projeto:

Um sistema de gestão bibliotecária.

## Diagrama (DER):
<img src="https://i.imgur.com/5Wo5cZS.png" />

## Documentação do Projeto:
<a href="https://python-production-fb5a.up.railway.app/api/docs/swagger-ui/#/"> Acessar link </a> 

## URL base

<h2>https://python-production-fb5a.up.railway.app/api</p>

## Instruções de uso:

1. Após clonar o repositório, crie seu ambiente virtual:
```bash
python -m venv venv
```
2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```
3. Faça a instalação dos pacotes utilizados no projeto:

```bash
pip install -r requirements.txt
```

4. Preencha as variáveis de ambiente seguindo o exemplo de `.env.example`:

#### SECRET_KEY= " Secret key da aplicação "
#### POSTGRES_DB= " Nome do db"
#### POSTGRES_USER= " Nome do usuário db"
#### POSTGRES_PASSWORD= " Senha do usuário db"
#### POSTGRES_HOST= " Chave opcional, para definir o host em que a aplicação irá rodar "
#### POSTGRES_PORT= " Chave opcional, para definir a porta em que a aplicação irá rodar "
#### EMAIL_HOST= " Host dos serviços de e-mail. "
#### EMAIL_PORT= " Porta dos serviços de e-mail. "
#### EMAIL_HOST_USER= " Usuário dos serviços de e-mail. "
#### EMAIL_HOST_PASSWORD= " Senha do usuário dos serviços de e-mail. "

5. Execute as migrações no seu console:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

6. Crie sua branch para sua tarefa e rode a aplicação para visualizar se ocorreu tudo certo:

```bash
git checkout -b nome da branch
python manage.py runserver
```
