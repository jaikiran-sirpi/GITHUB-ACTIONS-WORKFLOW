FROM python:3.13-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir  --target=/app  -r requirements.txt
COPY . .
FROM gcr.io/distroless/python3 
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 8000
CMD ["-m","uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]
