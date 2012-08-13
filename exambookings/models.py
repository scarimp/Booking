from django.db import models
#import datetime

#from profiles.models import BaseProfile
from django.contrib.auth.models import User

# Create your models here.
# class StudentProfile(models.Model):
#     baseProfile = models.OneToOneField(BaseProfile,
#                                 unique=True,
#                                 verbose_name= ('base_profile'),
#                                 related_name='studentProfile')
#     grade = models.IntegerField(max_length=2)
#     accomodations = models.TextField(max_length=400)

#     def __unicode__(self):
#         return (self.baseProfile.user.first_name + " " + self.baseProfile.user.last_name + " profile")
    
# class Test(models.Model):
#     name = models.CharField(max_length=40)
#     duration = models.IntegerField(max_length=4)
#     materialRequired = models.TextField(max_length=400)
    
#     def __unicode__(self):
#         return (self.name + " and " + str(self.duration))

# class Course(models.Model):
#     subject = models.CharField(max_length=40)
#     level = models.CharField(max_length=6)
#     students = models.ManyToManyField(StudentProfile, through='StudentBelongsToCourse')
#     tests = models.ManyToManyField(Test, through='CourseAssessedByTest')
#     def __unicode__(self):
#         return (self.subject + " @ " + self.level)

# class WorkPeriod(models.Model):
#     start = models.DateTimeField()
#     end = models.DateTimeField()
    
#     def __unicode__(self):
#         return (str(self.start) + " to " + str(self.end))

# class ExamCenter(models.Model):
#     roomNumber = models.CharField(max_length=15)
#     deskSeats = models.IntegerField(max_length=4)
#     computerSeats = models.IntegerField(max_length=4)
#     materialAvailable = models.TextField(max_length=400)
#     students = models.ManyToManyField(StudentProfile, through='StudentAssignedToExamCenter')
#     workPeriods = models.ManyToManyField(WorkPeriod, through='WorkPeriodAssignedToExamCenter')
    
#     def __unicode__(self):
#         return (self.roomNumber + " with " + str(self.deskSeats) + " and  " + str(self.computerSeats) + " seats")
        
# class StaffProfile(models.Model):
#     baseProfile = models.OneToOneField(BaseProfile,
#                                 unique=True,
#                                 verbose_name= ('base_profile'),
#                                 related_name='staffProfile')
#     courses = models.ManyToManyField(Course, through='StaffTeachingCourse')
#     workPeriods = models.ManyToManyField(WorkPeriod, through='StaffHasAWorkPeriod')
#     speciality = models.TextField(max_length=400)

#     def __unicode__(self):
#         return (self.baseProfile.user.first_name + " " + self.baseProfile.user.last_name + " profile")    


# class Booking(models.Model):
#     studentProfile = models.ForeignKey(StudentProfile)
#     course = models.ForeignKey(Course)
#     test = models.ForeignKey(Test)
#     examCenter = models.ForeignKey(ExamCenter)
#     courseTeacherProfile = models.ForeignKey(StaffProfile)
#     workPeriod = models.ForeignKey(WorkPeriod)

#     class Meta:
#         permissions = (
#             ("teacher_view", "Can view teacher's own bookings"),
#             ("exam_center_view", "Can view all bookings"),
#             )

class Booking(models.Model):
    GRADE_TEN = 10
    GRADE_ELEVEN = 11
    GRADE_TWELVE = 12
    STUDENT_GRADE_CHOICES = (
        (GRADE_TEN, '10'),
        (GRADE_ELEVEN, '11'),
        (GRADE_TWELVE, '12'),
        )
    
    EXAM_CENTER_RM_100 = '100A'
    EXAM_CENTER_CHOICES = (
        (EXAM_CENTER_RM_100, "Main Exam Center - Rm 100"),
        )
    
    PERIOD_TUTORIAL = 830
    PERIOD_ONE = 900
    PERIOD_TWO = 1030
    PERIOD_LUNCH = 1200
    PERIOD_THREE = 1230
    PERIOD_FOUR = 1400
    PERIOD_AFTERSCHOOL = 1530
    TEST_PERIOD_CHOICES = (
        (PERIOD_TUTORIAL, 'Tutorial Time'),
        (PERIOD_ONE, 'Period 1'),
        (PERIOD_TWO, 'Period 2'),
        (PERIOD_LUNCH, 'Lunch Time'),
        (PERIOD_THREE, 'Period 3'),
        (PERIOD_FOUR, 'Period 4'),
        (PERIOD_AFTERSCHOOL, 'After School'),
        )

    # studentProfile = models.ForeignKey(StudentProfile)
    studentFirstName = models.CharField(max_length=30)
    studentLastName = models.CharField(max_length=30)
    studentGrade = models.IntegerField(choices=STUDENT_GRADE_CHOICES,
                                       default=GRADE_TEN)
    
    # course = models.ForeignKey(Course)
    testCourseName = models.CharField(max_length=40)
    
    # test = models.ForeignKey(Test)
    testName = models.CharField(max_length=40)
    testDate = models.DateField()
    testDuration = models.CharField(max_length=40)
    
    # examCenter = models.ForeignKey(ExamCenter)
    examCenter = models.CharField(max_length=5,
                                  choices=EXAM_CENTER_CHOICES,
                                  default=EXAM_CENTER_RM_100)
    
    # courseTeacherProfile = models.ForeignKey(StaffProfile)
    courseTeacher = models.ForeignKey(User)
    
    # workPeriod = models.ForeignKey(WorkPeriod)
    testPeriod = models.IntegerField(choices=TEST_PERIOD_CHOICES,
                                     default=PERIOD_AFTERSCHOOL)

    # accomodations
    extendedTimeAccomodation = models.BooleanField()
    computerAccomodation = models.BooleanField()
    scribeAccomodation = models.BooleanField()
    enlargementsAccomodation = models.BooleanField()
    readerAccomodation = models.BooleanField()
    isolationQuietAccomodation = models.BooleanField()

    # allowances
    ellDictionaryAllowance = models.BooleanField()
    calculatorManipulativesAllowance = models.BooleanField()
    openBookNotesAllowance = models.BooleanField()
    computerInternetAllowance = models.BooleanField()
    englishDictionaryThesaurusAllowance = models.BooleanField()
    otherAllowances = models.CharField(max_length=200, blank=True)

    class Meta:
        permissions = (
            ("teacher_view", "Can view teacher's own bookings"),
            ("exam_center_view", "Can view all bookings"),
            )
        

#Relations
# class StudentBelongsToCourse(models.Model):
#     student = models.ForeignKey(StudentProfile)
#     course = models.ForeignKey(Course)
    
# class StudentAssignedToExamCenter(models.Model):
#     student = models.ForeignKey(StudentProfile)
#     examCenter = models.ForeignKey(ExamCenter)
    
# class CourseAssessedByTest(models.Model):
#     test = models.ForeignKey(Test)
#     course = models.ForeignKey(Course)

# class StaffTeachingCourse(models.Model):
#     staff = models.ForeignKey(StaffProfile)
#     course = models.ForeignKey(Course)

# class StaffHasAWorkPeriod(models.Model):
#     staff = models.ForeignKey(StaffProfile)
#     workPeriod = models.ForeignKey(WorkPeriod)
    
# class WorkPeriodAssignedToExamCenter(models.Model):
#     examCenter = models.ForeignKey(ExamCenter)
#     workPeriod = models.ForeignKey(WorkPeriod)
    
# class StudentTakingTest(models.Model):
#     test = models.ForeignKey(Test)
#     student = models.ForeignKey(StudentProfile)
#     dateCompleted = models.DateField()

