# Generated by Django 2.0.7 on 2018-08-03 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_universal', models.BooleanField()),
                ('subject', models.CharField(max_length=30)),
                ('is_affirmative', models.BooleanField()),
                ('predicate', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proof',
            name='conclusion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conclusion', to='proofs.Proposition'),
        ),
        migrations.AddField(
            model_name='proof',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major', to='proofs.Proposition'),
        ),
        migrations.AddField(
            model_name='proof',
            name='minor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minor', to='proofs.Proposition'),
        ),
        migrations.AddField(
            model_name='proof',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
