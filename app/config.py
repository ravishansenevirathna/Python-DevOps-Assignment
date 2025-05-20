class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost/flask_task_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False