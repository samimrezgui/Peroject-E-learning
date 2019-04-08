from django.db import models
from django import forms

# Create your models here.

 
from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50, default='')
	age = models.IntegerField()
	code = models.CharField(max_length=5)
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	#group = models.ForeignKey(Group, on_delete=models.CASCADE)



class Teacher(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	experience = models.IntegerField(default=0)
	#course = models.ForeignKey(Cours, on_delete=models.CASCADE)
	specilization = models.CharField(
		max_length=10,
		choices=(
			('math', 'Math'), ('physics', 'Physics'), ('arts', 'Arts')
		),
		default='math'
	)

 
	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' | ' + self.specilization

class Exercise(models.Model):
	author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	choices = models.CharField(max_length=100)
	difficulty = models.IntegerField(
		choices=((1, 'easy'), (2, 'medium'), (3, 'hard')),
		default=1
	)
	# forein key to test


	def __str__(self):
		return self.text

class individual_Assignment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


	def __str__(self):
		return self.student.first_name + ' working on ' + self.exercise.text 

	

class Cours(models.Model):
	description = models.CharField(max_length=200)
	objectives = models.CharField(max_length=200)
	room = models.CharField(max_length=50)
	day = models.CharField(max_length=10)
	start_time = models.CharField(max_length=10)
	end_time = models.CharField(max_length=10)
	def __str__(self):
		return 'this course is beginning at ' + self.start_time + ' and will be finished at ' + self.end_time
 	# teacher
	# description
	# objectives
	# room
	# dates
	# start date
	# end date

class Group(models.Model):
	name = models.CharField(max_length=30)
	level = models.CharField(max_length=30)
	def __str__(self):
		return self.name + ' and level ' + self.level


class Enrollment(models.Model):
	cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Test(models.Model):
	test = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	date = models.CharField(max_length=10)
	coeficient = models.FloatField(null=True, blank=True, default=None)
	Test_type = models.CharField(max_length=30)
	def __str__(self):
		return 'Test of ' + self.test.specilization + ' created by ' + self.test.first_name + ' ' + self.test.last_name 
	
class Group_Assignment(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	def __str__(self):
		return self.group.name + ' take a test at ' + self.test.date 
	 
