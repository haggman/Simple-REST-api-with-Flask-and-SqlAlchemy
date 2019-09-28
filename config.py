class Config:
    # TODO: user and pass in config file, bad
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://student:student@localhost/bank"
    # Removes obnoxious track mods warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
