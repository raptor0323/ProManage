from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Lead(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDER =(
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )

    JD = 'Just Dial'
    SM = 'Social Media'
    Google = 'Google'
    reference = 'Referral'
    EW = 'Event / Workshop'

    enquiry_via = (
        (JD ,'Just Dial'),
        (SM , 'Social Media'),
        (Google , 'Google'),
        (reference , 'Referral'),
        (EW , 'Event / Workshop'),
    )
    COLD = 'Cold'
    WARM = 'Warm'
    HOT = 'Hot'
    CHOICES_PRIORITY = (
        (COLD, 'Cold'),
        (WARM, 'Warm'),
        (HOT, 'Hot'),
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

    MSOffice = 'MS-Office'
    Hardware = 'Hardware'
    Networking = 'Networking'
    OSW = 'OS (Windows)'
    OSL = 'OS (Linux)'
    CCNA = 'CCNA'
    MCSA = 'MCSA'
    REDHAT = 'REDHAT'
    CAWS = 'Cloud (AWS)'
    CA = 'Cloud (Azure)'
    CB = 'Cyber Security'
    EH = 'Ethical Hacking'
    PT = 'Penetration Testing'
    C = 'C & C ++ Programming'
    DS = 'Data Science'
    DA = 'Data Analytics'
    AIML = 'AI / ML'
    Py = 'Python Programming'
    JAVA = 'JAVA'
    Mern = 'Mern-Stack'
    mean = 'Mean-Stack'
    WB = 'Web'
    JAVAFS = 'JAVA Full Stack'


    COURSE_CHOICES = (
        (MSOffice, 'MS-Office'),(Hardware, 'Hardware'),
        (Networking, 'Networking'),(OSW, 'OS (Windows)'),
        (OSL, 'OS (Linux)'),(CCNA, 'CCNA'),
        (MCSA, 'MCSA'), (REDHAT, 'REDHAT'),
        (CAWS, 'Cloud (AWS)'), (CA, 'Cloud (Azure)'),
        (CB, 'Cyber Security'),(EH, 'Ethical Hacking'),
        (PT, 'Penetration Testing'),
        (C, 'C & C ++ Programming'),(DS, 'Data Science'),
        (DA, 'Data Analytics'), (AIML,'AI / ML'),
        (Py, 'Python Programming'),
        (JAVA, 'JAVA'),(Mern, 'Mern-Stack'),(mean, 'Mean-Stack'),
        (WB, 'Web'),(JAVAFS, 'JAVA Full Stack')
    )

    LANG_ENGLISH = 'English'
    LANG_HINDI = 'Hindi'
    LANG_MARATHI = 'Marathi'
    LANG_FRENCH = 'French'
    KNOWN_LANGUAGES_CHOICES = (
        (LANG_ENGLISH, 'English'),
        (LANG_HINDI, 'Hindi'),
        (LANG_MARATHI, 'Marathi'),
    )

    name = models.CharField(max_length = 255)
    father_name = models.CharField(max_length = 255, blank = True, null=True)
    mother_name = models.CharField(max_length = 255, blank = True, null=True)
    email = models.EmailField()
    address= models.TextField(blank = True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    academic_qualification = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    known_languages = MultiSelectField(choices=KNOWN_LANGUAGES_CHOICES, blank=True, null=True)
    priority = models.CharField(max_length=100, choices=CHOICES_PRIORITY, default=WARM)
    gender = models.CharField(max_length=20, choices=GENDER, default=NA)
    enquiry_via = models.CharField(max_length=100, choices= enquiry_via, default= Google)
    courses_interested = MultiSelectField(choices=COURSE_CHOICES, blank=True, null=True)
    facalty = models.CharField(max_length=100, choices=facalty_via, default=NA)
    converted_to_admission = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name