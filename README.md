# Gerador de Senhas

Ferramenta utilizada para criar senhas seguras de forma automática.

## Requisitos

- Python 3.12 ou superior
- Docker (em caso de uso com `docker-compose`)
- Ferramentas e bibliotecas listadas em `pyproject.toml`

## Instalação

1. Clone este repositório para sua máquina local:
   ```bash
   git clone git@github.com:gustavodsantos/gerador-de-senhas.git
   cd gerador-de-senhas
   ```

2. Configure um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências usando o Poetry:
   ```bash
   poetry install
   ```
4. Configure as variáveis de ambiente necessárias. Um exemplo de arquivo `.env` pode incluir:
   ```
   DATABASE_URL=postgres://<usuário>:<senha>@localhost:5432/<nome_do_banco>
   SECRET_KEY=<sua_chave_secreta>
   ```
5. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
6. (Opcional) Utilize `docker-compose` para rodar os serviços:
   ```bash
   docker-compose up -d --build
   ```
## Uso

1. Execute o servidor localmente:
   ```bash
   python manage.py runserver
   ```
2. Acesse o projeto no navegador através de [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. Para gerar senhas, utilize o formulário fornecido na interface da aplicação. Preencha os parâmetros (comprimento, letras maiúsculas, números, caracteres especiais) conforme necessário e clique em "Gerar Senha".

4. Caso esteja utilizando o Docker, o backend estará exposto na porta 8000, enquanto o servidor NGINX será acessível na porta 80.
