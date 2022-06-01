# когда создаёшь новый Django проект:
1. [ ] __создать "проект"__ `django-admin startproject myfirst`
2. [ ] __создать "приложение"__ `python manage.py startapp articles`
3. [ ] (в 'myfirst') __создать папки__ [apps](), [static](), [templates]()
   1) [ ] __переместить папку__ [articles]() в папку [apps]()
   2) [ ] в папке [apps / articles]() __cоздать__ файл [urls.py]() | содержащий : 
   ```python
   from django.urls import path
   
   from . import views
   
   app_name = 'articles'
   urlpatterns = [
       path('', views.index, name = 'index'),
   ]
   ```
   1. [ ] в [myfirst / urls.py]() __дописать__ : `path('articles/', include('articles.urls')),`
4. [ ] в файле [myfirst / settings.py]() __дописать__ :
```python 
import os,sys #дописали
PROJECT_ROOT = os.path.dirname(__file__) #дописали
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) #дописали

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(PROJECT_ROOT, 'templates')
        ]

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static') #дописали
```
- [ ] код для [articles / views.py]()
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет мир!!!")
```

# пишем __структуру__ нашей __БД__ для articles (в [articles / models.py]())
```python
class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)
```
  - [ ] дописываем в [settings.py]() :
  ```python
    INSTALLED_APPS = [
        'articles.apps.ArticlesConfig',
  ```
сохраняем:
`python manage.py makemigrations articles`
`python manage.py migrate`
  - [ ] дописываем в [articles / models.py]() :
```python
import datetime
from django.utils import timezone

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
```
# добавляем раздел articles (__в админку__)
- [ ] __создать "админа"__ `python manage.py createsuperuser`
- [ ] дописываем в [articles / admin.py]():  
   ```python
   from .models import Article, Comment
   
   admin.site.register(Article)
   admin.site.register(Comment)
   ```
- [ ] дописываем в [articles / apps.py]():  
   ```python
       verbose_name = 'Блог'
   ```
- [ ] дописываем в [articles / models.py]():  
   ```python
       class Meta:
           verbose_name = 'Статья'
           verbose_name_plural = 'Статьи'
   ```