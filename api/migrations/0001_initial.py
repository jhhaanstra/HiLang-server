from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('subscribers', models.BigIntegerField(default=0)),
                ('image', models.CharField(max_length=200, null=True)),
                ('public', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('flag', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(null=True)),
                ('grammar', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SentenceStructureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('tag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SentenceStructureQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('correctOrder', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=60)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('distributor', models.PositiveSmallIntegerField(default=0)),
                ('attempt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WordListQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='sentencestructureoption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SentenceStructureQuestion'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='native_lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='native', to='api.Language'),
        ),
        migrations.AddField(
            model_name='course',
            name='trans_lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translation', to='api.Language'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
