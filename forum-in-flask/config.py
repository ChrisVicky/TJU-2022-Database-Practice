class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQL 设置
    SQLALCHEMY_DATABASE_URI = 'postgresql://shujuku:Shujuku@8.141.166.181:5432/shujuku'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件配置
    # ADMINS = ['wangy8961@163.com']  # 管理员的邮箱地址
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_SENDER = os.environ.get('MAIL_SENDER')
    # 分页设置
    # POSTS_PER_PAGE = 10
    # USERS_PER_PAGE = 10
    # COMMENTS_PER_PAGE = 10
    # MESSAGES_PER_PAGE = 10

