from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Daily_Objective(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"Daily_Objective [name = {self.name}]"

class Rule(models.Model):
    description = models.TextField(null=False, blank=False)
    reward = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return f"Rule [name = {self.description}]"
     
class Daily_Record(models.Model):
    date = models.DateField(null=True, blank=True, default = datetime.today)
    fk_daily_obj = models.ForeignKey(Daily_Objective, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    def __str__(self):
        return f"Daily_Record [date = {self.date}]"

class Category(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    reward = models.DecimalField(max_digits=10, decimal_places=0, default = 1)
    def __str__(self):
        return f"{self.name}"

class Category_Record(models.Model):
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Category_Record [description = {self.description}]"
    
class Goal(models.Model):
    description = models.TextField(null=False, blank=False)
    creation_date = models.DateField(null=True, blank=True, default = datetime.today)
    conclusion_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(null=False, blank=False, default=False)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.DecimalField(max_digits=10, decimal_places=0)
    def __str__(self):
        return f"Goal [description = {self.description}]"
    
class Gift(models.Model):
    creation_date = models.DateField(null=False, blank=False, default = datetime.today)
    conclusion_date = models.DateField(null=True, blank=True)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Gift [conclusion_date = {self.conclusion_date}]"

