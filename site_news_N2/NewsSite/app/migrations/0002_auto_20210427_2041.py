# Generated by Django 3.1.7 on 2021-04-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=1000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.onetopic')),
            ],
            options={
                'verbose_name_plural': 'კომენტარები',
            },
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]