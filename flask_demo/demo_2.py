from flask import Flask, request

app = Flask(__name__)

# url:网站是由协议+网址部分是域名：端口号，http[80]/https[443]://www.qq.com/
# URL与视图：path与视图


@app.route("/")
def hello_world():
    return "hello  world"


# 定义无参数的URL
@app.route("/profile")
def profile():
    return "我是个人中心"


# 定义有参数的url,可以限制参数类型，定义方式是将参数固定到path中
# 参数类型可以是string，int，float，path，uuid，any（any可以是上述类型中的任何一个）
@app.route("/blog/<int:blog_id>")
def blog_list(blog_id):
    return "你所访问的博客是：%s" % blog_id


# 查询字符串方式传参
# book/list:该接口为书的第一页数据
# book/list?page=2:这种方式可以获取第二页数据，http协议规定用?传参
@app.route("/book/list")
def book_list():
    # arguments:参数
    # request.args:类字典类型
    page = request.args.get("page", default=1, type=int)
    return "您获取的是第{}页".format(page)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
