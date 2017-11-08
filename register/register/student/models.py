# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from register.course.models import course

class student(models.Model):
    course_no = models.ManyToManyField(course)
    user_student= models.ForeignKey(User, null=True)
    student_id = models.CharField(max_length=20, null=True, unique=True)
    program = models.CharField(max_length=20, null=True)
    batch = models.CharField(max_length=20, null=True)

    @classmethod
    def create(cls, user_student, student_id, program, batch):
        student = cls(user_student=user_student, student_id=student_id, program=program, batch=batch)
        return student

    def __str__(self):
        return self.student_id



