# flask : python언어를 활용한 마이크로 웹 프레임워크
# Flask : 서버 생성, 실행, route 관련 클래스
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World"
# __ <- 내장변수
# python은 모듈화가 간편하다!!
# 외부에서 만든 py을 import 사용할 수 있다!
# import할 때, 메모리에 올라가 있다!!
# 그런데, 개발자의 의도와는 달리
# 실행되면 안되는 구문 -> __name__ 을 활용!!
# __name__ => 직접 실행할 경우 __main__ 으로 바뀜!!
# 만약, import 당한 경우!! __name__ 그대로 있음!!
if __name__ == "__main__":
    app.run()
    