# Generated by Django 2.0.7 on 2018-08-30 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('dt_nascimento', models.DateField(blank=True, max_length=10, null=True, verbose_name='Data de Nascimento')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('perfil', models.CharField(choices=[('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor')], max_length=1, verbose_name='Perfil')),
                ('status_user', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_fiscal', models.CharField(choices=[('PF', 'Pessoal Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Classificação fiscal')),
                ('clientename', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('numero_fiscal', models.CharField(max_length=14, unique=True, verbose_name='CNPJ/CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_fiscal', models.CharField(choices=[('PF', 'Pessoal Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Classificação fiscal')),
                ('fornecedorname', models.CharField(max_length=200, verbose_name='Fornecedor')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('numero_fiscal', models.CharField(max_length=14, unique=True, verbose_name='CNPJ/CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'db_table': 'Fornecedor',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100, verbose_name='Nome do Material')),
                ('tipo_mprima', models.CharField(max_length=50, verbose_name='Tipo de Material')),
                ('classificacao', models.CharField(max_length=50, verbose_name='Classificação do Material')),
                ('cor', models.CharField(max_length=50, verbose_name='Cor do Material')),
                ('cod_mprima', models.CharField(max_length=50, verbose_name='Código do Material')),
                ('nome_fabricante', models.CharField(max_length=50, verbose_name='Nome do Fabricante')),
            ],
            options={
                'db_table': 'Material',
            },
        ),
        migrations.CreateModel(
            name='PrestadorServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_fiscal', models.CharField(choices=[('PF', 'Pessoal Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Classificação fiscal')),
                ('prestadorname', models.CharField(max_length=200, verbose_name='Prestador de Serviço')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('numero_fiscal', models.CharField(max_length=14, unique=True, verbose_name='CNPJ/CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'db_table': 'Prestador',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_produto', models.CharField(max_length=50, verbose_name='Tipo de Produto')),
                ('produto', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('modelo', models.CharField(choices=[('Ux', 'Unissex'), ('F', 'Feminino'), ('M', 'Masculino')], max_length=2, verbose_name='Modelo do produto')),
                ('classificacao', models.CharField(max_length=50, verbose_name='Classificação do Produto')),
                ('tamanho', models.CharField(choices=[('Único', 'Único'), ('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG'), ('2G', '2G'), ('3G', '3G'), ('4G', '4G'), ('XG', 'XG'), ('EXG', 'EXG')], max_length=5, verbose_name='Tamanho do Produto')),
                ('cor', models.CharField(max_length=50, verbose_name='Cor do Produto')),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Produto')),
                ('especificacao', models.TextField(max_length=1000, verbose_name='Especificação do Produto')),
            ],
            options={
                'db_table': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servico', models.CharField(choices=[('Fabricação', 'Fabricação'), ('Reparo', 'Reparo')], max_length=10, verbose_name='Tipo de Serviço')),
                ('servico', models.CharField(choices=[('Costura', 'Costura'), ('Estampa', 'Estampa'), ('Bordado', 'Bordado')], max_length=7, verbose_name='Serviço')),
                ('valor_peca', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Peça')),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
            ],
            options={
                'db_table': 'Servico',
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_unidade', models.FloatField(verbose_name='Quantidade por unidade')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
                ('tecido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Material')),
            ],
            options={
                'db_table': 'Medida',
            },
        ),
    ]
