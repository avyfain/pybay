# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-19 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('symposion_proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
            ],
            options={
                'verbose_name': 'talk proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.CreateModel(
            name='TutorialProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('audience_level', models.IntegerField(choices=[(1, 'Novice'), (3, 'Intermediate'), (2, 'Experienced')])),
                ('recording_release', models.BooleanField(default=True, help_text='By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
            ],
            options={
                'verbose_name': 'tutorial proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
    ]