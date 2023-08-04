# Generated by Django 3.2.19 on 2023-06-28 22:48

from django.db import migrations


def create_user_spam_status(apps, schema_editor):
    MemberProfile = apps.get_model("core", "MemberProfile")
    UserSpamStatus = apps.get_model("curator", "UserSpamStatus")
    # all_statuses = []
    for mp in MemberProfile.objects.all():
        UserSpamStatus.objects.get_or_create(member_profile=mp)
        # all_statuses.append(status)
    # FIXME: figure out why bulk_create raises an error UserSpamStatus has no attribute 'id'
    # MemberProfile.objects.bulk_create(all_statuses)


def clear_user_spam_status(apps, schema_editor):
    UserSpamStatus = apps.get_model("curator", "UserSpamStatus")
    UserSpamStatus.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("curator", "0003_userspamstatus"),
    ]

    operations = [migrations.RunPython(create_user_spam_status, clear_user_spam_status)]
