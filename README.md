# Jogo da Velha Minimax

## Intro
Este jogo tem como objetivo proporcionar uma experiência divertida e educativa sobre inteligência artificial e lógica de programação. Os jogadores podem competir contra o computador ou entre si, testando suas habilidades e táticas para alcançar a vitória no tabuleiro 3x3.

O projeto é de código aberto, e você é bem-vindo para contribuir, relatar problemas e sugestões. Divirta-se jogando e explorando os conceitos de inteligência artificial aplicados ao jogo da velha!

## Preview
<p align="center">
	<img src="preview/jogando.gif"></img>
</p>

## Algoritimo
Abaixo, o melhor movimento está na posição do meio porque o valor máximo está no 2º nó à esquerda.
<p align="center">
	<img src="preview/tic-tac-toe-minimax-game-tree.png"></img>
</p>

Observe que a profundidade é igual aos movimentos válidos no tabuleiro.

Árvore de jogo simplificada:
<p align="center">
	<img src="preview/simplified-g-tree.png"></img>
</p>

A árvore deste exemplo tem 11 nós. A árvore completa do jogo tem 549.946 nós! Você pode testá-lo colocando uma variável global estática em seu programa e incrementando-a para cada chamada de função minimax por vez, fazendo um tipo de cache e melhorando muito a performance do seu algoritmo.
