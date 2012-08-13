from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from exambookings.models import Booking, StaffProfile
from django.views.generic import DetailView, ListView


def any_permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms))

class StaffOnlyViewMixin(object):
    @method_decorator(any_permission_required('exambookings.teacher_view', 'exambookings.exam_center_view'))
    def dispatch(self, *args, **kwargs):
        return super(StaffOnlyViewMixin, self).dispatch(*args, **kwargs)

class ShowBookings(StaffOnlyViewMixin, ListView):
    model = Booking
    context_object_name="bookings_list"
    template_name = 'exambookings/bookings_list.html'
        

    def get_queryset(self):
        if (self.request.user.has_perm('exambookings.exam_center_view')):
            bookings = Booking.objects.all()
        elif (self.request.user.has_perm('exambookings.teacher_view')):
            #theStaffBaseProfile = get_object_or_404(BaseProfile, emailAddress__exact=self.request.user.email)
            bookings = Booking.objects.filter(courseTeacherProfile=self.request.user.baseProfile.staffProfile)
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


##
# Original Code
##
# def index(request):
#     def index(request):
#     	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     return render_to_response('exambookings/index.html', {'latest_poll_list': latest_poll_list})

# def detail(request, poll_id):
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	return render_to_response('exambookings/detail.html', {'poll': p},
#                            context_instance=RequestContext(request))

# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('exambookings/results.html', {'poll': p})

# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render_to_response('exambookings/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         }, context_instance=RequestContext(request))
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))









