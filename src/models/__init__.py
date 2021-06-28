from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base_model import BaseModel
from .word import Word

__all__ = ['BaseModel', 'Word']