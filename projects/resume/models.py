from django.db import models

class Personal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.title


class JobItem(models.Model):
    title = models.CharField(max_length=200)
    job = models.ForeignKey(Job)

    def __unicode__(self):
        return self.job.title + '/' + self.title
