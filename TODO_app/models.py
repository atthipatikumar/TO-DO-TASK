from django.db import models

class RegisterLogo(models.Model):
    ID = models.IntegerField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=255, default=None, verbose_name="Title")

    def _str_(self):
        form = PostForm()
        return self.title
    class Meta:
        db_table = ('todo_title')
        unique_together = (('title'),)
        #app_lable = ('TODO_app')

class Register(models.Model):
    task_id = models.IntegerField(primary_key=False, verbose_name="TaskID")
    title = models.CharField(max_length=255, default=None, verbose_name="Title")
    description = models.TextField(default=None, verbose_name="Description")
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default=False, verbose_name="status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date_Created")
    date_modified = models.DateField(auto_now_add=False, verbose_name="Date_Modified")
    register_logo = models.ForeignKey('RegisterLogo', related_name='logo_text')

    def _str_(self):
        form = PostForm()
        return self.description

    class Meta:
        db_table = ('todo_fields')
        unique_together = (('task_id', 'register_logo'),)
        #app_lable = ('TODO_app')
