- O enunciado e proposta do trabalho 3 podem ser encontrados no arquivo T03_filtragem_especificação.pdf.
- As imagens de input e de refências podem ser encontradas na pasta CasosDeTeste
- Os inputs de cada caso de teste juntamente com os outputs esperados estão na pasta ImagensParaCasosDeTeste

O código pode ser encontrado no arquivo jupyter t3.ipynb. Caso queira executar o programa para os casos de teste, basta executar o comando a baixo de dentro do diretório ImagensParaCasosDeTeste

for i in {1..8}; do printf "$i:\nmine: ";python3 t3.py < ../CasosDeTeste/$i.in;printf "correct: ";cat ../CasosDeTeste/$i.out;done;

Observe que alterações realizadas no t3.ipynb precisam ser sincronizadas no t3.py. Isso pode ser feito baixando o notebook como .py.