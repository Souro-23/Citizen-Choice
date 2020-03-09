# Generated by Django 3.0.2 on 2020-01-16 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_postsarticle_hash_tags'),
        ('hashing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_hashing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hash', to='post.PostsArticle')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hash', to='post.FeedPosts')),
            ],
        ),
        migrations.AddField(
            model_name='hashing',
            name='hash',
            field=models.ManyToManyField(to='hashing.sub_hashing'),
        ),
        migrations.AddField(
            model_name='hashing',
            name='key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hash_key', to='hashing.sub_hashing'),
        ),
    ]
