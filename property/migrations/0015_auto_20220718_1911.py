# Generated by Django 2.2.24 on 2022-07-18 16:03
from itertools import chain


from django.db import migrations


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats_iterator = Flat.objects.all().iterator()

    try:
        first_iteration = next(flats_iterator)
    except StopIteration:
        return None
    for flat in chain([first_iteration], flats_iterator):
        new_owner, _ = Owner.objects.get_or_create(
            owner_fullname=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        new_owner.owner_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners)
    ]
