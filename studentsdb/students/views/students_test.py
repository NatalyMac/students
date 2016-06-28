from ..models.students import Student
from django.views.generic import ListView

class StudentListTest(ListView):
    model = Student
    context_object_name = 'students'
    template_name = "students/students_list_test.html"

    def get_context_data(self, **kwargs):
        """This method adds extra variables to template"""
        # get original context data from parent class
        context = super(StudentListTest, self).get_context_data(**kwargs)
        # tell template not to show logo on a page
        context['show_logo'] = False
        # return context mapping
        return context

    def get_queryset(self):
        """Order students by last_name."""
        # get original query set
        qs = super(StudentListTest, self).get_queryset()
        # order by last name
        return qs.order_by('first_name')
