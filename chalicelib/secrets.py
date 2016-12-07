import os
import json
import boto3

LIBDIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(LIBDIR, 'config.json')

def get_secret(key_name, filename=CONFIG_FILE):
    with open(filename) as f:
        config = json.load(f)
    encrypted = config[key_name].decode('base64')
    decrypted = boto3.client('kms').decrypt(
        CiphertextBlob=encrypted)['Plaintext']
    return decrypted

def get_kms_key_id(filename=CONFIG_FILE):
    with open(filename) as f:
        config = json.load(f)
        return config['key_id']
