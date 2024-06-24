from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/UserPosts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-timeStamp')

def delete(request, slug):
    post=Post.objects.filter(slug=slug).first()
    post.delete()
    return redirect("/blog/user_posts/")

def edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('editor1')
        image = request.POST.get('img_file')
        post.title = title
        post.content = content
        if image:
            post.image = image
        post.save()
        messages.success(request, "Blog post updated successfully.")
        return redirect(f"/blog/{post.slug}")
    context = {'post': post}
    return render(request, "blog/EditBlog.html", context)

def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/BlogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    if not request.session.get(f'viewed_post_{post.slug}'):
        post.views += 1
        post.save()
        request.session[f'viewed_post_{post.slug}'] = True
    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def Addblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.user
        content = request.POST.get('editor1')
        image = request.POST.get('img_file')
        blogpost = Post(title=title, author=author,slug=title, content=content, image=image)
        blogpost.save()
        return redirect("/blog/user_posts/")
    return render(request, "blog/AddBlog.html")


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")
