from django.db import models

class Blogpost(models.Model):
    post_id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    head0 = models.CharField(max_length=255,default="")
    chead0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=255,default="")
    chead1 = models.CharField(max_length=5000,default="")
    head2 = models.CharField(max_length=255,default="")
    chead2 = models.CharField(max_length=5000,default="")
    pub_data = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images/",default="")
    def __str__(self):
        return self.title
