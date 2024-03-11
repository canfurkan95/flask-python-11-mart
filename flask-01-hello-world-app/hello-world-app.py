from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head():
    return "hello world clarusway-17"

@app.route("/second")
def head_second():
    return "2. sayfa helelele"

@app.route("/third")
def head_uc():
    return "3. sayfa heleddıufhewıbjhele"

@app.route("/forth/<string:id>")
def forth(id):
    return f"bu sayfanın id'si {id}"


if __name__ == '__main__':

    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8081)