import flask
import os
import logging

app = flask.Flask(__name__)

global app_response_code, app_response_text
app_response_code = os.environ.get("RESPONSE_CODE",404)
app_response_text = os.environ.get("RESPONSE_TEXT","Not Found")

#Health Check Path for app
@app.route('/health')
def health():
    return ('OK',200)

@app.route('/<path:path>', methods=['GET'])
def s3_client(path):
    try:
        return (app_response_text,int(app_response_code))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')
