class Config:
    debug = True
    SECRET_KEY = 'qwertyuiop'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vick:p@127.0.0.1:5432/minpitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
