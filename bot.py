from telegram.ext import Updater, CommandHandler
import random, os

if os.path.exists('sentences.txt'):
    with open('sentences.txt') as FILE:
        sentences = [sentence.strip() for sentence in FILE]
else:
    sentences = []

if os.path.exists('predictions.txt'):
    with open('predictions.txt') as FILE:
        prediction = [prediction.strip() for prediction in FILE]
else:
    prediction = []

def start(update, context):
    update.message.reply_text("hello")
def hello(update, context):
    update.message.reply_text(
        '你好, {} 你這臭GG'.format(update.message.from_user.first_name))

def trash_talk(update, context):
    if sentences:
        update.message.reply_text(random.choice(sentences))
    else:
        update.message.reply_text('I have no words.')
def add(update, context):
    # print('from user:', update.message.from_user.id)
    # 限制只有特定人才能新增語錄
    if update.message.from_user.id == 856419041:
        sentence = update.message.text[5:].replace('\n', ' ')
        sentences.append(sentence)
        with open('sentences.txt', 'a') as FILE:
            print(sentence, file=FILE)
        update.message.reply_text('已加入：' + sentence)
    else:
        update.message.reply_text('只有岳澄能加拉><.')

def today(update, context):
    update.message.reply_text(random.choice(prediction))
def turn_egg(update, context):
    #update.message.reply_text("UR SSR SR R 機率為:1 4 15 80")
    pro = random.randint(1, 100)
    if pro == 1:
        update.message.reply_text("你抽到的是: UR")
        update.message.reply_text("看來你是個超級賽狗呢")
    elif pro <= 5:
        update.message.reply_text("你抽到的是: SSR")
    elif pro <= 20:
        update.message.reply_text("你抽到的是: SR")
    else:
        update.message.reply_text("你抽到的是: R")

def turn_egg_ten(update, context):
    #update.message.reply_text("UR SSR SR R 機率為:1 4 15 80")
    UR = 0
    SSR = 0
    SR = 0
    R = 0
    for i in range(10):
        pro = random.randint(1, 100)

        if pro == 1:
            UR = UR + 1
        elif pro <= 5:
            SSR = SSR + 1
        elif pro <= 20:
            SR = SR + 1
        else:
            R = R + 1
    update.message.reply_text("十連抽結果為: \n%d個UR \n%d個SSR \n%d個SR \n%d個R" %(UR , SSR , SR , R))


updater = Updater(your_token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('trash_talk', trash_talk))
updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('today', today))
updater.dispatcher.add_handler(CommandHandler('turn_egg', turn_egg))
updater.dispatcher.add_handler(CommandHandler('turn_egg_ten', turn_egg_ten))

updater.start_polling()
updater.idle()