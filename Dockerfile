FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x /app/entrypoint.sh


EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]

