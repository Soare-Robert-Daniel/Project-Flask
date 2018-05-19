FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app

WORKDIR /app
ENV FLASK_APP main.py
ENV FLASK_DEBUG 1
ENV HTTP_PROXY "http://0.0.0.0:80"
ENV HTTPS_PROXY "https://0.0.0.0:80"

CMD ["python", "main.py"]
