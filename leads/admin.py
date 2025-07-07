from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from leads.models import Lead  

class LeadsResource(resources.ModelResource):
    def before_import_instance(self, instance, row, **kwargs):
        user = kwargs.get('user')
        if user and not instance.created_by_id:
            instance.created_by = user

    class Meta:
        model = Lead  
        exclude = ('created_at', 'modified_at') 

class LeadsAdmin(ImportExportModelAdmin):
    resource_class = LeadsResource
    list_display = ('name', 'email', 'mobile_no', 'courses_interested')
    fields = (
        'name', 'father_name', 'mother_name', 'date_of_birth',
        'gender', 'email', 'address', 'courses_interested',
        'academic_qualification', 'mobile_no',
        'known_languages', 'enquiry_via', 'priority', 'facalty'
    )

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        res_kwargs = super().get_import_resource_kwargs(request, *args, **kwargs)
        res_kwargs.update({'user': request.user})
        return res_kwargs

admin.site.register(Lead, LeadsAdmin)  
