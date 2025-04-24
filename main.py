from flask import Flask


app = Flask(__name__)

@app.route('/hello')
def hello():
    print('heloo')


    return



app.run()