# Generated by Django 4.2.19 on 2025-06-15 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_produto_exibir_no_carrinho_produto_is_disponivel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='data_compra',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='total',
            new_name='total_preco',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='compra',
            name='total_itens',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compras', to=settings.AUTH_USER_MODEL),
        ),
    ]
