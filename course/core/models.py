from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner_ID = models.IntegerField()
    lessons = models.ManyToManyField('Lesson')

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_status = models.BooleanField(default=False)
    viewed_time_seconds = models.IntegerField(default=0)

    def set_viewed_status(self):
        if self.viewed_time_seconds >= (self.lesson.duration_seconds * 0.8):
            self.viewed_status = True
        else:
            self.viewed_status = False

