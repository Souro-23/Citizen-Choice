# Generated by Django 3.0.2 on 2020-01-17 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('hashing', '0004_auto_20200117_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='hash_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hashing',
            name='hash',
        ),
        migrations.AddField(
            model_name='hashing',
            name='field_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='field', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='hashing',
            name='object_id',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='sub_hashing',
        ),
        migrations.AddField(
            model_name='hashing',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='hashing.hash_tags'),
        ),
    ]