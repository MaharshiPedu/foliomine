from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from mysite.settings import MEDIA_ROOT


class Profile(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_name = models.CharField(
        max_length=50, null=False, default="New profile")
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    about = models.TextField(max_length=500)
    profile_photo = models.ImageField(
        upload_to='profile_photos/%Y/%m/%d/', blank=True, null=True)
    github_link = models.URLField(max_length=250, null=True)
    twitter_link = models.URLField(max_length=250, null=True)
    linkedin_link = models.URLField(max_length=250, null=True)

    class Meta:
        db_table = "Profile"

    def save(self, *args, **kwargs):
        super().save()
        # [:len(MEDIA_ROOT)-5] removes media from the end of MEDIA_ROOT url,
        # since profile_photo.url already contains it.
        if self.profile_photo:
            photo_url = MEDIA_ROOT[:len(
                MEDIA_ROOT) - 5] + self.profile_photo.url
            img = Image.open(photo_url)
            width, height = img.size

            if width > height:
                remaining = width - height
                left = remaining // 2
                right = height + (remaining // 2)
                croppedImage = img.crop((left, 0, right, height))

            elif width < height:
                remaining = height - width
                top = remaining // 2
                bottom = width + (remaining // 2)
                croppedImage = img.crop((0, top, width, bottom))

            else:
                croppedImage = img

            croppedImage.save(photo_url)

    def __str__(self):
        return self.first_name + " " + self.last_name + " profile"


class Experience(models.Model):

    id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    exp_start_date = models.DateField(null=False)
    exp_end_date = models.DateField(null=False)
    job_profile = models.TextField(max_length=50, null=False)
    company_name = models.TextField(max_length=50, null=False)
    details = models.TextField(max_length=2000, null=False)

    class Meta:
        db_table = "Experience"

    def __str__(self):
        return self.job_profile


class Education(models.Model):

    id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    edu_end_date = models.DateField(null=False)
    degree = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=50, null=False)
    grade = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = "Education"

    def __str__(self):
        return self.degree


class Project(models.Model):

    id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    proj_start_date = models.DateField(null=False)
    proj_end_date = models.DateField(null=False)
    project_name = models.CharField(max_length=100, null=False)
    project_details = models.TextField(max_length=2000, null=False)
    project_code_link = models.URLField(max_length=500, null=True)
    project_link = models.URLField(max_length=500, null=True)
    project_photo = models.ImageField(
        upload_to='project_photos/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        db_table = "Project"

    def save(self, *args, **kwargs):
        # print("----->>>>", self.project_photo.url)
        super().save()
        if self.project_photo:
            photo_url = MEDIA_ROOT[:len(MEDIA_ROOT) - 5] + self.project_photo.url
            img = Image.open(photo_url)
            img.save(photo_url)

    # def __str__(self):
    #     return self.project_name

