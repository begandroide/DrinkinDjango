from django.db import models

# Create your models here.
class Question(models.Model):
     question_text = models.CharField(max_length = 200)
     pub_date = models.DateTimeField('Date Published')
     
     def __str__(self):
             return self.question_text


class Choice(models.Model):
     question = models.ForeignKey(Question,on_delete=models.CASCADE)
     choice_text = models.CharField(max_length = 200)
     votes = models.IntegerField(default=0)
     
     def __str__(self):
             return self.choice_text

class Student(models.Model):
                    name = models.CharField(max_length = 200)
                    hobby = models.CharField(max_length = 200)
                    creation_date = models.DateTimeField('Creation Date')
     
                    def __str__(self): 
                                 return self.name

class Course(models.Model):
                    name_text = models.CharField(max_length = 200)
                    description = models.CharField(max_length = 200)

                    def _str_(self):
                                        return self.name_text

class StudentCourse(models.Model):
                    student = models.ForeignKey(Student,on_delete = models.CASCADE)
                    course = models.ForeignKey(Course, on_delete = models.CASCADE)
                    grade = models.IntegerField(default=0,)

                    def _str_(self):
                                        return self.student
