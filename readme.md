# 개요
본 프로젝트는 시험 일정 예약 시스템을 위한 RESTful API를 제공합니다. 설계 및 관련 아키텍처는 github wiki를 통해 확인해주시면 정말 감사하겠습니다 :)
- github wiki : [Github Wiki 바로 가기](https://github.com/rrosiee/reservation-server/wiki)

# 요구사항
- Python 3.12+
- Django
- Django REST framework
- drf-yasg (Swagger 문서 자동 생성)

# 로컬 실행 방법

로컬에서 해당 서버를 실행하는 방법은 **docker**를 이용한 방법, **local에 직접 데이터베이스**를 생성하는 방법 두 가지가 있습니다.

### 1. (권장)Docker를 이용한 방법

1. Docker Desktop 설치 및 실행 : [다운로드 링크](https://www.docker.com/products/docker-desktop/)
2. docker-compose 빌드

        $ docker-compose build
3. docker-compose 실행

        $ docker-compose up
4. api swagger문서 접속 : [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
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
7. api swagger문서 접속 : [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

## Swagger 문서
Swagger UI를 통해 API 문서를 확인할 수 있습니다.
```bash
# 개발 서버 실행 후 접속
http://localhost:8000/api/docs/
```

## API 엔드포인트

### 인증 API
| 메소드 | 엔드포인트       | 설명          |
|--------|----------------|--------------|
| POST   | `/api/auth/login/` | 사용자 로그인 |
| POST   | `/api/auth/logout/` | 사용자 로그아웃 |

### 사용자 API
| 메소드 | 엔드포인트      | 설명          |
|--------|---------------|--------------|
| GET    | `/api/user/`  | 사용자 정보 조회 |
| PUT    | `/api/user/`  | 사용자 정보 수정 |

### 예약 API
| 메소드 | 엔드포인트         | 설명            |
|--------|-----------------|----------------|
| POST   | `/api/reservation/` | 새로운 예약 생성 |
| GET    | `/api/reservations/` | 예약 목록 조회 |

### 관리자 예약 API
| 메소드 | 엔드포인트               | 설명               |
|--------|----------------------|------------------|
| GET    | `/api/admin/reservations/` | 모든 예약 조회 (관리자) |
| DELETE | `/api/admin/reservation/{id}/` | 예약 삭제 (관리자) |

### 일정 API
| 메소드 | 엔드포인트       | 설명           |
|--------|--------------|-------------|
| GET    | `/api/schedules/` | 일정 목록 조회 |

