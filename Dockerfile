# Python 3.12 기반 이미지
FROM python:3.12

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치를 위해 requirements.txt 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 코드 복사
COPY . .

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1