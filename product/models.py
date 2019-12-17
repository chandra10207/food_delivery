from django.db import models


class Food(models.Model):

    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name


class Topping(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    groups = models.ManyToManyField('Group', through='GroupMember', related_name='people')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    person = models.ForeignKey(Person, related_name='membership', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    extra = models.BooleanField(default=True)

    def __str__(self):
        return "%s is in group %s (as %d)" % (self.person, self.group, self.extra)