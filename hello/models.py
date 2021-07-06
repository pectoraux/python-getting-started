from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Document(models.Model):
    document_id = models.FileField(upload_to='static/', verbose_name='Proof of identity')
    document_utility = models.FileField(upload_to='static/', verbose_name='Proof of residence')
    email = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def file_link(self):
        if self.document_id:
            return "<a href='%s'>download</a>" % (self.document_id.url,)
        else:
            return "No attachment"

    file_link.allow_tags = True