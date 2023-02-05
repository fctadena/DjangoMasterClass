# Generated by Django 4.1.3 on 2022-12-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://w7.pngwing.com/pngs/200/109/png-transparent-cooking-pizza-pasta-android-delicious-pizza-thumbnail.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]