FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y supervisor

COPY . /app/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
