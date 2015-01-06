# -*- coding: utf-8 -*-
# 위 부분은 파이썬 문서 내에서 한글사용이 가능하게 인코딩 해주는 부분입니다
from flask import Flask
# flask 라는 모듈에서 Flask라는 클래스를 가져다 쓰겠다는 뜻입니다.
app = Flask(__name__)
# codrugFlaskExam.py 라는 파일의 이름 '__name__' 을 인자로 받아서 이 파일을 플라스크 어플로 만들겠다는 뜻이고 그 이름은 app

@app.route('/')
# 우리가 만들 주소 '예시: http://codrug.net/ 혹은 http://localhost:8000/' 에 그냥 접속했을 때, 즉 뒤 주소가 아무것도 안붙은 주소를 라우팅 함
def hello_world():
# '/'라는 주소에 들어가면 hello_world라는 함수를 실행합니다
    return 'Hello World!'
# 그 함수의 리턴값은 'Hello World'

#김재윤님이 참여하였습니다.

@app.route('/hello2')
def hello():
    return "Hello Flask!"


app.run()

#
# # 이 부분은 어플이 이 파일 안에서 실행될따면 어플을 실행한다는 부분인데, 다른곳에서 import codrugFlaskExam 이런식으로 불러다 썼을때는 실행이 안되게 함
# if __name__ == '__main__':
#     app.run()
