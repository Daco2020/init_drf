# DRF 초기세팅 파일 입니다.
### 다음 사항이 세팅되어 있습니다.
- cors 세팅
- pymysql 세팅
- logging 세팅
*설치된 라이브러리는 requirements를 참고해주세요.
*추가하면 좋은 공통 라이브러리는 추가 후 PR요청해주세요.


### 다음 순서를 따라해주세요.

1. 레포를 깃 클론을 받아주세요.
2. 가상환경을 만들어주세요. (파이썬은 3.8 버전입니다)
3. requirements.txt 를 이용하여 라이브러리를 설치해주세요.
4. project_name/settings.py 에서 DATABASE 에 데이터베이스 이름을 넣어주세요. (데이터 베이스가 없다면 생성 후 이름을 기재해주세요)
5. python manage.py runserver 으로 서버를 여러어주세요.
6. http://127.0.0.1:8000/users/ping  해당 url에서 반환메시지(pong)가 정상적으로 나오는지 확인해주세요.
7. 서버가 정상작동한다면 'project_name'의 이름을 본인의 프로젝트 명으로 바꿔주세요!
   (VSC기준, shift + command + f 를 누르면 모든 파일의 'project_name'을 찾아서 바꾸실 수 있습니다!)

# 수정 보완이 필요한 사항은 언제든지 깃헙 코멘트나 슬랙 디엠 남겨주세요!