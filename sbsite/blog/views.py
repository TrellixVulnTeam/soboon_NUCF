from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Post, Images
from .forms import PostForm, UserLoginForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory

# Create your views here.
def post_list(request):
    post_list= Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':post}) 

def post_new(request):

    # ImageFormset = modelformset_factory(Images, field=('image',), extra=4)
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3,)
    if request.method == "POST":

        form = PostForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)


        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # for form in formset.cleaned_data:
            #     try:
            #         image = form['image']
            #         photo = Images(post=post_form, image=image)
            #         photo.save()
            #         return redirect('post_list')
                
            #     except Exception as e:
            #         pass
            # return redirect('post_detail', pk=post.pk)
            
            for f in formset:
                try:
                    
                    photo = Images(post=post, image=f.cleaned_data['image'])
                    photo.save()
                   
                
                except Exception as e:
                    break
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'blog/post_edit.html', {'form': form, 'formset':formset,})



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
            
                    login(request, user)
                    return HttpResponseRedirect(reverse('post_list'))
                else:
                    return HttpResponse("등록된 사용자가 아닙니다.")    
            else:
                return HttpResponse("등록된 사용자가 아닙니다.")  
    else:
        form = UserLoginForm()

    context = {
        'form' : form,
    }    

    return render(request, 'blog/login.html', context)

def user_logout(request):  
    logout(request)
    return redirect('post_list') 



def gallery(request):
    
    return render(request,'blog/gallery.html')     
 
def about(request):
    
    return render(request,'blog/about.html')         