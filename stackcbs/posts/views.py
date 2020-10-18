from django.shortcuts import render,redirect
from .models import Post,Like
from profiles.models import Profile
from .forms import PostModelForm,CommentModelForm
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    
    

    #post froms and comment form and initials 
    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False                   # when we submit post we ll set it to true
    print('post_added',post_added)
    profile = Profile.objects.get(user=request.user)
    
    if 'submit_p_form' in request.POST:
        print(33333)
        p_form = PostModelForm(request.POST,request.FILES)
        if p_form.is_valid():
            print(44444)
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        post_added = False
        print(111)
        c_form = CommentModelForm(request.POST) 
        if c_form.is_valid():
            print(222)
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm() 
    print(post_added)
    context = {
        'qs':qs,
        'profile':profile,
        'p_form' : p_form,
        'c_form' : c_form,
        'post_added':post_added,

    }

    return render(request,'posts/main.html',context)

@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id') #now we know to which post we are dealin
        post_obj = Post.objects.get(id=post_id)#post object 
        #now we need check for many to many field of posts to profile oif user 
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)  #if already liked then remove this profile 
        else:
            post_obj.liked.add(profile)
        


        like,created = Like.objects.get_or_create(user=profile,post_id=post_id) 
        #like is the object , created is the boolean value 
        if not created:
            if like.value=='Like':
                like.value = 'Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'    

            post_obj.save()
            like.save()    
    return redirect('posts:main-post-view')

class PostDeleteView(LoginRequiredMixin,DeleteView): #login must be firts parameter    model = Post
    template_name = 'posts/confirm_del.html'
    success_url = reverse_lazy('posts:main-post-view')  #first app name , name of our path from url
    #success_url = '/posts/'  #this will give the same above result

    def get_object(self,*args,**kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request,'you need to be author of this post in order to delete this ')
        return obj

class PostUpdateView(LoginRequiredMixin,UpdateView):
    form_class = PostModelForm
    model = Post
    template_name = 'posts/Update.html'
    success_url = reverse_lazy('posts:main-post-view')  #first app name , name of our path from url
    #success_url = '/posts/'  #this will give the same above result

    def form_valid(self,form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None,"you need to be author to update")  
            return super().form_invalid(form) 
