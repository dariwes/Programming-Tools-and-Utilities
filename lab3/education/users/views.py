from django.urls import reverse_lazy
from .forms import UserProfileCreationForm, CourseRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.models import Course


class SignUpView(generic.CreateView):
    template_name = 'users/signup.html'
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('user_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class UserRegistrationCoursesView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseRegistrationForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.users.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_course_detail',
                            args=[self.course.id])


class UserCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'users/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(users__in=[self.request.user])


class UserCourseDetailView(DetailView):
    model = Course
    template_name = 'users/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(users__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = course.modules.all().first()
        return context
