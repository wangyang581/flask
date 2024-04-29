from flask import Flask, render_template

app = Flask(__name__)


# 渲染模版
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/blog/<int:blog_id>")
def blog_list(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="wang")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
