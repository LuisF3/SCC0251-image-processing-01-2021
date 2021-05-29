- O enunciado e proposta do trabalho 4 podem ser encontrados no arquivo A04_recovery_and_fourier.pdf.
- As imagens de input e de refências podem ser encontradas na pasta InputImages
- Os inputs de cada caso de teste juntamente com os outputs esperados estão na pasta TestCases

O código pode ser encontrado no arquivo jupyter t4.ipynb. Caso queira executar o programa para os casos de teste, basta executar o comando a baixo de dentro do diretório TestCases

for i in {1..8}; do printf "$i:\nmine: ";python3 t4.py < ../TestCases/case$i.in;printf "correct: ";cat ../TestCases/case$i.out;done;

Observe que alterações realizadas no t4.ipynb precisam ser sincronizadas no t4.py. Isso pode ser feito baixando o notebook como .py.

Nesse trabalho 4 os erros estão um pouco maiores pois os outputs oficiais estão utilizando desvio padrão para o cálculo das variáveis dispn e displ, entretanto, o correto é utilizar a variância. Apesar das diferenças nos erros, o threshold limite foi respeitado e as respostas estão validas.  