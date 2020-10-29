from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    profile_picture = CloudinaryField('image')
    prof_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    bio = models.TextField(default="")
    contact_info = models.CharField(max_length=200, blank=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

    @classmethod
    def get_profile_data(cls):
        return Profile.objects.all()

    class Meta:
        db_table = 'profiles'