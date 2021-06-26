# Generated by Django 3.2 on 2021-06-21 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('Visited_place', models.CharField(blank=True, max_length=500)),
                ('categories', models.CharField(blank=True, max_length=300)),
                ('bloger_name', models.CharField(blank=True, max_length=400)),
                ('blog_title', models.CharField(blank=True, max_length=900)),
                ('blog_link', models.URLField(blank=True, max_length=900)),
                ('image_blog', models.ImageField(blank=True, upload_to='media/blog_images')),
            ],
        ),
        migrations.CreateModel(
            name='Add_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(blank=True, max_length=500, null=True)),
                ('number_of_visited_places', models.CharField(blank=True, max_length=300, null=True)),
                ('tour_location', models.CharField(blank=True, max_length=300, null=True)),
                ('tour_tittle', models.CharField(blank=True, max_length=900, null=True)),
                ('day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=100)),
                ('night', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=100)),
                ('charges', models.CharField(blank=True, max_length=200)),
                ('highlight', models.CharField(blank=True, max_length=2000)),
                ('max_people', models.CharField(blank=True, max_length=300)),
                ('start_date', models.DateField(default='dd/mm/yy')),
                ('last_date', models.DateField(default='dd/mm/yy')),
                ('pickup_address', models.CharField(blank=True, max_length=400)),
                ('retuen_location', models.CharField(blank=True, max_length=400)),
                ('bedroom', models.CharField(blank=True, max_length=400)),
                ('depature_time', models.TimeField(default='hh:mm:ss')),
                ('what_to_expect', models.CharField(blank=True, max_length=1000, null=True)),
                ('day1_rout', models.CharField(blank=True, max_length=1000, null=True)),
                ('day1_visited_place', models.CharField(blank=True, max_length=1000, null=True)),
                ('day2_rout', models.CharField(blank=True, max_length=1000, null=True)),
                ('day2_visited_place', models.CharField(blank=True, max_length=1000, null=True)),
                ('day3_rout', models.CharField(blank=True, max_length=1000)),
                ('day3_visited_place', models.CharField(blank=True, max_length=1000, null=True)),
                ('day4_rout', models.CharField(blank=True, max_length=1000)),
                ('day4_visited_place', models.CharField(blank=True, max_length=1000)),
                ('map_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('image1', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('image2', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('image3', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('image4', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('image5', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('image6', models.ImageField(null=True, upload_to='media/tour_images/')),
                ('status', models.CharField(default='destination', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messagess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=300)),
                ('lname', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=300)),
                ('message', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('number', models.CharField(blank=True, max_length=200)),
                ('otp', models.CharField(blank=True, max_length=5)),
                ('status', models.CharField(default='Valid', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registered_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('number', models.CharField(blank=True, max_length=20)),
                ('password', models.CharField(blank=True, max_length=20)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('twitter_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('father_name', models.CharField(blank=True, max_length=400)),
                ('address', models.CharField(blank=True, max_length=400)),
                ('zip_code', models.CharField(blank=True, max_length=400)),
                ('country', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(blank=True, max_length=400)),
                ('profile', models.ImageField(blank=True, upload_to='media/profile/')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300)),
                ('comment', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='txn_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('txnid', models.CharField(max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('txndate', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(default='pendding', max_length=200)),
                ('tour', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='travel.add_tour')),
            ],
        ),
    ]