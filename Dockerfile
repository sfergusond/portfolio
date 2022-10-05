FROM python:3.10.6-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN apk add g++
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput

# copy project
COPY . .

EXPOSE 8080

CMD ["gunicorn", "--bind", ":8080", "portfolio.wsgi"]