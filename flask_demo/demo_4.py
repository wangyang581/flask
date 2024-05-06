from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


class User:
    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email


# 创建一个路由和视图函数的映射
@app.route("/")
def hello_world():
    return "WHICXK  world"


@app.route("/filter")
def filter():
    user = User(username="wang", email="xx@qq.com")
    mytime = datetime.now()
    return render_template("filter.html", user=user, mytime=mytime)


def datatime(value, format="%Y-%m-%d %H:%M"):
    return value.strftime(format)
app.add_template_filter(datatime, "dformat")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

