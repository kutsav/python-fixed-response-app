import flask
import os
import logging

app = flask.Flask(__name__)

global app_response_code, app_response_text, app_port, app_methods
app_response_code = os.environ.get("RESPONSE_CODE",404)
app_response_text = os.environ.get("RESPONSE_TEXT","Not Found")
app_port = int(os.environ.get("APP_PORT",8000))
app_methods = [m.strip().upper() for m in os.environ.get("ALLOWED_METHODS", "GET,OPTIONS").split(",")]

#Health Check Path for app
@app.route('/health')
def health():
    return ('OK',200)

@app.route('/', defaults={'path': ''}, methods=app_methods)
@app.route('/<path:path>', methods=app_methods)
def catch_all(path):
    try:
        return (app_response_text, int(app_response_code))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=app_port)
