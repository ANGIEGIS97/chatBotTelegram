import telebot

# Conexión con el BOT
TOKEN = 'PONGAN_SU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# Diccionario de respuestas automáticas
respuestas = {
    "el circuito no enciende": "Fuente de alimentación defectuosa",
    "el voltaje en la salida es bajo": "Resistencia dañada",
    "el capacitor se calienta demasiado": "Falla en el capacitor",
    "la señal tiene mucho ruido": "Interferencia electromagnética"
}

@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    texto = message.text.lower().strip()  # Convierte el mensaje a minúsculas y elimina espacios extra
    respuesta = respuestas.get(texto, "Lo siento, no tengo una respuesta para eso.")
    bot.reply_to(message, respuesta)

if __name__ == "__main__":
    bot.polling(none_stop=True)
