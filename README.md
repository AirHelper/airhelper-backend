# 에어소프트 게임 관리 시스템

## 프로젝트 구성하기
'''
docker-compose up
'''


## 프로젝트 구성 후에 아래 주소로 접속한다.
> 127.0.0.1:8000

장고 페이지가 뜨면 정상!


### EOF 오류발생시
1. notead++ 설치
2. start-server.sh를 notepad++로 연다.
3. 컨트롤+A로 모두 블럭 처리
4. 편집->줄의 끝문자 변환-> UNIX 또는 Linux로 변경
5. 재빌드


## 개발 방법
1. PEP8 코딩 컨벤션을 준수한다. 
> 파이참에서 설정 가능

2. features/기능명 브랜치를 생성하여 작업한다.
> 로그인의 경우 features/oauth 또는 features/kakao 등등..

3. 커스텀 유저 모델 생성한다.
> 참고자료 드림 - Notion->개발란->참고문헌 파일 확인

4. 한앱에 하나의 기능을 넣는다.
'''
docker-compose exec django python manage.py startapp 앱명
'''

5. 본인이 만든 기능에 대해 README.md를 작성한다.



#### 각종 명령어들
1. DB 마이그레이션
> docker-compose exec django python manage.py makemigrations <app-name>

2. 마이그레이션 적용
> docker-compose exec django python migrate <app-name>

3. 마이그레이션 적용 현황
> docker-compose exec django python manage.py showmigrations <app-name>

4. 관리자 계정 생성
> docker-compose exec django python manage.py createsuperuser

5. 테스트 수행
> docker-compose exec django pytest 'appname'

6. 새 앱 만들기
> docker-compose exec django python manage.py startapp 'appname'

7. 테스트 커버리지 시각화
> docker-compose exec django coverage run manage.py test
> docker-compose exec django coverage html
