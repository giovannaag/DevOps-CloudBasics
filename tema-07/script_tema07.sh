#!/bin/bash

cd ~/Desktop/DevOps-CloudBasics/tema-06/datasets

echo "-- Excluindo datasets anteriores --"

cd title.principals/
if [ -e data.tsv ]; then
    rm data.tsv
fi
cd -

cd title.basics/
if [ -e data.tsv ]; then
    rm data.tsv
fi
cd -

cd name.basics/
if [ -e data.tsv ]; then
    rm data.tsv
fi
cd -

echo  $'\n-- Fazendo o download de novos datasets --'

wget -P title.principals https://datasets.imdbws.com/title.principals.tsv.gz
wget -P title.basics https://datasets.imdbws.com/title.basics.tsv.gz
wget -P name.basics https://datasets.imdbws.com/name.basics.tsv.gz

echo $'\n-- Extraindo e renomeando os arquivos dos datasets --'

cd title.principals/
gunzip title.principals.tsv.gz
mv title.principals.tsv data.tsv
cd - 

cd title.basics/
gunzip title.basics.tsv.gz
mv title.basics.tsv data.tsv
cd -

cd name.basics/
gunzip name.basics.tsv.gz
mv name.basics.tsv data.tsv
cd -

echo $'\n-- Rodando o tema 06 --'

cd ../
python3 main.py

echo $'\n-- Fazendo o upload dos tweets para o bucket --'
aws s3 sync tweets/ s3://jt-dataeng-giovannagadelha/tema07/tweets/ 

