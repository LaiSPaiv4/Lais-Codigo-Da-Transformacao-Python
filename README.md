# Código da Transformação - Python 🐍

Este repositório foi criado para organizar todas as atividades e projetos desenvolvidos durante 
o curso de CDT. O objetivo é demonstrar a evolução do aprendizado, desde a lógica básica até
estruturas mais complexas.

## 📁📍 Estrutura do Repositório

O projeto está dividido em módulos:

* **Modulo_01/**: Contém o desafio prático da Calculadora Interativa.
* **Modulo_02/**: Contém o desafio prático Introdução ao Python.
* **Modulo_03/**: Contém o desafio prático Lógica de Programação.
* **Modulo_04/**: Contém o desafio prático Estrutura de Dados.
* **Modulo_05/**: Contém o desafio prático Modularização com Funções.
* **Mudulo_06/**: Contém o desafio prático Manipulação de Arquivos.
* **Mudulo_07/**: Contém o desafio prático Modularização e Bibliotecas Externas.
* **Mudulo_08/**: Contém o desafio prático Programação Orientada a Objetos.
* **Modulo_09/**: Contém o desafio prático Tratamento de Erros.
* **Modulo_10/**: Contém o desafio prático Introdução a APIs.
* **Modulo_11/**: Contém o desafio prático Banco de Dados com PostgreSQL.
* **Modulo_12/**: Contém o desafio prático Testes Automatizados em Python
* **Modulo_13/**: Contém o desafio prático Desenvolvimento de APIs com Flask
* **Modulo_14/**: Contém o desafio prático 
* *(Futuros módulos serão adicionados aqui)*

---

## 🧮 Projeto: Calculadora Interativa (Módulo 01)

O primeiro desafio consistiu em desenvolver uma calculadora funcional que executa operações básicas 
de aritmética via terminal.

### 🚀 Funcionalidades
* Soma, Subtração, Multiplicação e Divisão.
* Tratamento de erro para **divisão por zero**.
* Tratamento de erro para **entradas inválidas** (letras ou símbolos) usando blocos `try/except`.
* Laço de repetição `while True` que permite várias operações sem fechar o programa.
* Opção de encerramento amigável (Opção 0).

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Conceitos:** Lógica de programação, condicionais (`if/elif/else´), laços de repetição e
tratamento de exceções.

---

## 📅 Projeto: Boas-vindas e Data Atual (Módulo 02)

O desse desafio aqui foi criar um programa que interage com o usuário e utiliza informações do próprio
computador para exibir a data e a hora.

### ✨ O que o programa faz?
* Pergunta o nome: O usuário digita seu nome e recebe uma saudação personalizada.
* Mostra o dia e a hora: O programa consulta o relógio do sistema e exibe o momento exato da execução.
* Formatação amigável: A data aparece no formato que usamos no Brasil (Dia/Mês/Ano), facilitando a leitura.

### 🛠️ Ferramentas Utilizadas
* Comando input: Usado para conversar com o usuário e receber o nome.
* Comando print: Usado para exibir as mensagens na tela.
* Biblioteca datetime: Uma ferramenta pronta do Python que serve para trabalhar com datas e horários.
* Função now: Recurso que "tira uma foto" do momento atual do relógio.

---

## 🤖 Projeto: Lógica de Programação e Tomada de Decisão (Módulo 03)

O foco deste módulo foi aprofundar na lógica de programação, criando programas que conseguem analisar dados, 
comparar valores e repetir tarefas através de menus interativos.

### ✨ O que o programa faz?
* Operações Matemáticas: Realiza cálculos de soma, subtração, multiplicação e divisão (com proteção contra divisão por zero).
* Comparação de Valores: Analisa dois números e identifica qual é o maior ou se são iguais.
* Classificação por Faixa Etária: Identifica a fase da vida do usuário (Criança, Adolescente, Adulto ou Idoso)
com base na idade informada.
* Menu Interativo (Desafio Extra): Um sistema que utiliza um laço de repetição para permitir que o usuário escolha várias operações
sem precisar reiniciar o programa.

### 🛠️ Ferramentas Utilizadas
* **Estruturas Condicionais (`if`, `elif`, `else`):** Essenciais para decidir qual mensagem exibir ou qual cálculo realizar.
* **Laço de Repetição (`while True`):** Utilizado no desafio extra para criar um menu que só fecha quando o usuário solicita.
* **F-strings:** Usadas para formatar a saída dos dados de forma limpa e profissional.
* **Operadores de Comparação e Lógicos:** Para validar as idades e comparar a grandeza dos números.

---

## 🎲 Projeto: Estruturas de Dados (Módulo 04)

Este módulo foi focado no domínio de estruturas que permitem armazenar múltiplos dados e na criação de sistemas interativos complexos, 
utilizando Listas e Dicionários.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Gestor de Compras):** Um sistema dinâmico para manipular listas, permitindo adicionar, remover e visualizar
itens em tempo real.
* **Atividade 02 (Dicionário de Aluno):** Organização de informações heterogêneas (texto, números e listas) dentro de um
objeto único para facilitar o acesso via chaves.
* **Atividade 03 (Classificador de Paridade):** Um algoritmo que percorre sequências numéricase utiliza lógica matemática (`%`) 
para separar números pares de ímpares.
* **Desafio Extra (Agenda de Contatos):** Um sistema completo de gerenciamento usando Dicionários, aplicando o método `.pop()` 
para remoção segura e buscas otimizadas por nome.

### 🛠️ Ferramentas Utilizadas
* **Listas (`[]`):** Armazenamento sequencial e métodos `append()` e `remove()`.
* **Dicionários (`{}`):** Mapeamento de informações por Chave e Valor e uso do método `.items()`.
* **Loops (`while` e `for`):** Criação de menus infinitos e iteração sobre coleções de dados.
* **Método `.pop()`:** Utilizado na agenda para remover registros e recuperar o valor removido simultaneamente.
* **Operadores Lógicos e Aritméticos:** Essenciais para a filtragem de dados e validação de opções do menu.

---

## 👩‍💻 Projeto: Modularização com Funções em Python (Módulo 05)

Este módulo foi focado na criação de **Funções**, permitindo a reutilização de código, organização lógica e o processamento de dados
através de parâmetros e retornos.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Saudação Personalizada):** Criação de uma função simples para padronizar mensagens de boas-vindas utilizando parâmetros.
* **Atividade 02 (Cálculo de Média e Status):** Uma função que recebe uma lista de notas, calcula a média aritmética e retorna tanto o valor numérico quanto o status (Aprovado/Reprovado).
* **Atividade 03 (Análise de Extremos):** Utilização das funções nativas `max()` e `min()` dentro de uma função customizada para identificar 
os maiores e menores valores de uma lista.
* **Atividade Extra (Sistema de Autenticação):** Desenvolvimento de uma lógica de login que integra funções com dicionários para validar 
usuários e senhas de forma segura.

### 🛠️ Ferramentas e Conceitos Aplicados
* **Definição de Funções (`def`):** Estruturação de blocos de código reutilizáveis.
* **Parâmetros e Argumentos:** Passagem de dados para dentro das funções para processamento dinâmico.
* **Comando `return`:** Técnica para extrair resultados das funções e utilizá-los em outras partes do programa.
* **Lógica de Validação:** Verificação de existência de chaves em dicionários combinada com comparação de valores.
* **Formatação Numérica:** Uso de `: .2f` para exibir médias com apenas duas casas decimais.

---

## 📂 Projeto: Manipulação de Arquivos (Módulo 06)

Este módulo foi focado no aprendizado de como o Python interage com o sistema de arquivos do computador, permitindo ler, criar e editar diferentes formatos de armazenamento de dados de forma persistente.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Persistência em TXT):** Criação de um sistema de gravação e leitura de arquivos de texto plano, utilizando codificação `UTF-8` para garantir a integridade de caracteres especiais.
* **Atividade 02 (Integração JSON):** Manipulação de dicionários complexos (clientes premium) e sua conversão para o formato `JSON`, incluindo formatação visual com recuo (indent) e leitura dinâmica dos dados.
* **Atividade 03 (Sistema de Notas em CSV):** Um gerenciador interativo via terminal que permite adicionar nomes, matérias e notas em uma planilha, com verificação automática de cabeçalho e exibição formatada em colunas.
* **Atividade Extra (Sistema de Backup Automatizado):** Um utilitário de sistema que utiliza bibliotecas de manipulação de diretórios para criar cópias de segurança de pastas inteiras, organizando-as por data e hora `(timestamp)`.

### 🛠️ Ferramentas Utilizadas
* **Bibliotecas Padrão do Python:** Uso das ferramentas nativas `json` (para dados estruturados), `csv` (para planilhas), 
`os` e `shutil` (para manipulação de pastas e arquivos de sistema) e `datetime` (para controle de tempo no backup).
* **Gerenciador de Contexto (with open()):** Utilizado para garantir a abertura e o fechamento seguro de todos os arquivos gerados.
* **Modos de Escrita e Leitura:** Aplicação prática dos parâmetros 'w' (escrita), 'r' (leitura) e 'a' (anexar dados).
* **Tratamento e Formatação:** Uso de f-strings com alinhamento e codificação UTF-8 para evitar erros de acentuação nos arquivos.

---

## 📦 Projeto: Modularização e Bibliotecas Externas (Módulo 07)

Este módulo foi dedicado à organização de projetos em múltiplos arquivos e ao uso de bibliotecas externas para aumentar a produtividade, separando a lógica de funções da execução principal do programa.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Criação de Módulos Próprios):** Desenvolvimento do arquivo utilidades.py com funções matemáticas personalizadas (soma, subtração e potência), importadas para o script principal.
* **Atividade 02 (Uso de Bibliotecas Externas):** Implementação da biblioteca Faker para geração de dados fictícios em português e integração com datetime para carimbos de data/hora.
* **Atividade 03 (Jogo Adivinha-Python):** Sistema interativo de adivinhação com geração de números aleatórios e cálculo de proximidade para fornecer dicas ao usuário.

### 🛠️ Ferramentas Utilizadas
* **Modularização:** Uso de import e from/import para conectar diferentes arquivos de código.
* **Bibliotecas Nativas:**
* random: Geração de valores aleatórios.
* math: Operações matemáticas avançadas (valor absoluto).
* datetime: Captura e formatação de datas.
* **Bibliotecas de Terceiros:**
* Faker: Criação de dados de teste (nomes, e-mails e cidades).
* **Lógica de Interação:** Implementação de loops while e condicionais if/elif/else para o controle do fluxo do jogo.

---

## 🏛️ Projeto: Programação Orientada a Objetos (Módulo 08)

Este módulo foi dedicado ao estudo da POO, focando na criação de sistemas modulares e reutilizáveis através de classes, objetos, herança e
gerenciamento de estados.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Classes e Objetos):** Criação da `classe Carro` para entender a estrutura de atributos `(marca, modelo, cor)` e métodos de ação, 
como o comportamento de buzinar.
* **Atividade 02 (Herança e Polimorfismo):** Implementação de uma `classe especializada CarroEletrico` que herda características da classe base 
e adiciona atributos específicos como autonomia de bateria.
* **Atividade 03 (Encapsulamento e Estados):** Desenvolvimento de uma `classe Celular` com métodos para alternar o status `(ligado/desligado)`
e uso do método especial `__str__` para representação textual do objeto.
* **Atividade Extra (Sistema de Biblioteca):** Um sistema completo de gerenciamento que utiliza a interação entre duas classes (Livro e Biblioteca)
para controlar acervos, realizar empréstimos e validar disponibilidades.

### 🛠️ Ferramentas Utilizadas
* **Paradigma POO:** Uso de Classes, Objetos e o método construtor `__init__`.
* **Herança:** Aplicação da função `super()` para reaproveitamento de lógica de classes pai.
* **Métodos Especiais:** Implementação do `__str__` para personalizar a exibição dos objetos em listas e prints.
* **Gestão de Estados:** Uso de variáveis booleanas para controlar o fluxo de disponibilidade `(True/False)`.
* **Lógica de Coleções:** Uso de listas internas para armazenar e percorrer múltiplos objetos dinamicamente.

---

## 👩‍🏭 Projeto: Tratamento de Erros (Módulo 09)

Este módulo foi dedicado ao estudo da resiliência de software, focando em como prever, capturar e tratar falhas para garantir que o sistema continue funcionando mesmo diante de entradas inesperadas.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Fundamentos do Try-Except):** Implementação de cálculos matemáticos seguros para tratar erros de divisão por zero e entrada
de dados inválidos (letras em vez de números).
* **Atividade 02 (Exceções Customizadas):** Criação da classe `SaldoInsuficienteError` para personalizar mensagens de erro em sistemas bancários,
indo além das exceções padrão do Python.
* **Atividade 03 (Validação de Dados):** Desenvolvimento de funções de proteção para garantir que entradas como idade e valores monetários sejam 
sempre números positivos e coerentes.
* **Atividade Extra (Sistema de Login e Segurança):** Um sistema de autenticação com limite de tentativas, utilizando exceções para controlar
acessos negados e bloqueios de segurança.

### 🛠️ Ferramentas Utilizadas
* **Blocos de Controle:** Uso de `try`, `except`, `else` e `finally` para gerenciar o fluxo de erro.
* **Exceções Personalizadas:** Criação de classes próprias herdando de `Exception` para regras de negócio específicas.
* **Comando Raise:** Lançamento manual de exceções para interromper execuções perigosas ou inválidas.
* **Sanitização de Input:** Uso de loops `while True` combinados com tratamento de erro para validar dados em tempo real.
* **Lógica de Segurança:** Implementação de contadores de tentativas e verificadores de credenciais.

---

## 🌐 Projeto: Introdução a APIs (Módulo 10)

Este módulo foi focado no aprendizado de como o Python se conecta com o mundo externo, utilizando a biblioteca `requests` para consumir APIs (Application Programming Interfaces), tratar dados recebidos em formato JSON e gerenciar erros de conexão de forma resiliente.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Verificação de Ambiente):** Configuração do ambiente no VS Code e validação da instalação do gerenciador de pacotes `pip` e da biblioteca `requests`.
* **Atividade 02 (Previsão do Tempo com OpenWeatherMap):** Integração com uma API real de clima para buscar dados meteorológicos globais, aplicando técnicas de autenticação via Chave de API (API Key).
* **Atividade 03 (Filtração e Formatação de Dados):** Extração seletiva de informações específicas do JSON bruto (como temperatura atual, sensação térmica e condições climáticas) e exibição organizada no terminal utilizando emoticons e réguas visuais.
* **Atividade 04 (Consumo Avançado - Buscador de Filmes no TMDB):** Desenvolvimento de um sistema completo que consome a API do The Movie Database para buscar filmes por título em tempo real, tratando textos longos com quebras de linha automáticas e convertendo formatos de datas internacionais.

### 🛠️ Ferramentas e Conceitos Aplicados
* **Biblioteca `requests`:** Uso do método `requests.get()` para realizar requisições HTTP do tipo GET a servidores externos.
* **Tratamento de Erros de Rede:** Implementação de blocos `try/except` específicos para capturar problemas de internet (`ConnectionError`), respostas de erro dos servidores (`HTTPError`) e proteção contra travamentos por lentidão usando o parâmetro `timeout`.
* **Manipulação de JSON:** Uso do método `.json()` para transformar dados brutos em dicionários Python nativos, navegando de forma segura através do método `.get()`.
* **Biblioteca `textwrap`:** Utilização da ferramenta nativa para formatar e ajustar sinopses longas dentro do limite visual do terminal.

---

## 🗄️ Projeto: Banco de Dados com SQLite (Módulo 11)

Este módulo foi focado na introdução ao armazenamento de dados persistentes, utilizando a biblioteca nativa `sqlite3` do Python para criar bancos de dados locais, estruturar tabelas relacionais e executar comandos SQL essenciais para manipulação de informações.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Criação de Tabela):** Configuração inicial de um banco de dados (`sistema.db`) e criação da tabela `Clientes`, definindo chaves primárias automáticas (`AUTOINCREMENT`) e restrições de integridade (`UNIQUE` e `NOT NULL`).
* **Atividade 02 (Operações CRUD):** Desenvolvimento de um sistema gerenciador interativo via terminal que implementa o ciclo completo do CRUD: Inserir (`INSERT`), Consultar (`SELECT`), Atualizar (`UPDATE`) e Deletar (`DELETE`) registros na tabela de clientes.
* **Atividade 03 (Consultas e Filtros SQL):** Exploração de consultas SQL avançadas utilizando o operador `LIKE` e caracteres curinga (`%`) para filtrar registros específicos, como buscar clientes por iniciais do nome ou por provedor de e-mail.
* **Desafio Extra (Gestor de Tarefas):** Criação de um utilitário completo de lista de tarefas integrado ao mesmo banco de dados, utilizando uma nova tabela (`Tarefas`) com controle automático de estados e status (`Pendente` / `Concluído`).

### 🛠️ Ferramentas e Conceitos Aplicados
* **Biblioteca `sqlite3`:** Uso de recursos nativos para conexão, execução de comandos por meio de objetos `cursor` e persistência de dados com `commit()`.
* **Linguagem SQL Básica:** Domínio de comandos fundamentais de DDL (Data Definition Language) e DML (Data Manipulation Language).
* **Prepared Statements (`?`):** Aplicação de boas práticas de segurança utilizando interrogações como marcadores de posição nas consultas para prevenir ataques de *SQL Injection*.
* **Tratamento de Exceções do Banco:** Captura de erros específicos de banco de dados, como `sqlite3.Error` e `sqlite3.IntegrityError` (para evitar cadastros duplicados).

---

## 🧪 Projeto: Testes Automatizados em Python (Módulo 12)

Este módulo foi dedicado ao desenvolvimento de testes automatizados, uma das práticas mais importantes da engenharia de software para garantir
a estabilidade, confiabilidade e o correto funcionamento do código diante de novas alterações.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Testes Unitários de Funções):** Criação de testes simples com o módulo nativo `unittest` para validar o comportamento isolado de funções matemáticas de soma.
* **Atividade 02 (Testes de Classes):** Criação de uma classe `Calculadora` e estruturação de cenários de teste complexos utilizando o método `setUp()` do `unittest` para instanciar objetos de forma limpa antes de cada verificação.
* **Atividade 03 (Tratamento de Exceções):** Implementação de testes robustos para validar entradas inválidas, utilizando `assertRaises` para garantir que o sistema dispare erros esperados (como impedir a divisão por zero).
* **Desafio Extra (Testes de API com Pytest):** Desenvolvimento de testes de integração para uma API construída em Flask utilizando o framework `pytest`, aplicando o conceito de `fixtures` para simular requisições HTTP (`GET`) e validar os códigos de status (`200 OK`) e retornos em JSON.

### 🛠️ Ferramentas e Conceitos Aplicados
* **Framework `unittest`:** Criação de classes de teste herdando de `unittest.TestCase` e uso de asserções como `assertEqual` e `assertRaises`.
* **Regras de Descoberta (`Discovery`):** Organização e nomenclatura padronizada de arquivos de teste (`test_*.py`) para execução em lote via terminal.
* **Framework `pytest`:** Instalação, configuração e uso de um dos frameworks de testes mais modernos do ecossistema Python.
* **Mocks de Cliente Flask (`test_client`):** Simulação de testes de integração em rotas de API sem a necessidade de levantar um servidor web real em ambiente de desenvolvimento.

---

## 🌐🌶️ Projeto: Desenvolvimento de APIs com Flask (Módulo 13)

Este módulo foi dedicado ao desenvolvimento de APIs (Application Programming Interfaces) robustas utilizando o framework Flask, 
conectando rotas HTTP ao banco de dados relacional SQLite para garantir a persistência de informações e aplicando conceitos de segurança e autenticação.

### ✨ O que foi desenvolvido?
* **Atividade 01 (Configuração Básica de Servidor):** Configuração de um ambiente Flask básico com a implementação de uma rota `GET /saudacao` que retorna uma mensagem de boas-vindas estruturada.
* **Atividade 02 (Requisições com JSON):** Desenvolvimento de uma rota `POST /cadastrar` para recebimento de dados e parâmetros enviados pelos clientes no formato JSON, aplicando conceitos de validação de payload.
* **Atividade 03 (Persistência no SQLite):** Integração do servidor Flask ao banco de dados relacional SQLite, implementando a criação automatizada de tabelas e persistindo os dados dos usuários enviados via requisições POST.
* **Desafio Extra (API Completa de Blog com Autenticação):** Desenvolvimento de uma API completa para um sistema de blog, contendo relacionamentos entre tabelas (usuários, posts e comentários), controle de gerenciamento de publicações e sistema de autenticação via Token seguro gerado dinamicamente para os usuários.

### 🛠️ Ferramentas e Conceitos Aplicados
* **Framework Flask:** Utilização de um dos microframeworks mais populares do Python para a criação rápida, modular e performática de servidores web e rotas de API.
* **Protocolo HTTP e Métodos:** Manipulação prática dos verbos HTTP mais importantes (`GET` para leitura e `POST` para criação de dados), compreendendo o uso dos códigos de status apropriados (`200 OK`, `201 Created`, `400 Bad Request` e `401 Unauthorized`).
* **Banco de Dados SQLite:** Modelagem de tabelas e execução de comandos SQL nativos (`INSERT INTO`, `SELECT`, `JOIN`) para salvar dados localmente em arquivos `.db`.
* **Autenticação Baseada em Token:** Conceito de segurança para proteção de endpoints, exigindo um token gerado no login através de Headers de Autorização (`Authorization`) para permitir operações de escrita (posts e comentários).

---

## 🔧 Como executar o projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/LaiSPaiv4/Lais-Codigo-Da-Transformacao-Python.git](https://github.com/LaiSPaiv4/Lais-Codigo-Da-Transformacao-Python.git)
