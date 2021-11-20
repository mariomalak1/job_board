from django.db import models

# Create your models here.

'''
 django model field : 
    - html widget
    - validation 
    - db size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):  # table 
    title = models.CharField(max_length=100)  # column
    # location 
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
    category = models.ForeignKey('category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'jobs/' , null=True , blank = True)

    def __str__(self):
        return self.title

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_leter = models.CharField(max_length=500)
    job = models.ForeignKey(Job, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.name