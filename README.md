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
* **Modulo_06/**: Contém o desafio prático Manipulação de Arquivos.
* **Modulo_07/**: Contém o desafio prático Modularização e Bibliotecas Externas.
* **Modulo_08/**: Contém o desafio prático Programação Orientada a Objetos.
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

## 🔧 Como executar o projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/LaiSPaiv4/Lais-Codigo-Da-Transformacao-Python.git](https://github.com/LaiSPaiv4/Lais-Codigo-Da-Transformacao-Python.git)
