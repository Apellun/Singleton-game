FROM python:3.9-slim-bullseye

WORKDIR /game

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY ./game .
ENV FLASK_APP=app.py
CMD flask run -h 0.0.0.0 -p 5000