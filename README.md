## API de criação de hitórias

### Requisitos
#### CRUD de Histórias

1. **Cadastro e Gerenciamento de Histórias**
    - Adicionar uma nova história (título, descrição, categoria)
    - Atualizar informações da história
    - Remover uma história
    - Listar todas as histórias

#### Geração de Conteúdo

2. **Integração com a API do ChatGPT**
    - Enviar uma prompt para a API do ChatGPT e receber uma parte da história como resposta
    - Adicionar essa parte da história ao conteúdo da história em questão

#### Gestão de Usuários

3. **Cadastro e Gerenciamento de Usuários**
    - Registrar um novo usuário
    - Atualizar informações do usuário
    - Remover um usuário
    - Listar todos os usuários

#### Especificações Técnicas

- Utilização de FastAPI para a construção da API.
- Utilização de um banco de dados para armazenar os dados.
- Convenções REST na API.
- Utilização de Pydantic para validação de dados.
- Documentação interativa (Swagger).

#### Critérios de Teste

1. **Testes Unitários**
    - Testes para algumas funcionalidades do CRUD de histórias e usuários.
  
2. **Testes de Integração**
    - Testes que validam se a API está funcionando como um todo (com o banco de dados).

### 📁 Estrutura de pastas

Dentre os arquivos presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>app</b>: aqui estarão todos os arquivos do projeto.
