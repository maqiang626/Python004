# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbOriginalComments(models.Model):
    title = models.CharField(max_length=2550, blank=True, null=True)
    alink = models.CharField(max_length=2550, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    crawling_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_original_comments'


class TbSemanticEmotion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    alink = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    crawling_date = models.DateTimeField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_semantic_emotion'


class TbSentimentAnalysis(models.Model):
    counter = models.CharField(max_length=11, blank=True, null=True)
    crawling_date_latest = models.DateTimeField(blank=True, null=True)
    sentiment_avg = models.CharField(max_length=11, blank=True, null=True)
    plus = models.CharField(max_length=11, blank=True, null=True)
    minus = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sentiment_analysis'
