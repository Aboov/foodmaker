from platform import processor
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import os
from food import food
TOKEN=os.environ["TOKEN"]
USERNAME="@Dadfoodiebot"
#Commands
async def star_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello thanks for chating with me I am not a banana")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is help")

async def food_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("please send enter the ingredients in this format ingredients:apple,banana... ")

#Responses
def handel_response(text:str):
    processed:str =text.lower()
    if 'ingredients:' in processed:
        processed.replace("ingredients:","").strip()
        recipe=food()
        return recipe.Get_recipe_based_on_ingredients(ingredients=processed)
    else:
        return "sad"

async def hande_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str=update.message.chat.type
    text:str =update.message.text

    print(f"User({update.message.chat.id}) in {message_type}: '{text}'")
    if message_type == "group":
        if USERNAME in text:
            new_text:str=text.replace(USERNAME,"").strip()
            response:str=handel_response(new_text)
        else:
            return
    else:
        response:str=handel_response(text)
    print("bot:",response)
    await update.message.reply_text(response)


async def error(update:Update,conext:ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} casued error {conext.error}")
if __name__=='__main__':
    print("starting bot")
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",star_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", food_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT,hande_message))

    #erros
    app.add_error_handler(error)
    print("polling")
    app.run_polling(poll_interval=3)