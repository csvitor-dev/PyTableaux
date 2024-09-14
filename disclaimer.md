<h1>Geral</h1>
<p>O projeto se trata de um executor do método tableaux.</p>
<p>Abaixo se encontra uma explicação geral dos pontos determinantes para o funcionamento desta aplicação.</p>

<h3>Pastas:</h3>
<b>file_manipulation: </b>Pasta unicamente feita para decompor os arquivos que forem a base para a execução.<br>
<b>inputs: </b>Pasta para os exemplos que devem ser passados para a execução em tableaux.<br>
<b>parser: </b>O decompor de fórmulas, abstraindo as formulas para a execução.<br>
<b>solver: </b>O solver do tableaux, transforma e aplica as regras de expansão.<br>
<b>utils: </b>As ultilidades para esta aplicação.<br>

<h3>Rota de execução:</h3>
1. Ao dar entrada nesta aplicação(inserindo os determiandos exemplos na pasta <b>inputs</b>), os '.tab' serão tratados, sendo postos em ordem com suas marcações. Em um exemplo, após o tratamento um arquivo ganharia mais ou menos este formato:<br>
<code>{'a': True, 'a->b': True}</code><br>
2. Após isto, uma árvore é contruída utilizando os dados e marcações do dicionário construído anteriormente. Realizando então um DFS, de forma recursiva, são abordados cada ramo. No caso de um ramo aberto, as execução para de imediato e retorna as valorações que resultam em um ramo aberto, caso contrário, retorna a um ponto anterior e executa novamente outra busca por um outro ramo.