# Generated by Django 4.1.6 on 2023-02-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("expense_tracker", "0003_alter_expense_expensetype"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="remarks",
            field=models.TextField(blank=True, default="NA", null=True),
        ),
    ]