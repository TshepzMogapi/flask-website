from flask_restful import Api
from resources import Wordlist, Word
from models import Word as WordModel, db
from flask_migrate import Migrate
from app import create_app


app = create_app()
migrate = Migrate(app, db)


# API
api = Api(app)
api.add_resource(Wordlist, '/api/words')
api.add_resource(Word, '/api/word/<keyword>')

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Word=WordModel)