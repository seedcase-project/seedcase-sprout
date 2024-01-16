# Generated by Django 4.2.8 on 2024-01-16 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnDataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TableMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('original_file_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ColumnMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('allow_missing_value', models.BooleanField()),
                ('allow_duplicate_value', models.BooleanField()),
                ('data_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.columndatatype')),
                ('table_metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tablemetadata')),
            ],
        ),
    ]
