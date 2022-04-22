FROM python:3.10

RUN mkdir /code
WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code/src
ENV DJANGO_SETTINGS_MODULE settings

# Install during build phase
# RUN (curl -Ls https://cli.doppler.com/install.sh || wget -qO- https://cli.doppler.com/install.sh) | sh

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

# Executa o script de inicialização
ENTRYPOINT ["./start.sh"]
# ENTRYPOINT ["doppler", "run", "--", "./start.sh"]
