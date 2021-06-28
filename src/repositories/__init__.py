from flask_sqlalchemy import SQLAlchemy
from .word import WordRepository

db = SQLAlchemy()
__all__ ['WordRepository']