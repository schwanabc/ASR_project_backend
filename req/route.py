from flask import Flask, jsonify, request
from req import process_text
def init(app: Flask):
    @app.route('/ping')
    def ping_api():
        return jsonify({ 'message': 'pong' })
    
    @app.route('/getdata', methods = ['GET'])
    def call():
        if request.method == 'GET':
            sentence = request.args['sentence']
            return jsonify(process_text.find_nearast_sentence(sentence))
