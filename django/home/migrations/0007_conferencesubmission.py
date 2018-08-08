# Generated by Django 2.0.8 on 2018-08-07 21:44

import core.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_add_peer_review_workflow_20180529_1814'),
        ('core', '0002_platform_description_20180520_0549'),
        ('home', '0006_add_submission_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Presentation title', max_length=150)),
                ('abstract', core.fields.MarkdownField(blank=True, help_text='Presentation abstract', max_length=3000, rendered_field=True)),
                ('abstract_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('html', 'html'), ('plain', 'plain'), ('', '')], default='markdown', max_length=30)),
                ('video_url', models.URLField(help_text='URL to your video presentation - YouTube links preferred')),
                ('_abstract_rendered', models.TextField(editable=False)),
                ('model_url', models.URLField(blank=True, help_text='Persistent URL to a model associated with your presentation (if applicable)')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='home.ConferencePage')),
                ('presenters', models.ManyToManyField(to='library.Contributor')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.MemberProfile')),
            ],
        ),
    ]
