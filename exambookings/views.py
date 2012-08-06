from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from exambookings.models import Booking, Staff
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectTemplateResponseMixin

def any_permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms))

class ShowBookings(ListView):
    model = Booking
    context_object_name="bookings_list"
    template_name = 'exambookings/bookings_list.html'
        
    @method_decorator(any_permission_required('exambookings.teacher_view', 'exambookings.exam_center_view'))
    def dispatch(self, *args, **kwargs):
        return super(ShowBookings, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        theStaff = get_object_or_404(Staff, emailAddress__exact=self.request.user.email)
        return Booking.objects.filter(courseTeacher=theStaff)

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









