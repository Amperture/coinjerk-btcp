import os


class Config(object):
    ENABLE_USER_REGISTRATION = \
        (os.getenv("ENABLE_USER_REGISTRATION").lower() == "true")
