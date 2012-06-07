from exambookings.models import *
#from exambookings.models import Student
from django.contrib import admin

#Relationships
class StudentBelongsToCourseInline(admin.TabularInline):
    model = StudentBelongsToCourse
    extra = 1
class CourseAssessedByTestInline(admin.TabularInline):
    model = CourseAssessedByTest
    extra = 1
class StudentTakingTestInline(admin.TabularInline):
    model = StudentTakingTest
    extra = 1
class StudentAssignedToExamCenterInline(admin.TabularInline):
    model = StudentAssignedToExamCenter
    extra = 1
class StaffTeachingCourseInline(admin.TabularInline):
    model = StaffTeachingCourse
    extra = 1
class WorkPeriodAssignedToExamCenterInline(admin.TabularInline):
    model = WorkPeriodAssignedToExamCenter
    extra = 1
class StaffHasAWordPeriodInline(admin.TabularInline):
    model = StaffHasAWorkPeriod
    extra = 1
#Model.Admins
class TestAdmin(admin.ModelAdmin):
    model = Test
    inlines = (CourseAssessedByTestInline,StudentTakingTestInline)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['firstName']}),
        (None, {'fields': ['lastName']}),
        (None, {'fields': ['emailAddress']}),
        (None, {'fields': ['grade']}),
        (None, {'fields': ['accomodations']}),
    ]
    inlines = (StudentBelongsToCourseInline,)
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']}),
        (None, {'fields': ['level']}),
    ]
#Registering
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(ExamCenter)
admin.site.register(Staff)
admin.site.register(WorkPeriod)
admin.site.register(Booking)

##
# Original Code
##
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
