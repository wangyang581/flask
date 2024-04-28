from flask import Flask

app = Flask(__name__)

# url:网站是由协议+网址部分是域名：端口号，http[80]/https[443]://www.qq.com/
# URL与视图：path与视图

@app.route('/')
def hello_world():
    return 'hello  world'

@app.route('/profile')
def profile():
    return '我是个人中心'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
