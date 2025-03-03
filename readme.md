# 로컬 실행 방법

로컬에서 해당 서버를 실행하는 방법은 **docker**를 이용한 방법, **local에 직접 데이터베이스**를 생성하는 방법 두 가지가 있습니다.

### 1. (권장)Docker를 이용한 방법

1. Docker Desktop 설치 및 실행 : [다운로드 링크](https://www.docker.com/products/docker-desktop/)
2. docker-compose 빌드

        $ docker-compose build
3. docker-compose 실행

        $ docker-compose up
4. api swagger문서 접속 : [http://localhost:8000/docs](http://localhost:8000/docs)
5. (선택) 종료

        $ docker-compose down

### 2. Local에서 실행

1. postgresql 17 버전 설치 : [다운로드 링크](https://www.postgresql.org/download/)
2. terminal에서 db생성

        $ createdb reservation
3. python 3.12 버전 설치 : [다운로드 링크](https://www.python.org/downloads/release/python-3129/)
4. 해당 프로젝트의 터미널에서 가상환경 생성 및 의존성 설치

        $ python3 -m venv .venv
        $ source .venv/bin/activate
        $ pip install -r requirements.txt
5. 데이터 마이그레이션

        $ python3 manage.py migrate
6. 서버 실행

        $ python3 manage.py runserver
7. api swagger문서 접속 : [http://localhost:8000/docs](http://localhost:8000/docs)