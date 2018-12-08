FROM python:3.7

WORKDIR /app/

EXPOSE 8000
COPY ./ /app/
RUN pip install -r requirements.txt
ADD . /code/
