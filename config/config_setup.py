import os
import json

prefix = raw_input('ENV_PREFIX: ')
db_uri = prefix + '_DB_URI'
db_name = prefix + '_DB_NAME'
db_collection = prefix + '_DB_COLLECTION'
debug = prefix + '_DEBUG'
secret_key = prefix + '_SECRET_KEY'

db_uri_value = raw_input('db uri: ')
db_name_value = raw_input('db name: ')
db_collection_value = raw_input('collection name: ')
debug_value = raw_input('debug? (True/False): ')
secret_key_value = raw_input('secret key: ')


config = {}
config[db_uri] = db_uri_value
config[db_name] = db_name_value
config[debug] = debug_value
config[secret_key] = secret_key_value

try:
    for key, val in config.items():
        os.environ[key] = val

    with open('settings.py', 'w') as f:
        settings_file = """import os

SETTINGS = {
    'DB_URI': os.environ.get('%s', '-1'),
    'DB_NAME': os.environ.get('%s', '-1'),
    'DEBUG': os.environ.get('%s', '-1'),
    'SECRET_KEY': os.environ.get('%s', '-1')
}

""" % (db_uri, db_name, debug, secret_key)
        f.write(settings_file)
except Exception as e:
    print 'Error saving/writing config: %s' % e
