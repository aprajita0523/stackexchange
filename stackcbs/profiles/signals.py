from django.db.models.signals import post_save # info will be send at the end of save method 
from django.contrib.auth.models import User # the user model
from django.dispatch import receiver  #in order to regsiter signals we will be using reciever decorators
from .models import Profile,Relationship # our Profile model


#use reciever decorator and inside we put in the post_save and indicate 
#who is the sender so the sender is the user here
#User will send the signal about user being created
#basically User instance will be automatically created in Profile model once user created
#everytime user created a profile to user will be created automatically .
@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created, **kwargs):
     # sender is the model of the user and instance of the particular User
     #created is the boolean value
     # if user craeted out of this user model then we can simply 
     #print('sender',sender)
     #print('instance',instance)
     #sender <class 'django.contrib.auth.models.User'>
     #instance signaluser

     if created:
         Profile.objects.create(user=instance) #as a user we can pass this instace this is our first signal 


#for status aceepted adding frieds to both 
@receiver(post_save,sender=Relationship)
def post_save_add_to_friends(sender,instance,created,**kwargs):
            sender_ = instance.sender   #_ used just to differentiate var with model var
            receiver_ = instance.receiver
            if instance.status == "accepted":
                sender_.friends.add(receiver_.user)
                receiver_.friends.add(sender_.user)
                sender_.save()
                receiver_.save()
                #bothe sender and reciever from relationship model
                #added to respetive profile.user and vice versa


