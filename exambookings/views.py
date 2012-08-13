from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from exambookings.models import Booking #, StaffProfile
from django.views.generic import DetailView, ListView

from django.views.generic.edit import CreateView

def any_permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms))

class StaffOnlyViewMixin(object):
    @method_decorator(any_permission_required('exambookings.teacher_view', 'exambookings.exam_center_view'))
    def dispatch(self, *args, **kwargs):
        return super(StaffOnlyViewMixin, self).dispatch(*args, **kwargs)


class CreateBooking(StaffOnlyViewMixin, CreateView):
    model = Booking
#    template_name_suffix = "_create_form" # looks for template "booking_create_form.html"
    context_object_name = "create_booking"
    template_name = 'exambookings/make_a_booking.html'

    def render_to_response(self, context, **response_kwargs):
        #return django.shortcuts.render_to_response('exambookings/make_a_booking.html', {})
        return super(CreateBooking, self).render_to_response(context, **response_kwargs)
        

class ShowBookings(StaffOnlyViewMixin, ListView):
    model = Booking
    context_object_name="bookings_list"
    template_name = 'exambookings/bookings_list.html'

    def get_queryset(self):
        if (self.request.user.has_perm('exambookings.exam_center_view')):
            bookings = Booking.objects.all()
        elif (self.request.user.has_perm('exambookings.teacher_view')):
            #theStaffBaseProfile = get_object_or_404(BaseProfile, emailAddress__exact=self.request.user.email)
            bookings = Booking.objects.filter(courseTeacherProfile=self.request.user.get_profile().staffProfile)
        else:
            bookings = []

        bookings_list = []
        for booking in bookings:
            bookings_list.append(
                {"studentFirstName": booking.studentProfile.baseProfile.user.first_name,
                 "studentLastName": booking.studentProfile.baseProfile.user.last_name,
                 "course": booking.course,
                 "test": booking.test,
                 "examCenter": booking.examCenter,
                 "courseTeacher": booking.courseTeacherProfile,
                 "workPeriod": booking.workPeriod })
        return bookings_list
        
@login_required
def static_page(request, file_name):
    return render_to_response('exambookings/static_pages/'+file_name, {})


