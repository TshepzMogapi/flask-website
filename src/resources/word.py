from flask import request, jsonify
from flask_restful import Resource

from repositories import WordRepository

class Word(Resource):
  def get(self, keyword: str):
    word = WordRepository.get(keyword)
    return word, 200
  

class Wordlist(Resource):
  def post(self):

    request_json = request.get_json(silent=True)
    word: str = request_json['word']
    description: str = request_json['description']
    try:
      word = WordRepository.create(word, description)
      return word, 200
    except Exception as e:
      response = jsonify(e.to_dict())
      response.status_code = e.status_code
      return response