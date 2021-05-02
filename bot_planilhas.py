"""
NOTE: This example has been presented at the following course: https://www.udemy.com/course/aprenda-a-programar-um-bot-do-whatsapp
"""

# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd

# Importar arquivo excel
df = pd.read_excel(r'C:\Users\mathe\Downloads\whatsapp_api-master\whatsapp_api-master\exemplo_excel_v2.xlsx')

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
nomes_palavras_chaves = df['Contato']

# Lista dos nomes que vou me referir na mensagem
# primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chaves]
primeiros_nomes = df['Nome']

lista_mensagens = df['Mensagem']

# Loop para mandar mensagens para os clientes
for primeiro_nome, nome_pesquisar, mensagem in zip(primeiros_nomes, nomes_palavras_chaves, lista_mensagens):
    
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()
