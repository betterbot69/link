from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'mbh_movies_bot'


if __name__ == "__main__":
    app.run()
