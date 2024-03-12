from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from login import Telegram_Token
from pytube import YouTube


async def Descargar(update: Update,context:ContextTypes.DEFAULT_TYPE):
        print(update.message.text)
        #update.message.text;
        yt = YouTube(update.message.text)
        descarga=yt.streams.get_highest_resolution()
        descarga.download();


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')



app = ApplicationBuilder().token(Telegram_Token).build()

app.add_handler(CommandHandler("hello",hello))
app.add_handler(CommandHandler("echo",Descargar))

app.run_polling(allowed_updates=Update.ALL_TYPES)






