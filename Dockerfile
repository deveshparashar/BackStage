FROM python:3.13-alpine

EXPOSE 5000

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

WORKDIR /src

CMD ["python", "app.py"]

