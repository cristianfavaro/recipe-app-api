FROM python:3.7-alpine
LABEL maintainer Cristian Favaro

#NAO ENTENDI ISSO MUITO BEM
ENV PYTHONUNBUFFERED 1

#copia daqui do local e joga tudo no requi no docker
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt 

RUN mkdir /app
WORKDIR /app

#copiei o arquivo local para o docker. 
COPY ./app /app


#usuario para usar a aplicacao 
#-d é para apenas rodar as aplicacoes. nao instalar por exemplo. 
#isso é para questao de seguranca. evitar usar o root account.
RUN adduser -D user
USER user 
