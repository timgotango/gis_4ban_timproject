from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # onetoonekey는 1대1이였다면, foreignkey는 1대다
    # cascade(종속)가 user가 삭제되면 article 또한 삭제였다면, set_null은 user가 없어져도 신원 미상으로는 article 존재.
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)    # media 안에 article이라는 파일이 생기고 그 안에 이미지가 저장.
    content = models.TextField(null=True)    # 장문을 쓸 경우에는 textfield
    created_at = models.DateField(auto_now_add=True, null=True)    # DB에 저장되는 순간의 시각을 알아서 찍어줌
    like = models.IntegerField(default=0)