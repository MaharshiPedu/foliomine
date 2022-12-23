from django.db import models


class User(models.Model):

    first_name      = models.CharField(max_length=25, null=False)
    last_name       = models.CharField(max_length=25, null=False)
    email           = models.EmailField(max_length=50, null=False)
    hashed_password = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.first_name+" "+self.last_name+" user"


class Profile(models.Model):

    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name    = models.CharField(max_length=25, null=False)
    last_name     = models.CharField(max_length=25, null=False)
    about         = models.TextField(max_length=500)
    profile_photo = models.ImageField(upload_to='profile_photos/%Y/%m/%d/', blank=True, null=True)
    github_link   = models.URLField(max_length=250, null=True) 
    twitter_link  = models.URLField(max_length=250, null=True) 
    linkedin_link = models.URLField(max_length=250, null=True)

    class Meta:
        db_table = "Profile"

    def __str__(self):
        return self.first_name+" "+self.last_name+" profile"


class Experience(models.Model):

    profile_id   = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date   = models.DateField(null=False)
    end_date     = models.DateField(null=False)
    job_profile  = models.TextField(max_length=50, null=False)
    company_name = models.TextField(max_length=50, null=False)
    details      = models.TextField(max_length=2000, null=False)

    class Meta:
        db_table = "Experience"
    
    def __str__(self):
        return self.job_profile


class Education(models.Model):

    profile_id   = models.ForeignKey(Profile, on_delete=models.CASCADE)
    end_date     = models.DateField(null=False)
    degree       = models.CharField(max_length=100, null=False)
    school       = models.CharField(max_length=200, null=False)
    city         = models.CharField(max_length=20, null=False)
    country      = models.CharField(max_length=50, null=False)
    grade        = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = "Education"

    def __str__(self):
        return self.degree


class Project(models.Model):

    profile_id      = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date      = models.DateField(null=False)
    end_date        = models.DateField(null=False)
    project_name    = models.CharField(max_length=100, null=False)
    project_details = models.TextField(max_length=2000, null=False)

    class Meta:
        db_table = "Project"

    def __str__(self):
        return self.project_name
