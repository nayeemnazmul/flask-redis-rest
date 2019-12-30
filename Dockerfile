FROM python:3.6.1-alpine
LABEL Author="Nazmul Islam"
LABEL E-mail="md.nazmul@northsouth.edu"
WORKDIR /flask-redis-rest
ADD . /flask-redis-rest
RUN pip install -r requirements.txt
RUN apt-get install redis-server
RUN redis-server
ENTRYPOINT [ "python" ]
CMD ["app.py"]