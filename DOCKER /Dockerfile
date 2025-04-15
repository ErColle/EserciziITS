FROM python:3.11.11

COPY python_requirements.txt /
RUN pip install -r python_requirements.txt

RUN mkdir /app
COPY app.py /app/
WORKDIR /app