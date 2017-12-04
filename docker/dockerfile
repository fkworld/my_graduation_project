FROM python

MAINTAINER fengyong fkworld@foxmail.com

WORKDIR app
VOLUME ["/app"]
COPY requirements.txt /app/
RUN python3 -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt -i https://pypi.douban.com/simple

EXPOSE 80

CMD ["gunicorn","-w","4","-b","0.0.0.0:80","start:app"]