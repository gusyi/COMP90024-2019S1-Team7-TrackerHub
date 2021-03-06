# -*- coding: utf-8 -*-

from django.db import models
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField, ListField, DateTimeField


class Tweet(Document):
    user = TextField()
    text = TextField()
    date = TextField()
    last_update = TextField()
    process = IntegerField()
    img_id = ListField(TextField)
    geo = ListField(TextField)
    hashtags = ListField(TextField)
    tags = ListField(TextField)
