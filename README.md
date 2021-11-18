# Atividade Uninter

Atividade da disciplina de Lógica de Programação na Uninter


## Requisitos pessoais

 - Observar a condicionante pessoal para realizar cada teste
 - Realizar os testes e seus registros para envio a disciplina
 - Gerar todo o documento para envio conforme especificação da atividade

## Metodologia de Correção

- Apresentar seu algoritmo completo, indentado e organizado; (Básico e obrigatório em toda produção de código)
- Explicar seu código através de comentários;
- Colocar uma IMAGEM com o terminal rodando e mostrando o que cada exercício pede.

## 1 Exercício: Ensino por faixa etária

A ampliação do Ensino Fundamental para nove anos de duração, tornou a matrícula da criança obrigatória a partir dos seis anos de idade. Implemente um programa que fornecidos
o nome e a idade de um criança classifique-a em uma das etapas de ensino.

### Classificação

| Ensino                | Faixa Etária |
| --------------------- | ------------ |
| Educação Infantil     | 1 a 5 anos   |
| Ensino Fundamental I  | 6 a 10 anos  |
| Ensino Fundamental II | 11 a 14 anos |
| Ensino médio          | > 15 anos    |

### Funções necessárias conforme escopo

- Receber nome
- Receber idade
- Realizar classificação
- Encerrar programa


## 2 Exercício: Codificando nomes

O programa deve imprimir na tela o nome convertido

### Codificação de conversão

| Letra | Código |
| :---: | :----: |
|   A   |   @    |
|   E   |   &    |
|   I   |   !    |
|   O   |   #    |
|   U   |   *    |

### Funções necessárias conforme escopo
- Converte o nome para UpperCase
- Codifica o nome
- Exibe nome convertido e o codificado

## 3 Exercício:

Implementar um jogo que é popular entre as crianças: um hotel onde os hóspedes têm algumas restrições quanto a localização de seu quarto.
O jogo é composto por 4 fases, onde cada fase (a partir da fase 2) só é desbloqueada se a anterior for concluída com êxito.

### Regras do jogo
- O rato não pode ficar ao lado do gato.
- O cão não pode ficar ao lado do osso.
- O gato não pode ficar ao lado do cão.
- O queijo não pode ficar ao lado do rato

### Definições

| Letra | Equivalência |
| :---: | ------------ |
|   G   | GATO         |
|   C   | CÃO          |
|   R   | RATO         |
|   O   | OSSO         |
|   Q   | QUEIJO       |
|   *   | Indisponível |
|   _   | Vazio        |

#### Matriz dos quartos

[1 2 3 4]
[5 6 7 8]


### Requisitos

 - Ao término de cada fase o jogador deverá receber uma mensagem informando se teve êxito ou não na sua resposta.
   - Se não teve êxito, o programa se encerra mostrando a mensagem: “Você perdeu!”.
   - Se teve exito a próxima fase é desbloqueada.
 - Ao terminar a ultima fase com exito uma mensagem de “Você ganhou!” é mostrada na tela.

#### Fase 1

O jogador deve alocar o RATO e o GATO na seguinte matriz que representa os
quartos.

[* * _ G]
[R _ * *]

#### Fase 2

Na segunda fase o jogador deve alocar : CÃO, CÃO E OSSO.

[_ * * *]
[* C _ _]

#### Fase 3

Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO.

[_ * * *]
[_ G _ *]

#### Fase 4

Na fase 4, o jogador deverá alocar: QUEIJO, QUEIJO, OSSO.

[_ _ _ *]
[* R * *]

## 4 Exercício: Inscrições com voucher

Uma escola de cursos de TI oferece vouchers para que os participantes possam assistir algumas aulas gratuitas de Python. Para isso o participante que deseja assistir as aulas gratuitas desse curso específico, deve fazer uma inscrição para receber o voucher.
Implemente um programa que armazene as inscrições para o curso.

### Requisitos

- O programa deverá armazenar para cada inscrição:
  - Um código único para o voucher
  - Nome
  - Email
  - Telefone
  - Curso
- Menu de opções ao usuário:
  - 1- Inscrição:
    - O usuário deverá ser capaz de informar todos os dados da inscrição.
    - O código do voucher deve ser preenchido automaticamente pelo sistema.
    - O usuário não deve ter a opção de alterar esse código.
  - 2- Visualizar inscrição:
    - O programa deverá imprimir, na tela, para cada reserva, todos os dados dessa inscrição.
    - Caso nenhuma inscrição tenha sido cadastrada ao selecionar essa opção, o programa deverá exibir a mensagem “nenhuma inscrição cadastrada”.
  - 3- Encerrar:
    - O programa se encerra.
  - Opção inexistente:
    - Mensagem de erro requisitando opção válida