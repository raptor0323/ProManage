# Generated by Django 5.1.6 on 2025-03-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0003_rename_converted_to_client_lead_converted_to_admission"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="enquiry_via",
            field=models.CharField(
                choices=[
                    ("Just Dial", "Just Dial"),
                    ("Social Media", "Social Media"),
                    ("Google", "Google"),
                    ("Referral", "Referral"),
                    ("Event / Workshop", "Event / Workshop"),
                ],
                default="Google",
                max_length=100,
            ),
        ),
    ]
