from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    sample_string = " Hello Mini Kube";
    return render_template('index.html', str=sample_string)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
