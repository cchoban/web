FROM python:3.7.1

WORKDIR /tmp
RUN mkdir /backend
RUN git clone https://github.com/cchoban/web.git -b dev
WORKDIR /tmp/web
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN mkdir /var/log/gunicorn
WORKDIR /tmp
RUN mv web/* /backend/
WORKDIR /backend
ENV STATICFILES_DIR=/usr/src/app/static
ENV MEDIAFILES_DIR=/usr/src/app/media
EXPOSE 8080
WORKDIR /backend/src
