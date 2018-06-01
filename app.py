import time
import flask_monitoringdashboard as dashboard

from flask import Flask

app = Flask(__name__)
dashboard.config.version = '3.0'
dashboard.bind(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def delayed_hello_world():
    time.sleep(2)
    return '[Delayed] Hello World!'


if __name__ == '__main__':
    app.run()
