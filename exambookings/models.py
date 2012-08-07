from django.db import models
import datetime

from django.contrib.auth.models import User

# Create your models here.
# class Student(models.Model):
#     firstName = models.CharField(max_length=25)
#     lastName = models.CharField(max_length=25)
#     emailAddress = models.EmailField(max_length=254)
#     grade = models.IntegerField(max_length=2)
#     accomodations = models.TextField(max_length=400)
    
#     def __unicode__(self):
#         return (self.firstName + " and " + str(self.emailAddress))
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name= ('user'),
                                related_name='student_profile')
    grade = models.IntegerField(max_length=2)
    accomodations = models.TextField(max_length=400)
    
class Test(models.Model):
    name = models.CharField(max_length=40)
    duration = models.IntegerField(max_length=4)
    materialRequired = models.TextField(max_length=400)
    
    def __unicode__(self):
        return (self.name + " and " + str(self.duration))

class Course(models.Model):
    subject = models.CharField(max_length=40)
    level = models.CharField(max_length=6)
    students = models.ManyToManyField(StudentProfile, through='StudentBelongsToCourse')
    tests = models.ManyToManyField(Test, through='CourseAssessedByTest')
    def __unicode__(self):
        return (self.subject + " @ " + self.level)

class WorkPeriod(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __unicode__(self):
        return (str(self.start) + " to " + str(self.end))

class ExamCenter(models.Model):
    roomNumber = models.CharField(max_length=15)
    deskSeats = models.IntegerField(max_length=4)
    computerSeats = models.IntegerField(max_length=4)
    materialAvailable = models.TextField(max_length=400)
    students = models.ManyToManyField(StudentProfile, through='StudentAssignedToExamCenter')
    workPeriods = models.ManyToManyField(WorkPeriod, through='WorkPeriodAssignedToExamCenter')
    
    def __unicode__(self):
        return (self.roomNumber + " with " + str(self.deskSeats) + " and  " + str(self.computerSeats) + " seats")
        
# class Staff(models.Model):
#     name = models.CharField(max_length=25)
#     emailAddress = models.EmailField(max_length=254)
#     speciality = models.TextField(max_length=400)
#     courses = models.ManyToManyField(Course, through='StaffTeachingCourse')
#     workPeriods = models.ManyToManyField(WorkPeriod, through='StaffHasAWorkPeriod')
    
#     def __unicode__(self):
#         return (self.name + " and " + str(self.emailAddress))

class StaffProfile(models.Model):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name= ('user'),
                                related_name='staff_profile')
    courses = models.ManyToManyField(Course, through='StaffTeachingCourse')
    workPeriods = models.ManyToManyField(WorkPeriod, through='StaffHasAWorkPeriod')
    speciality = models.TextField(max_length=400)


class Booking(models.Model):
    student = models.ForeignKey(StudentProfile)
    course = models.ForeignKey(Course)
    test = models.ForeignKey(Test)
    examCenter = models.ForeignKey(ExamCenter)
    courseTeacher = models.ForeignKey(StaffProfile)
    workPeriod = models.ForeignKey(WorkPeriod)

    class Meta:
        permissions = (
            ("teacher_view", "Can view teacher's own bookings"),
            ("exam_center_view", "Can view all bookings"),
            )


#Relations
class StudentBelongsToCourse(models.Model):
    student = models.ForeignKey(StudentProfile)
    course = models.ForeignKey(Course)
    
class StudentAssignedToExamCenter(models.Model):
    student = models.ForeignKey(StudentProfile)
    examCenter = models.ForeignKey(ExamCenter)
    
class CourseAssessedByTest(models.Model):
    test = models.ForeignKey(Test)
    course = models.ForeignKey(Course)

class StaffTeachingCourse(models.Model):
    staff = models.ForeignKey(StaffProfile)
    course = models.ForeignKey(Course)

class StaffHasAWorkPeriod(models.Model):
    staff = models.ForeignKey(StaffProfile)
    workPeriod = models.ForeignKey(WorkPeriod)
    
class WorkPeriodAssignedToExamCenter(models.Model):
    examCenter = models.ForeignKey(ExamCenter)
    workPeriod = models.ForeignKey(WorkPeriod)
    
class StudentTakingTest(models.Model):
    test = models.ForeignKey(Test)
    student = models.ForeignKey(StudentProfile)
    dateCompleted = models.DateField()


    
# ##
# # Original Code
# ##

# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __unicode__(self):
#         return self.question
    
#     def was_published_today(self):
#         return self.pub_date.date() == datetime.date.today()
#     was_published_today.short_description = 'Published today?'

# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField()

#     def __unicode__(self):
#         return self.choice
