FROM python:3.13.0

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]