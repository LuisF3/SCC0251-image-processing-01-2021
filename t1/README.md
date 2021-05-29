- O enunciado e proposta do trabalho 1 podem ser encontrados no arquivo T01_geração_de_imagens_especificação.pdf.
- As imagens de refências podem ser encontradas na pasta imagens_de_referência
- Os inputs de cada caso de teste juntamente com os outputs esperados estão na pasta casos_de_teste

O código pode ser encontrado no arquivo jupyter t1.ipynb. Caso queira executar o programa para os casos de teste, basta executar o comando a baixo de dentro do diretório imagens_de_referência

for i in {1..5}; do printf "$i:\nmine: ";python3 t1.py < ../casos_de_teste/case0$i.in;printf "correct: ";cat ../casos_de_teste/case0$i.out;done;

Observe que alterações realizadas no t1.ipynb precisam ser sincronizadas no t1.py. Isso pode ser feito baixando o notebook como .py.