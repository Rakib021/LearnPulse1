# Generated by Django 4.2.3 on 2023-09-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_course_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='Media/featured_img'),
        ),
    ]
