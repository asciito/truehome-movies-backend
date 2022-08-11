FROM python:3-alpine

COPY ["requirements.txt", "/code/"]

COPY [".", "/code/"]

WORKDIR /code/

RUN apk add gcc musl-dev mariadb-connector-c-dev

RUN pip install -r requirements.txt

ENV ENV=/etc/profile

RUN echo 'alias django="python -m manage $@"' >> "$ENV"

EXPOSE 8000

CMD ["python", "-m", "manage", "runserver", "0.0.0.0:8000"]
