from django import template
from .. import models
from django.contrib.contenttypes.models import ContentType
register = template.Library()

@register.inclusion_tag('comments/tags/show_comments.html', takes_context=True)
def show_comments(context):
    obj = context.get('object')
    next_step = context.get('request').path
    print(next_step)
    content_type = ContentType.objects.get_for_model(obj)
    content_type_id = content_type.pk
    comments = models.Comment.objects.filter(content_type=content_type, object_id=obj.pk)
    return {'comments' : comments, 'next_step' : next_step, 'content_type_id' : 'content_type_id'}


    