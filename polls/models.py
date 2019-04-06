from django.db import models
from django import forms

# Create your models here.

 

class Etudiant(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	email = models.EmailField(max_length=70,blank=True)
    
	def __str__(self):
		return self.first_name

	 


class Teacher (models.Model):


	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=70,blank=True)
	specialty = models.CharField(max_length=100)
	experience = models.IntegerField()
	#phone_Number = models.CharField(max_length=120)


	def __str__(self):
		return self.first_name

	


class Exercise (models.Model):
	acceder = models.ManyToManyField(Etudiant, through='Membership')
	Énoncé= models.CharField(max_length=100)
	body = forms.CharField(widget= forms.Textarea, label="description",required=True)
	description = models.TextField()

	Fill_in_the_Blank = 'R1'
	Multi_Option_Format ='R2'
	writing ='R3'
	Correct_the_answer ='R4'
	EXERCISE_TYPE = (
    (Fill_in_the_Blank, 'Fill in the Blank'),
    (Multi_Option_Format, 'Multi Option Format'),
	(writing, 'writing'),
	(Correct_the_answer, 'Correct the answer')
	)
	type_of_exercise = models.CharField(max_length=1, choices=EXERCISE_TYPE, default=Fill_in_the_Blank)



	Exercise_1 = 'E1'
	Exercise_2 ='E2'
	Exercise_3 ='E3'
	Exercise_4 ='E4'
	EXERCISE_TYPE_CHOICES = (
    (Exercise_1, 'Exercise 1'),
    (Exercise_2, 'Exercise 2'),
	(Exercise_3, 'Exercise 3'),
	(Exercise_4, 'Exercise 4')
	)
	select_an_exercise = models.CharField(max_length=1, choices=EXERCISE_TYPE_CHOICES, default=Exercise_1)



	easy = 'E'
	medium ='M'
	difficult ='D'
	exercise_level_choices = (
    (easy, 'Easy'),
    (medium, 'Medium'),
	(difficult, 'Difficult')
	)
	exercise_level = models.CharField(max_length=1, choices=exercise_level_choices ,default=easy)

	def __str__(self):
		return self.acceder
	
 
class Membership (models.Model):
	
	etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
 	