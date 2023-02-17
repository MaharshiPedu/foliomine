FROM nikolaik/python-nodejs:python3.8-nodejs19-slim

ENV DockerHOME=/home/app

RUN mkdir -p ${DockerHOME}

WORKDIR ${DockerHOME}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip

COPY . ${DockerHOME}

RUN pip install -r requirements.txt

EXPOSE 8000
RUN cd mysite
CMD python manage.py runserver 0.0.0.0:8000; python manage.py tailwind start