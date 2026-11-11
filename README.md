# Portal de Notícias

Aplicação Django de portal de notícias com autenticação, perfis, CRUD de postagens e API REST.

## Funcionalidades

- Cadastro, login e logout de usuários.
- Perfis de leitor e escritor.
- Publicação, edição e exclusão de postagens.
- Upload de imagens para as postagens.
- Página inicial com as últimas notícias.
- API REST para listagem de postagens em `/api/v1/postagens/`.
- Painel administrativo do Django.

## Stack

- Python 3.12+
- Django 5.1
- Django REST Framework
- SQLite
- HTML, CSS e JavaScript
- GitHub Actions

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra `http://127.0.0.1:8000/`. O admin fica em `/admin/`.

### Variáveis de ambiente

| Variável | Padrão | Uso |
|---|---|---|
| `DJANGO_SECRET_KEY` | `dev-only-change-me` | obrigatória em produção |
| `DJANGO_DEBUG` | `1` | use `0` em produção |
| `DJANGO_ALLOWED_HOSTS` | vazio | hosts separados por vírgula |

## Testes

```bash
python manage.py test
```

O CI em `.github/workflows/django.yml` roda `manage.py check` e a suíte em Python 3.12.

## Estrutura

```
preEstagio/      configuração do projeto
home/            usuários, autenticação e perfil
postagem/        postagens, formulários, serializers e API
templates/       páginas HTML
static/          CSS
media/           imagens enviadas
```

## API

`GET /api/v1/postagens/` retorna todas as postagens em JSON.

## Limitações

- O projeto usa SQLite por padrão.
- Não há paginação na API.
- O upload de imagens usa o armazenamento local.
- Projeto acadêmico, sem deployment de produção configurado.

## Licença

MIT. Ver [LICENSE](LICENSE).
