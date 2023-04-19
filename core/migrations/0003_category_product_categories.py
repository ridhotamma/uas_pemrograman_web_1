# Generated by Django 4.2 on 2023-04-19 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_product_options_alter_sales_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(to="core.category"),
        ),
    ]
