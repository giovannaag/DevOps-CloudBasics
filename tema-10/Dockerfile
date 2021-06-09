FROM python:3

RUN mkdir /Tema10
WORKDIR /Tema10

RUN pip install awscli

COPY . /Tema10/

RUN bash aws_credentials.sh

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
