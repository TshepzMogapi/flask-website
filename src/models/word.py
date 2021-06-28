from . import db
from .base_model import BaseModel
import datetime

class Word(db.Model, BaseModel):
  word = db.Column(
    db.String, primary_key=True,
    unique=True,nullable=False)
  description = db.Column(
    db.String,nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  def __init__(self, word: str, description: str):
    self.word = word
    self.description = description