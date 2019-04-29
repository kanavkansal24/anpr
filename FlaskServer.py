from flask import Flask, jsonify, make_response, request
import base64
import Run
from MongoServer import *


app = Flask(__name__)


@app.route('/')
def index():
    return "Server says hello!"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/upload', methods=['POST'])
def uploadjson():
    print (request.is_json)
    content = request.get_json()
    print("ayy")
    print (content)
    print(content['base64'])
    return make_response(jsonify({'imageBLOB': content['base64']}), 200)


@app.route('/uploadimg', methods=['POST'])
def frecog():
    connection= connectToMongo()
    #print (con)
    content = request.get_json()
    img_data = content['ImageBLOB']
    imgdata = base64.b64decode(img_data)
    filename = 'ImagesFromApp/Image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    text = Run.imgToText(filename)
    #print type(text)
    print str(text)
    if (text==[]):
        data2 = {"ayy": "No plate"}
        return jsonify(data2)
    else:
        insert(connection,text)

        data2 = {"ayy": text}

    # json_data = json.dumps(data2)
        return jsonify(data2)


@app.route('/uploadvid', methods=['POST'])
def frecog2():
    content = request.get_json()
    vid_data = content['video']
    viddata = base64.b64decode(vid_data)
    print (content['name'])
    filename = 'vid2.mp4'
    with open(filename, 'wb') as f:
        f.write(viddata)
    # name=ty.m()
    return "kachow"


if __name__ == '__main__':
    #connection = connectToMongo()
    app.run(host='0.0.0.0')