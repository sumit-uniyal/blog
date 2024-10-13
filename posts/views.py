from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from .forms import CommentForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    post = Posts.objects.all()
    return render(request, 'posts/index.html', context={'post':post})

def blog_detail(request, id):
    post = get_object_or_404(Posts, id=id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Assuming the user is logged in
            comment.save()
            return redirect('blog_detail', id=id)  # Redirect after POST to avoid duplicate submission
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, 'posts/blog-detail.html', context)

def comment_like(request, id):
    comment = Comment.objects.get(pk=id)
    comment.likes += 1
    comment.save()
    return redirect (home)

# views.py
def share_blog(request, blog_id):
    # Retrieve the blog post
    blog = get_object_or_404(Posts, id=blog_id)
    recipient_email = None

    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')  # Get email from POST data
        if recipient_email:
            # Prepare email content
            subject = f"Check out this blog: {blog.title}"
            message = f"Read the blog '{blog.title}' Created by { blog.created_by.first_name } { blog.created_by.last_name }\n\n{blog.description}"
            
            # Send the email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )

            return redirect(home)  # Redirect to blog detail page