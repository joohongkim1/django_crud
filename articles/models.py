from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE -> 'Article이 삭제되면 Comment도 함께 삭제'
    # article.comment_set <- django 디폴트값
    # related_name => 'Article Instance'가 comment를 역참조 할 수 있는 이름을 정의
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # add 없는 경우 : 추가 됐을 때 뿐만 아니라 데이터에 수정이 생긴 모든 경우 

    # 역순으로 가져올 수 있도록
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content