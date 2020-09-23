FROM python:3.7-alpine
LABEL maintainer Cristian Favaro

#NAO ENTENDI ISSO MUITO BEM
ENV PYTHONUNBUFFERED 1

#copia daqui do local e joga tudo no requi no docker
COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt 

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app

#copiei o arquivo local para o docker. 
COPY ./app /app


#usuario para usar a aplicacao 
#-d é para apenas rodar as aplicacoes. nao instalar por exemplo. 
#isso é para questao de seguranca. evitar usar o root account.
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user

RUN chown -R user:user /vol/
RUN chown -R 755 /vol/web

USER user 
