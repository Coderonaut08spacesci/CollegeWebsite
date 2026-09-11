from django.db import models
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(max_length=100) # e.g., Computer Science, Commerce, Arts
    code = models.CharField(max_length=10, unique=True) # e.g., CS, COMM, ARTS
    description = models.TextField()
    head_of_dept = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Admission', 'Admissions'),
        ('Exam', 'Examinations'),
        ('Sports', 'Sports & Cultural'),
        ('General', 'General Notice'),
    ]
    
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='General')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.category}"

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=150)
    banner_image = models.ImageField(upload_to='events/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
