from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

#не полная информация

class KgmaWorkView(generic.ListView):
    template_name = 'kgmawork.html'
    queryset = models.KgmaWork.objects.all

    def get_queryset(self):
        return models.KgmaWork.objects.all()



#детальная информация
class KgmaWorkDetailView(generic.DetailView):
    template_name = 'kgmawork_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.KgmaWork, id=show_id)



#добавление работника
class KgmaWorkCreateView(generic.CreateView):
    template_name = 'add_kgma_work.html'
    form_class = forms.KgmaWorkForm
    queryset = models.KgmaWork.objects.all()
    success_url = '/kgmawork/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(KgmaWorkCreateView, self).form_valid(form=form)

#добавление комментария
class CommentCreateView(generic.CreateView):
    template_name = 'commentadd.html'
    form_class = forms.CommentForm
    queryset = models.Commet_TV.objects.all()
    success_url = '/kgmawork/'

#Изменение шоу
class KgmaWorkUpdateView(generic.UpdateView):
    template_name = 'update_kgma.html'
    form_class = forms.KgmaWorkForm
    success_url = '/kgmawork/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.KgmaWork, id=show_id)

    def form_valid(self, form):
        return super(KgmaWorkUpdateView, self).form_valid(form=form)



#Удаление
class KgmaWorkDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = "/kgmawork/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.KgmaWork, id=show_id)











