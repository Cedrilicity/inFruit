import threading

from flaredantic import FlareTunnel, FlareConfig
from flask import Flask, jsonify, url_for, render_template, request
from fruits import fruits

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getFruit', methods=['GET'])
def getFruit():
    global fruit
    if request.method == 'GET':
        fruit = request.args['fruit']
    for item in fruits:
           if item["name"].lower() == fruit.lower():
                return jsonify(item)

    return jsonify({"error": "Fruit not found"})

def run_tunnel():
    config = FlareConfig(
        port=5000,
        verbose=True  # Enable logging for debugging
    )
    with FlareTunnel(config) as tunnel:
        print(f"Flask app available at: {tunnel.tunnel_url}")
        app.run(port=5000)


if __name__ == '__main__':
    threading.Thread(target=run_tunnel).start()