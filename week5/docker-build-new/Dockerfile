FROM python:3.8.12-slim

RUN apt update -y && apt install -y python3.9

RUN rm /usr/local/bin/python && ln -s /usr/bin/python3.9 /usr/local/bin/python

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

#Since we do not want to create virtual env but install system wide and deploy it we use the following
RUN pipenv install --system --deploy

COPY ["week5-predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "week5-predict:app"]
