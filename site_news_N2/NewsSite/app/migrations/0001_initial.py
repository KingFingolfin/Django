# Generated by Django 3.1.7 on 2021-04-24 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='unknown', max_length=128)),
                ('image', models.ImageField(default='images/template.png', upload_to='images')),
                ('link', models.CharField(default='unknown', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'რეკლამა',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=15)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'კონტაქტები',
            },
        ),
        migrations.CreateModel(
            name='Gmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'მეილები',
            },
        ),
        migrations.CreateModel(
            name='OneTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('picture', models.ImageField(default='images/default_picture.png', upload_to='images')),
                ('text', models.TextField()),
                ('nameAuthor', models.CharField(default='unknown', max_length=50)),
                ('imageAuthor', models.ImageField(default='images/default_author.jpg', upload_to='images')),
                ('aboutAuthor', models.TextField(default='...', max_length=500)),
                ('news_type', models.CharField(choices=[('1', 'სხვა'), ('2', 'მეცნიერება'), ('3', 'პოლიტიკა'), ('4', 'ხელოვნება'), ('5', 'ისტორია')], default='1', max_length=128)),
            ],
            options={
                'verbose_name_plural': 'სტატიები',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=700)),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.onetopic')),
            ],
        ),
    ]