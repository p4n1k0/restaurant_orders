# Boas-vindas ao repositório do projeto `Restaurant Orders`!

Aqui você vai encontrar os detalhes de como foi estruturar o desenvolvimento do meu projeto a partir deste repositório.

# Entregáveis

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary>
    <p>O Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 precisa de você para finalizar sua ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.</p>
    <p>Um primeiro time iniciou o desenvolvimento deste projeto e já preparou uma estrutura inicial para que eu finalize essa construção. Assim, ao longo deste projeto eu fui responsável por construir testes para classes já implementadas, implementei uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), também implementei uma classe que gerará os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que fará a gestão de estoque dos ingredientes.</p>

🚵 Habilidades exercitadas: </br>
  - Praticar o conceito de `Hashmaps` através das estruturas de dados `Dict` e `Set`do Python; </br>
  - Praticar a ferramenta `Pandas` junto a sua estrutura de dados `DataFrame`; </br>
  - Praticar os conhecimentos de testes de software; </br>
  - Praticar os conhecimentos de orientação a objetos. </br>

</details>


# Orientações
<details>
  <summary><strong>⚠️ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:p4n1k0/restaurant_orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd restaurant_orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

  ```bash
  pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```
Obs: Alguns testes foram desenvolvidos pelo time da trybe.

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>

<details>
  <summary><strong>🗣 Me dê feedbacks sobre o projeto!</strong></summary><br />

</details>

<details>
  <summary>
    <b>👀 De olho na dica - Como rodar a aplicação?</b>
  </summary>

Para ver a aplicação rodando com as funcionalidades que implementei use o comando a seguir
```
uvicorn app:app
```
    
Acesse a rota `/docs` para ver a [documentação](http://127.0.0.1:8000/docs) gerada pelo FastAPI

</details>
