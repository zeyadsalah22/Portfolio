from django.db import models

class Project(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    link = models.URLField()
    tools = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Project: {self.name}"

class Skill(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    acquired = models.TextField()

    def __str__(self):
        return f"Skill: {self.name}"

class Certificate(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=64)

    def __str__(self):
        return f"Certificate: {self.name}"

class Texter(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} messaged you"