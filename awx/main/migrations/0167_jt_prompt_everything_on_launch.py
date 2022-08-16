# Generated by Django 3.2.13 on 2022-08-16 11:40

import awx.main.fields
import awx.main.utils.polymorphic
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0166_alter_jobevent_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblaunchconfig',
            name='execution_environment',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=awx.main.utils.polymorphic.SET_NULL,
                related_name='execution_environment',
                to='main.executionenvironment',
            ),
        ),
        migrations.AddField(
            model_name='joblaunchconfig',
            name='labels',
            field=models.ManyToManyField(related_name='joblaunchconfig_labels', to='main.Label'),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_execution_environment_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_forks_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_instance_groups_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_job_slice_count_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_labels_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='ask_timeout_on_launch',
            field=awx.main.fields.AskForField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='labels',
            field=models.ManyToManyField(related_name='schedule_labels', to='main.Label'),
        ),
        migrations.AddField(
            model_name='workflowjobnode',
            name='labels',
            field=models.ManyToManyField(related_name='workflowjobnode_labels', to='main.Label'),
        ),
        migrations.AddField(
            model_name='workflowjobtemplatenode',
            name='labels',
            field=models.ManyToManyField(related_name='workflowjobtemplatenode_labels', to='main.Label'),
        ),
        migrations.CreateModel(
            name='JobLaunchConfigInstanceGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(db_index=True, default=None, null=True)),
                ('instancegroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instancegroup')),
                ('joblaunchconfig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.joblaunchconfig')),
            ],
        ),
        migrations.CreateModel(
            name='JobInstanceGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(db_index=True, default=None, null=True)),
                ('instancegroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instancegroup')),
                ('unifiedjob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='instance_groups',
            field=awx.main.fields.OrderedManyToManyField(
                blank=True, editable=False, related_name='job_instance_groups', through='main.JobInstanceGroupMembership', to='main.InstanceGroup'
            ),
        ),
        migrations.AddField(
            model_name='joblaunchconfig',
            name='instance_groups',
            field=awx.main.fields.OrderedManyToManyField(
                blank=True, editable=False, related_name='joblaunchconfigs', through='main.JobLaunchConfigInstanceGroupMembership', to='main.InstanceGroup'
            ),
        ),
    ]
