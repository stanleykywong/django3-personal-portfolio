from django.db import models

# Create your models here.

# *** each "model"---maps to a single database "table" ("Project")
# *** each "attribute" of the model---represents a database "field" ("title")

# 12a---in personal_portfolio_project/blog/models.py, add:
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # 18g---personal_portfolio_project/blog/models.py, add:
    # to show the title name, instead of Blog object (1), (2), (3)......
    def __str__(self):
        return self.title
