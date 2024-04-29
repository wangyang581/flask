from flask import Flask, render_template

app = Flask(__name__)


class User:
    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email


# 渲染模版
@app.route("/")
def hello_world():
    user = User(username="wang", email="xx@qq.com")
    person = {"name": "张三", "email": "zhangsan@qq.com"}
    return render_template("index.html", user=user, person=person)


@app.route("/blog/<int:blog_id>")
def blog_list(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="wang")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
