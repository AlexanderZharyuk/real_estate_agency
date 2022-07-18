# Generated by Django 2.2.24 on 2022-07-18 16:03

from django.db import migrations


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        new_owner, _ = Owner.objects.get_or_create(
            owner_fullname=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        new_owner.owner_flats.add(flat)
        new_owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners)
    ]
