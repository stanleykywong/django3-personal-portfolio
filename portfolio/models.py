from django.db import models

# Create your models here.

# 4a---personal_portfolio_project/portfolio/models.py, add Model (DB table)
# *** each "model"---maps to a single database "table" ("Project")
# *** each "attribute" of the model---represents a database "field" ("title")
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # 18f---personal_portfolio_project/portfolio/models.py, add:
    # to show the "title" name, instead of Project object (1), (2), (3)......
    def __str__(self):
        return self.title
