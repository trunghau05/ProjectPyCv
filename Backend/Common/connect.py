from mongoengine import connect

connect(
    db='pycv_db',
    host='localhost',
    port=27017
)
