from faker import Faker
from datetime import datetime

print("\n===== Atividade 02 =====\n")

fake = Faker('pt_BR')

agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

nome_cliente = fake.name()
email_cliente = fake.email()
cidade_cliente = fake.city()

print("-" * 40)
print(f"CADASTRO GERADO EM: {data_formatada}")
print("-" * 40)
print(f"Nome do Cliente: {nome_cliente}")
print(f"E-mail: {email_cliente}")
print(f"Cidade: {cidade_cliente}")
print("-" * 40)