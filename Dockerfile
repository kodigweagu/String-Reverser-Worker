FROM python:latest
WORKDIR /app
COPY ./app /app
COPY requirements.txt /app
RUN pip install pip --upgrade && pip install -r /app/requirements.txt
CMD ["python", "./main.py" ]