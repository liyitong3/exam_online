from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico")

@app.route('/')
def hello_world():
    return render_template('default.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
