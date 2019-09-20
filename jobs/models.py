from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()

    def __str__(self):  # Job 의 데이터가 어떻게 표현되는지 결정
        return self.name