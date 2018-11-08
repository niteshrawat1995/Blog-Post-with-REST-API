from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
# from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query_set = self.model.objects.filter(Q(title__icontains=query) |
                                                  Q(content__icontains=query)
                                                  )
            return query_set
        else:
            return super(PostListView, self).get_queryset()


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    # overriding to change the query set
    def get_queryset(self):
        query = self.request.GET.get('q')
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        if query:
            query_set = self.model.objects.filter(Q(author=user),
                                                  Q(title__icontains=query)| Q(content__icontains=query))
            return query_set
        else:
            return self.model.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Overriding the form to make the current user as the author of the post.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overriding form_valid() from UpdateView to make the current user as the author.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # overriding test_func() of UserPassesTestMixin so that only the author can update the post.
    def test_func(self):
        # get the current post object.
        post = self.get_object()
        # check the user is actually the author of the post.
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # overriding test_func() of UserPassesTestMixin so that only the author can delete the post.
    def test_func(self):
        # get the current post
        post = self.get_object()
        # check the user is actually the author of the post.
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


class GridListView(ListView):
    # filterset_class = ProductFilter
    template_name = 'blog/grid.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()

    def post(self):
        print('iam working!')
        if self.request.POST.getlist('checks'):
            Post.objects.filter(self.request.POST.getlist('checks')).delete()
        return super(GridListView, self).post()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GridListView, self).get_context_data(**kwargs)
        # context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        total_count = Post.objects.all().count()
        context['total_count'] = total_count
        context['comment_list'] = Comment.objects.all()
        return context
