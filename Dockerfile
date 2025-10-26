
FROM efreidevopschina.azurecr.io/cache/library/python:3.11-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY src ./src
COPY tests ./tests


EXPOSE 8000


CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
