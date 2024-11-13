import random
from datetime import datetime, timedelta
from telegram import Bot, ParseMode
from telegram.ext import Updater
import time

# Função para gerar sinais de apostas
def gerar_sinal(link):
    grid = [['💣' for _ in range(5)] for _ in range(5)]
    num_mines = random.randint(4, 7)
    
    # Inserir diamantes aleatórios
    for _ in range(25 - num_mines):
        while True:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if grid[x][y] == '💣':
                grid[x][y] = '💎'
                break
    
    grid_str = '\n'.join([''.join(row) for row in grid])
    valido_ate = (datetime.now() + timedelta(minutes=4)).strftime('%H:%M')  # Válido por 4 minutos
    proximo_sinal = (datetime.now() + timedelta(minutes=5)).strftime('%H:%M')  # Próximo sinal
    
    sinal = f"""
SINAL FINALIZADO ✅
AGUARDE ATÉ O PRÓXIMO⏳

ENTRADA VERIFICADA✅

{grid_str}

⏰ Válido até: {valido_ate}
💥 {num_mines} Mines 
🎮 Jogue aqui: [Plataforma bugada aqui]({link})

Novo sinal às {proximo_sinal}.
"""
    return sinal

# Função para enviar sinais automaticamente no canal
def enviar_sinais(bot: Bot, canal_id: str, link: str):
    while True:
        sinal = gerar_sinal(link)
        bot.send_message(chat_id=canal_id, text=sinal, parse_mode=ParseMode.MARKDOWN)
        time.sleep(300)  # Aguarda 5 minutos antes de enviar o próximo sinal

# Configuração do bot
def main():
    TOKEN = '7564052024:AAHNP2lIW7AsVomwv6OAv60r8ajfbUXUETI'  # Substitua pelo token do seu bot
    CANAL_ID = '-1002324559120'  # Substitua pelo nome do canal ou ID (ex: -1001234567890)
    
    LINK_DIRECIONAMENTO = "https://www.tigre-777bet.com/share/5956792"  # Substitua pelo link desejado
    
    bot = Bot(TOKEN)
    print("Bot iniciado. Enviando sinais para o canal...")
    
    # Envia sinais continuamente
    enviar_sinais(bot, CANAL_ID, LINK_DIRECIONAMENTO)

if name == 'main':
    main()