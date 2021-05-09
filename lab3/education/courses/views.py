from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Course
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet


# можно применять для любого обработчика,
# который работает с моделью, содержащей поле owner
class OwnerMixin:
    # получать только те объекты,
    # владельцем которых является текущий пользователь (request.user)
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    # автоматически заполнять поле owner сохраняемого объекта.
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    # модель, с которой работает обработчик
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin):
    # поля модели, из которых будет формироваться объект
    # обработчиками CreateView и UpdateView
    fields = ['subject', 'title', 'slug', 'overview']
    # адрес, на который пользователь будет перенаправлен
    # после успешной обработки формы классами CreateView и UpdateView
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'


# список курсов, созданных пользователем
class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        qs = super(ManageCourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class CourseCreateView(OwnerCourseEditMixin,
                       OwnerEditMixin,
                       CreateView,
                       PermissionRequiredMixin):
    # проверка наличия у пользователя разрешения
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin,
                       UpdateView,
                       PermissionRequiredMixin):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin,
                       DeleteView,
                       PermissionRequiredMixin):
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')
    permission_required = 'courses.delete_course'


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    # отвечает за формирование набора форм
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course, 'formset': formset})
