from django.db import models


# Main Section
class BaseModel(models.Model):
    """
    공통적으로 사용할 BaseModel
    - created: 객체 생성 시간 (자동 설정)
    - modified: 객체 수정 시간 (자동 갱신)
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
