from django.db import models

# Create your models here.
from user_profile_app.models import User
from django.utils.text import slugify

from .slugs import generate_unique_slug

class Category(models.Model):
    title= models.CharField(max_length=50,unique=True)
    slug = models.SlugField(null=True,blank=True)
    created_date= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    


class Tag(models.Model):
    title= models.CharField(max_length=50,)
    slug = models.SlugField(null=True,blank=True)
    created_date= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)




class Blog(models.Model):
    user = models.ForeignKey(User,related_name="user_blogs",on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name="category_blogs", on_delete=models.CASCADE)
    
    tags= models.ManyToManyField(Tag,related_name="tag_blogs",blank=True)
    # black = True dile, blog post korar shomoy tag ta required dekhabe na

    likes=models.ManyToManyField(User,related_name="user_likes",blank=True)
    title = models.CharField(max_length=50,)
    slug = models.SlugField(null=True,blank=True)
    banner = models.ImageField(upload_to='blog_banners')
    created_date= models.DateField(auto_now_add=True)
    description=models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        updating = self.pk is not None
        if updating:
            self.slug = generate_unique_slug(self,self.title, update=True)
            super().save(*args,**kwargs)
        else:
            self.slug = generate_unique_slug(self,self.title)
            super().save(*args,**kwargs)

        
    



class Comment(models.Model):
    user = models.ForeignKey(User,related_name="user_comments",on_delete=models.CASCADE)
    blog= models.ForeignKey(Blog,related_name="blog_comments", on_delete=models.CASCADE)
    text= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    

class Comment_Reply(models.Model):
    user = models.ForeignKey(User,related_name="user_replies",on_delete=models.CASCADE)
    comment= models.ForeignKey(Comment,related_name="comment_replies", on_delete=models.CASCADE)
    text= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
