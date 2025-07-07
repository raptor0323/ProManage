from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Admission(models.Model):
    # Gender choices
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )
    COLD = 'Cold'
    WARM = 'Warm'
    HOT = 'Hot'
    CHOICES_PRIORITY = (
        (COLD, 'Cold'),
        (WARM, 'Warm'),
        (HOT, 'Hot'),
    )
    # Enquiry via choices
    JD = 'Just Dial'
    SM = 'Social Media'
    Google = 'Google'
    reference = 'Referral'
    EW = 'Event / Workshop'
    enquiry_via = (
        (JD, 'Just Dial'),
        (SM, 'Social Media'),
        (Google, 'Google'),
        (reference, 'Referral'),
        (EW, 'Event / Workshop'),
    )
    # facalty 
    NA = 'SELECT'
    Mrunal_Mam = "Mrunal_Mam"
    Ankita_Mam = "Ankita_Mam"
    Chaitany_Sir = 'Chaitany_Sir'
    Dnyanda_Mam = 'Dnyanda_Mam '
    facalty_via = (
        (Mrunal_Mam,"Mrunal_Mam"),
        (Ankita_Mam,"Ankita_Mam"),
        (Chaitany_Sir,'Chaitany_Sir'),
        (Dnyanda_Mam,'Dnyanda_Mam ')
        )

    # Course choices
    COURSE_CHOICES = (
        ('MS-Office', 'MS-Office'), ('Hardware', 'Hardware'),
        ('Networking', 'Networking'), ('OS (Windows)', 'OS (Windows)'),
        ('OS (Linux)', 'OS (Linux)'), ('CCNA', 'CCNA'),
        ('MCSA', 'MCSA'), ('REDHAT', 'REDHAT'),
        ('Cloud (AWS)', 'Cloud (AWS)'), ('Cloud (Azure)', 'Cloud (Azure)'),
        ('Cyber Security', 'Cyber Security'), ('Ethical Hacking', 'Ethical Hacking'),
        ('Penetration Testing', 'Penetration Testing'),
        ('C & C ++ Programming', 'C & C ++ Programming'),
        ('Data Science', 'Data Science'), ('Data Analytics', 'Data Analytics'),
        ('AI / ML', 'AI / ML'), ('Python Programming', 'Python Programming'),
        ('JAVA', 'JAVA'), ('Mern-Stack', 'Mern-Stack'),
        ('Mean-Stack', 'Mean-Stack'), ('Web', 'Web'),
        ('JAVA Full Stack', 'JAVA Full Stack')
    )

    # Known languages
    KNOWN_LANGUAGES_CHOICES = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Marathi', 'Marathi'),
    )

    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    academic_qualification = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    known_languages = MultiSelectField(choices=KNOWN_LANGUAGES_CHOICES, blank=True)
    priority = models.CharField(max_length=100, choices=CHOICES_PRIORITY, default=WARM)
    gender = models.CharField(max_length=20, choices=GENDER, default=NA)
    enquiry_via = models.CharField(max_length=100, choices=enquiry_via, default=Google)
    facalty = models.CharField(max_length=100, choices=facalty_via, default=NA)
    courses_interested = MultiSelectField(choices=COURSE_CHOICES, blank=True)
    created_by = models.ForeignKey(User, related_name='admissions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name