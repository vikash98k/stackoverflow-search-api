from django.db import models


class Question(models.Model):
    ORDER_CHOICES = [
    ("desc", "desc"),
    ("asc", "asc")
    ]
    SORT_CHOICES = [
        ("activity", "activity"),
        ("votes", "votes"),
        ("creation", "creation"),
        ("relevance", "relevance")
    ]
    CLOSED_CHOICES=[
        ("True","True"),
        ("False","False")
    ]
    NOTICE_CHOICES=[
        ("True","True"),
        ("False","False")
    ]
    WIKI_CHOICES=[
        ("True","True"),
        ("False","False")
    ]
    ACCEPTED_CHOICES=[
        ("True","True"),
        ("False","False")
    ]
    MIGRATED_CHOICES=[
        ("True","True"),
        ("False","False")
    ]

    title = models.CharField(max_length=100)
    page = models.IntegerField()
    site = models.CharField(max_length=20,default="stackoverflow")
    notice=models.CharField(max_length=5,choices=NOTICE_CHOICES,blank=True)
    order = models.CharField(max_length=4, choices=ORDER_CHOICES, default="desc")
    sort = models.CharField(max_length=9, choices=SORT_CHOICES, default="activity")
    closed = models.CharField(max_length=5,choices=CLOSED_CHOICES,blank=True)
    accepted=models.CharField(max_length=5,choices=ACCEPTED_CHOICES,blank=True)
    migrated=models.CharField(max_length=5,choices=MIGRATED_CHOICES,blank=True)
    wiki=models.CharField(max_length=5,choices=WIKI_CHOICES,blank=True)
