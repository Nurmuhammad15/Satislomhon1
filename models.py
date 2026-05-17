from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class Course(models.Model):
    COURSE_TYPE = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('individual', 'Shaxsiy'),
    ]
    title = models.CharField(max_length=200)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE)
    description = models.TextField()
    icon = models.CharField(max_length=10, default='📱')
    features = models.TextField(help_text="Har bir qator alohida xususiyat")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class Statistic(models.Model):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return f"{self.number} - {self.label}"
