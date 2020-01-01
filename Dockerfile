FROM python:3.6.1-alpine

MAINTAINER Nazmul Islam "md.nazmul@northsouth.edu"
LABEL Author="Nazmul Islam"
LABEL E-mail="md.nazmul@northsouth.edu"

WORKDIR /flask-redis-rest
ADD . /flask-redis-rest

EXPOSE 5000:5000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD ["app.py"]