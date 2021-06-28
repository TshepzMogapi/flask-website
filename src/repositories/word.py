from sqlalchemy.exc import IntegrityError
from models import Word

class WordRepository:
  
  @staticmethod
  def create(word: str, description: str) -> dict:
    """creates word"""
    result: dict = {}
    try:
      word = Word(word=word, description=description)
      word.save()
    except IntegrityError:
      Word.rollback() # raise Exception
    return result
  
  @staticmethod
  def get(keyword: str) -> dict:
    """query for a word"""
    word: dict = {}
    word = Word.query.filter_by(word=keyword).first_or_404()
    word = {
      'word': word.word,
      'description': word.description,
    }

    return word