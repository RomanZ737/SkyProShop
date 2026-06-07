from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post_form.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_number += 1
        self.object.save()
        if self.object.views_number >= 100:
            send_mail(
                "Поздравляю",
                f"просмотры поста {self.object.title} достигли 100",
                "django@example.com",
                ["roman.v@zfamily.aero"],
                fail_silently=False,
            )
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', args=[self.kwargs.get('pk')])

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

