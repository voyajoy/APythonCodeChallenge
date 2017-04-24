FROM python:3.4.6-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /pcc
WORKDIR /pcc
ADD ./source/requirements.txt /pcc/
ADD ./source/constraints.txt /pcc/
RUN pip install -r requirements.txt -c constraints.txt
ADD ./source/ /pcc/
