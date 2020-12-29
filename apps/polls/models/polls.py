from django.core import meta


# Create your models here.
class Poll(meta.Model):

    question = meta.CharField(maxlength=200)
    pub_date = meta.DateTimeField('date published')

class Choice(meta.Model):
    poll = meta.ForeignKey(Poll)
    choice = meta.CharField(maxlength=200)
    votes = meta.IntegerField()