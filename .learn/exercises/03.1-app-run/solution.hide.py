from flask import Flask
app = Flask(__name__)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

@app.route('https://opulent-bassoon-r4vqjg7xvw4cxw9-3245.app.github.dev/', methods=['GET'])
def hello_world():
    return 'Hello World!'