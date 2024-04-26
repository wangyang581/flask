from flask import Flask

# __name__: 代表当前demo_1.py这个模块
# 1.以后出现bug，可以帮助我们快速定位
# 2.对于寻找板块文件，有一个相对路径
app = Flask(__name__)

# 创建一个路由和视图函数的映射
@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()
