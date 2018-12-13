# Generated by Django 2.1.2 on 2018-12-13 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=150)),
                ('costoPresupuestado', models.IntegerField()),
                ('costoReal', models.IntegerField()),
                ('notaAdicional', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=150)),
                ('nombreSucursal', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Tienda'),
        ),
    ]
