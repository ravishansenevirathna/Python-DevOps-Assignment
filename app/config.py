class Config:
    SECRET_KEY = 'your-secret-key'
    #local
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost/flask_task_db'

    # docker
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:1234@mysql:3306/flask_task_db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

