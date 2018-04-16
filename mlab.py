
import mongoengine

#admin:codethechange17@ds041494.mlab.com:41494/chamcong
host = "ds041494.mlab.com"
port = 41494
db_name = "chamcong"
user_name = "admin"
password = "codethechange17"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())