from flask import Flask

app = Flask(__name__)   # 实例化


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')
def index():  # put application's code here
    return 'This is index'

@app.route('/test')
def test():
    return "这是test页面"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
