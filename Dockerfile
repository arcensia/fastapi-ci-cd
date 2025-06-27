# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY ./app /app

# 실행 (main.py의 __main__ 실행)
CMD ["python", "main.py"]
