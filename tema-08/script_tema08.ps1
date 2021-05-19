Set-Location C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets

Write-Host "-- Excluindo datasets anteriores --"

Set-Location title.principals/
if(Test-Path -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\data.tsv -PathType Leaf) {
    Remove-Item -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\data.tsv
}

Set-Location ../

Set-Location title.basics/
if(Test-Path -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\data.tsv -PathType Leaf){
    Remove-Item -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\data.tsv
}

Set-Location ../

Set-Location name.basics/
if(Test-Path -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\data.tsv -PathType Leaf) {
    Remove-Item -Path C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\data.tsv
}

Set-Location ../

Write-Host "-- Fazendo o download de novos datasets --"

Start-BitsTransfer -Source "https://datasets.imdbws.com/title.principals.tsv.gz" -Destination "C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\title.principals.tsv.gz"
Start-BitsTransfer -Source "https://datasets.imdbws.com/title.basics.tsv.gz" -Destination "C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\title.basics.tsv.gz"
Start-BitsTransfer -Source "https://datasets.imdbws.com/name.basics.tsv.gz" -Destination "C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\name.basics.tsv.gz" 

Write-Host "-- Extraindo os arquivos dos datasets ---"
set-alias 7z "$env:ProgramFiles\7-Zip\7z.exe"

7z x -oC:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\ C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\title.principals.tsv.gz -r;
Remove-Item C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.principals\title.principals.tsv.gz

7z x -oC:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\ C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\title.basics.tsv.gz -r;
Remove-Item C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\title.basics\title.basics.tsv.gz

7z x -oC:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\ C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\name.basics.tsv.gz -r;
Remove-Item C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\datasets\name.basics\name.basics.tsv.gz

Write-Host "-- Rodando o tema 06 --"
Set-Location ../
Python main.py 

Write-Host "-- Fazendo o upload dos tweets para o bucket --"
Set-Location C:\Windows\System32
aws s3 sync C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-06\tweets s3://jt-dataeng-giovannagadelha/tema08/tweets/
Set-Location C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-08


