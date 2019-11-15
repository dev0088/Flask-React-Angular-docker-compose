# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7
 
WORKDIR /flask-app

COPY requirements.txt /flask-app/requirements.txt
RUN pip install -r requirements.txt

COPY . /flask-app/
RUN cd /flask-app/

EXPOSE 5000

CMD ["python", "hello.py"]
