from flask import Flask
from model import get_inference

app = Flask(__name__)

@app.route('/inference/<argument>')
def inference(argument):
    inference_data = get_inference(argument)
    return inference_data

if __name__ == '__main__':
    app.run(host='0.0.0.0')