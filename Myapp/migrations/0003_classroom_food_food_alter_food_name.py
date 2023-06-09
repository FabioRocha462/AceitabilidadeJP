# Generated by Django 4.1.7 on 2023-03-15 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom_food',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.food'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(choices=[('BISCOITO ROSQUINHA COM SUCO VITAMINA DE GOIABA E FRUTA', 'BISCOITO ROSQUINHA COM SUCO VITAMINA DE GOIABA E FRUTA'), ('BISCOITO MARIA OU CREAM CRACKER COM SUCO', 'BISCOITO MARIA OU CREAM CRACKER COM SUCO'), ('ARROZ COM FEIJÃO E FRANGO GUISADO', 'ARROZ COM FEIJÃO E FRANGO GUISADO'), ('SOPA DE FRANGO COM ESPAGUETE E LEGUMES', 'SOPA DE FRANGO COM ESPAGUETE E LEGUMES'), ('BEIJU COM MARGARINA E CAFÉ COM LEITE', 'BEIJU COM MARGARINA E CAFÉ COM LEITE'), ('CUSCUZ RECHEADO COM OVOS MEXIDOS E SUCO', 'CUSCUZ RECHEADO COM OVOS MEXIDOS E SUCO'), ('BAIÃO DE 2 COM MACAXEIRA, CARNE BOVINA E SUCO', 'BAIÃO DE 2 COM MACAXEIRA, CARNE BOVINA E SUCO'), ('TAPIOCA COM QUEIJO COALHO E VITAMINA DE DE GOIABA', 'TAPIOCA COM QUEIJO COALHO E VITAMINA DE GOIABA'), ('ARROZ DE LEITE COM PAÇOCA DE CARNES DE SOL', 'ARROZ DE LETE COM PAÇOCA DE CARNE DE SOL'), ('CUSCUZ RECHEADO COM CARNE MOÍDA E SUCO', 'CUSCUZ RECHEADO COM CARNE MOÍDA'), ('CACHORRO QUENTE COM MOLHO DE CARNE MOÍDA DE SUCO', 'CACHORRO QUENTE COM MOLHO DE CARNE MOÍDA E SUCO'), ('RISOTO DE FRANGO COM LEGUMES', 'RISOTO DE FRANGO COM LEGUMES'), ('BOLO DE CACO E CAFÉ COM LEITE', 'BOLO DE CACO E CAFÉ COM LEITE'), ('TAPIOCA RECHEADA COM OVOS MEXIDOS E SUCO DE POLPA', 'TAPIOCA RECHEADA COM OVOS MEXIDOS E SUCO DE POLPA'), ('MUNGUNZÁ COM FRANGO AO MOLHO BRANCO', 'MUNGUNZÁ COM FRANGO AO MOLHO BRANCO'), ('SOPA DE CARNE BOVINA COM MACARRÃO E LEGUMES', 'SOPA DE CARNE BOVINA COM MACARRÃO E LEGUMES'), ('MACARRONADA DE FRANGO', 'MACARRONADA DE FRANGO'), ('BOLO SIMPLES COM VITAMINA DE BANANA E AVEIA', 'BOLO SIMPLES COM VITAMINA DE BANANA E AVEIA'), ('CANJA DE FRANGO COM BATATA INGLESA E CENOURA', 'CANJA DE FRANGO COM BATATA INGLESA E CENOURA'), ('BAIÃO DE 2 COM CARNE BOVINA E VINAGRETE', 'BAIÃO DE 2 COM CARNE BOVINA E VINAGRETE'), ('MACARRONADA DE CARNE MOÍDA', 'MACARRONADA DE CARNE MOÍDA')], max_length=255),
        ),
    ]
