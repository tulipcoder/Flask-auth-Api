import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or b'\xd1:\xb6\xd3\x8d\x160\xa9\xa5\x00a\x14K\xf2\xd3\xd8'
    

    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}