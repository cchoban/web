FROM python:3.7

WORKDIR /app/

EXPOSE 8000
COPY ./ /app/
RUN pip install -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_10.x  | bash -
RUN apt-get install -y nodejs
RUN npm install
ADD . /code/