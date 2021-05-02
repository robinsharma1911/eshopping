# Generated by Django 3.1.2 on 2020-10-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logs', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='carts_db',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_db')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.log_db')),
            ],
        ),
    ]
