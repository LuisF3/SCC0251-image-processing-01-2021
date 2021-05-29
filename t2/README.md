- O enunciado e proposta do trabalho 2 podem ser encontrados no arquivo T02_realce_superresolucao_especificação.pdf.
- As imagens de input e de refências podem ser encontradas na pasta ImagensParaTestes
- Os inputs de cada caso de teste juntamente com os outputs esperados estão na pasta CasosDeTeste

O código pode ser encontrado no arquivo jupyter t2.ipynb. Caso queira executar o programa para os casos de teste, basta executar o comando a baixo de dentro do diretório ImagensParaTestes

for i in {1..8}; do printf "$i:\nmine: ";python3 t2.py < ../CasosDeTeste/case0$i.in;printf "correct: ";cat ../CasosDeTeste/case0$i.out;done;

Observe que alterações realizadas no t2.ipynb precisam ser sincronizadas no t2.py. Isso pode ser feito baixando o notebook como .py.