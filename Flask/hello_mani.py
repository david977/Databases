from flask import Flask

app = Flask(__name__)

@app.route("/")
def name():
    return 'My name is Mani Bhattari'

if __name__ == '__main__':
     app.run()
