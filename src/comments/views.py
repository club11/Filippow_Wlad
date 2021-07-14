from django.forms import forms
from django.shortcuts import render

from django.views.generic import FormView


from django.http import HttpResponseRedirect

from django.contrib.contenttypes.models import ContentType
from . import forms

class CommentCreateView(FormView):
    form_class = forms.CommentCreateForm
    template_name = 'comments/tags/show_comments.html'

    def form_valid(self, form):
        next_step = form.cleaned_data.get('next_step')
        #comment_text = form.cleaned_data.get('next_step')
        #author = self.request.user
        #content_type_id = form.cleaned_data.get('content_type_id')
        return HttpResponseRedirect(next_step)
