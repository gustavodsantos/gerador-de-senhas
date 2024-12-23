# Gerador de Senhas

Ferramenta utilizada para criar senhas seguras de forma automática.

## Índice

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [FAQs (Perguntas Frequentes)](#faqs-perguntas-frequentes)

---

## Requisitos

Certifique-se de que você tenha os seguintes pré-requisitos antes de iniciar:

1. **Python 3.12 ou superior**  
   [Guia de instalação do Python](https://www.python.org/downloads/)

2. **Docker** (opcional, se for executar com `docker-compose`)  
   [Instalar o Docker](https://www.docker.com/products/docker-desktop)

3. **Poetry** para gerenciar dependências do projeto  
   [Guia de instalação do Poetry](https://python-poetry.org/docs/#installation)

4. Ferramentas e bibliotecas listadas no arquivo `pyproject.toml`.

---

## Instalação

Siga as etapas abaixo para configurar o projeto:

1. **Clone o repositório** para sua máquina local:
   ```bash
   git clone https://github.com/gustavodsantos/gerador-de-senhas.git
   cd gerador-de-senhas
   ```

2. **Configure um ambiente virtual** (recomendado para isolar dependências):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências usando o Poetry**:
   ```bash
   poetry install
   ```

4. **Configure as variáveis de ambiente**:
   - Utilize o arquivo `env-sample` como modelo para criar um arquivo `.env`:
     ```bash
     cp env-sample .env
     ```
   - Edite o arquivo `.env` com as informações necessárias, como nome do banco de dados, usuário, senha e outros detalhes. Por exemplo:
     ```env
     DEBUG=True
     SECRET_KEY=super-secreto
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

5. **Configure o banco de dados e aplique as migrações**:
   ```bash
   python manage.py migrate
   ```

6. **(Opcional)** Use o Docker Compose para executar o ambiente completo:
   ```bash
   docker compose up -d --build
   ```

Se algum problema ocorrer, consulte a [seção FAQs](#faqs-perguntas-frequentes) abaixo.

---

## Uso

### 1. Executando Localmente
1. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

2. Abra o navegador e acesse o endereço: [http://localhost:8000](http://localhost:8000).

3. Utilize o formulário para gerar senhas personalizadas:
   - Especifique:
     - O **comprimento** da senha.
     - Se deseja incluir **letras maiúsculas**, **números** ou **caracteres especiais**.
   - Clique em **"Gerar Senha"** para obter seu resultado.

### 2. Usando Docker
1. Caso esteja usando o Docker, o backend estará disponível na **porta 8000**.  
2. O servidor NGINX será acessível na **porta 80**.

3. Para verificar os serviços em execução:
   ```bash
   docker ps
   ```

4. Para encerrar os containers:
   ```bash
   docker compose down
   ```

### 3. Logs e Debugging
Para visualizar logs do projeto ao usar o Docker, execute:
```bash
docker logs <container_id>
```

Se problemas ocorrerem, consulte a [seção FAQs](#faqs-perguntas-frequentes).

---

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga estas etapas:

1. **Faça um fork do repositório**:
   - Clique no botão "Fork" na página principal do repositório.

2. **Clone seu repositório forkado**:
   ```bash
   git clone https://github.com/seu-usuario/gerador-de-senhas.git
   cd gerador-de-senhas
   ```

3. **Crie um branch para sua funcionalidade ou correção**:
   ```bash
   git checkout -b minha-feature
   ```

4. **Faça as alterações desejadas no código** e adicione um commit:
   ```bash
   git commit -m "Descrição clara da funcionalidade ou correção"
   ```

5. **Envie suas alterações para o repositório remoto**:
   ```bash
   git push origin minha-feature
   ```

6. **Abra um Pull Request (PR)**:
   - Descreva de forma detalhada as mudanças adicionadas e seus impactos.

### Requisitos para Contribuições:
- Certifique-se de que o código segue os padrões de formatação (ex.: PEP8).
- Antes de enviar suas alterações, execute os testes:
   ```bash
   pytest
   ```

---

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).  
Sinta-se à vontade para usar, modificar ou distribuir, desde que os termos da licença sejam respeitados.

---

## FAQs (Perguntas Frequentes)

### 1. Não consigo instalar as dependências com o Poetry. O que fazer?
Certifique-se de que o Poetry está instalado corretamente e a versão é compatível. Caso tenha problemas, tente reinstalá-lo com o seguinte comando:
```bash
pip install --user poetry
```

### 2. Ao usar Docker, os containers não iniciam. O que pode estar errado?
Certifique-se de que o serviço Docker está em execução. Você pode verificar com:
```bash
docker info
```
Caso precise rebuildar os containers, execute:
```bash
docker compose up --build
```

### 3. Recebo o erro "variável de ambiente não configurada". O que fazer?
Verifique se o arquivo `.env` foi criado corretamente com base no `env-sample`. Certifique-se de que todas as variáveis obrigatórias foram definidas.

### 4. Como parar o servidor local?
Pressione `Ctrl+C` no terminal onde o servidor está em execução.

---

## Sobre

Este projeto foi criado para facilitar a geração de senhas confiáveis e seguras.  
Para dúvidas ou sugestões, sinta-se à vontade para [abrir uma issue](https://github.com/gustavodsantos/gerador-de-senhas/issues).