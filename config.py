# Developement Environment
DEBUG = True

# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#DATABASE
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(BASE_DIR, 'britecore.db'))
DATABASE_CONNECT_OPTION = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application threads.
THREADS_PER_PAGE = 2

# Enable protection against CSRF
CSRF_ENABLED = True

# Secret Keys
CSRF_SESSION_KEY = """?UMHRaR#zMrBR]{."(Yk^EQSh:/nw?@CqgBSF!._9p+S&k<-xf45x/"X>%SMquR"""
SECRET_KEY = """%2Yds+,wQ4.lg2H;k*v%df(GE8Y"k!,CSafFF1g.ub'_t^49T]7a{%R0}AUi;H"""
