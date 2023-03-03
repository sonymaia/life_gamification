from django.db import models

class Daily_Objective(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"Daily_Objective [name = {self.name}]"

class Course(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    conclusion_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Couse [name = {self.name}]"


class Book(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    conclusion_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Book [name = {self.name}]"


class Rule(models.Model):
    description = models.TextField(null=False, blank=False)
    award = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return f"Rule [name = {self.description}]"
    
    
class Logbook(models.Model):
    date = models.DateField(null=True, blank=True)
    fk_daily_obj = models.ForeignKey(Daily_Objective, on_delete=models.CASCADE)