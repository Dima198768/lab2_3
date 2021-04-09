from flask import Flask
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
  return 'localhost'
  
@app.route('/echo/<text>')
def echo(text):
    return "You use echo with text: " + text

@app.route('/login/<login>/<password>')
def login(login, password):
    res = login == "dima" and password == "123"
    if(res):
        return "logined"
    else:
        return "Bad credencials"

app.run()