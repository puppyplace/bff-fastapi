FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

RUN ls

RUN pip install -r ./requirements.txt
