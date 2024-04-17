import os

print(os.getcwd())
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'