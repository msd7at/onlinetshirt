from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user =    CustomUser(name="hitesh",
                            email="anurag.7140@gmail.com", 
                            is_staff=True,
                            is_superuser=True,
                            phone="9650836604",
                            gender='Male')
        user.set_password("12345")
        user.save()

    dependencies =[

    ]

    operations =[
        migrations.RunPython(seed_data),
    ]