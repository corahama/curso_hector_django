# Generated by Django 2.2.3 on 2019-07-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'projecto', 'verbose_name_plural': 'projectos'},
        ),
        migrations.AlterField(
            model_name='project',
            name='autor',
            field=models.CharField(default='', max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Titulo'),
        ),
    ]