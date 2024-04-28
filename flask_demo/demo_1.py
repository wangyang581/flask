from flask import Flask

# __name__: 代表当前demo_1.py这个模块
# 1.以后出现bug，可以帮助我们快速定位
# 2.对于寻找板块文件，有一个相对路径
app = Flask(__name__)


# 创建一个路由和视图函数的映射
@app.route("/")
def hello_world():
    return "WHICXK  world"


# 1.debug模式：开启debug模式后，只要修改代码后保存，就会自动重新加载，不需要手动重启项目
# 如果开发的时候出现bug，开启debug模式后，在浏览器上就可以看到出错的信息

# 2.修改host：host修改为0.0.0.0，就可以让别的电脑通过IP地址访问该电脑上的flask项目

# 3.修改port端口号：可以通过端口号运行不同的flask程序
#   在其他项目占用端口号时可以通过port修改监听端口号

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
