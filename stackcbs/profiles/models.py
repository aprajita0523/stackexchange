from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify 

# Create your models here.
# each of below feilds reprensent columns in the database
# every row needs to referd as object
# every user can have acess to his profile only hence one to one used not foreign
class Profile(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # if user deleted the profile will be deleted as well
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=300 ,blank=True)
    country = models.CharField(max_length=200,blank=True)
    avatar = models.ImageField(default='avatar.png',upload_to = 'avatars/')
    #image path stored here not images
    #need to install pillow for the Image , create media_root , Also add default picture 
    friends = models.ManyToManyField(User,blank=True,related_name="friend")
    #dafult=None can be also used 
    slug = models.SlugField(unique=True, blank=True)
    #slug is a way of generating a valid URL, generally using data already obtained
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_friends(self):
        return self.friends.all()  #manytomany relationship

    def get_friends_no(self):
        return self.friends.all().count()       #no. of friends

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
        #profile will be created once registered.
    
    def get_post_no(self):
        return self.posts.all().count() #instead of writing post_set.all()
        #reverse relationship to the POSt Model as we have related name 
    def get_all_authors_posts(self):
        return self.posts.all()    #reverse relationship to POST model, here we have relate name 
    

    def get_likes_given_no(self):
        likes =  self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked +=1
        return total_liked    

    def get_likes_recieve_no(self):
        post = self.posts.all()
        total_liked = 0
        for item in post:
            total_liked += item.liked.all().count()
        return total_liked
         #we are grabbing particular posts 
         #we are acessing the likes field
         #we are grabbing all the likes of particular posts and ounting them 
         #we are doing this for each post object of our profile instance
         #to commulate it in total liked



    #setting value to slug if the first name and last name exist 
    def save(self, *args , **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name)+""+str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug +""+ str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)     
        self.slug = to_slug
        super().save(*args,**kwargs) 
STATUS_CHOICES = (
    ('send','send'),  #first is for databse cant see second for admin 
    ('accepted','accepted')
)
class Relationship(models.Model):
    sender = models.ForeignKey(Profile , on_delete=models.CASCADE, related_name='sender') # if profile gets deleted relationship will be deleted
    receiver = models.ForeignKey(Profile , on_delete=models.CASCADE, related_name='receiver') # if profile gets deleted relationship will be deleted
    status = models.CharField(max_length=8,choices =STATUS_CHOICES )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
        #self.sender returns Profile str 
       
    