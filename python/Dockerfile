FROM python:latest

WORKDIR /usr/app/src
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["gunicorn", "--workers=3", "-b 0.0.0.0:8000", "main:app"]
