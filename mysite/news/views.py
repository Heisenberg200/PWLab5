from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
# from django.http import HttpResponse
from .models import News, Category
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрированы')
            # return redirect('login')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

# def index(request):
#     # print(dir(request))
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'\n<div><p>{item.title}</p>\n<p>{item.content}</p>\n</div><hr>\n'
#     return HttpResponse(res)
#     # return HttpResponse("Привет притурки!")

# def index(request):
#     news = News.objects.all()
#     # categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#         # 'categories': categories,
#     }
#     return render(request, 'news/index.html', context=context)

# Вместо ф-ции index (просмотр всех новостей)
class HomeNews(ListView):
    model = News
    # template_name = 'news/index.html'
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2

# для добавления своих переменных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

# фильтр - наш запрос
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')




# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})

  # вместо функции get_category (ПРОСМОТР НОВОСТЕЙ КОНКРЕТНОЙ КАТЕГОРИИ)
class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    # фильтр
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

# для добавления своих переменных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

# def test(request):
#     return HttpResponse('<h1> Тестовая страница </h1>')

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item':news_item})

# вместо функции view_news (просмотр конкретной новости)
class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = News.objects.create(**form.cleaned_data)
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})

# вместо функции add_news (создание новости)
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'   # если НЕ авторизован, направить на страницу авторизации
    # raise_exception = True  # или как вариант ВОЗБУДИТЬ ОШИБКУ и вывести 403 FORBIDDEN

