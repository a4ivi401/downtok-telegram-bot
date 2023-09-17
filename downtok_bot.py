import telebot
from tiktok_downloader import ttdownloader

bot_token = 'PASTE_YOUR_API_HERE'  # Замените на свой токен бота

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Отправь мне ссылку на видео с TikTok, и я скачаю его для тебя. Автор бота: a4ivi4')

@bot.message_handler(func=lambda message: True)
def download_video(message):
    video_url = message.text
    if 'tiktok.com' in video_url:
        try:
            d = ttdownloader(video_url)
            d[0].download('video.mp4')
            with open('video.mp4', 'rb') as file:
                bot.send_chat_action(message.chat.id, 'upload_video')
                bot.send_video(message.chat.id, file)
            bot.reply_to(message, 'Видео успешно скачано и отправлено!')
        except Exception as e:
            bot.reply_to(message, 'Произошла ошибка при скачивании видео.')
            print(e)
    else:
        bot.reply_to(message, 'Пожалуйста, отправьте ссылку на видео с TikTok.')

bot.polling()
