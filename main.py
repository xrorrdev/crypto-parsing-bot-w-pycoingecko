import logging
from aiogram import Bot, Dispatcher, executor, types
from pycoingecko import CoinGeckoAPI

import markups as nav


logging.basicConfig(level=logging.INFO)

bot = Bot('Your bot Token ')
dp = Dispatcher(bot)
cg = CoinGeckoAPI()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Choose coin", reply_markup=nav.coinlist)
#sending start msg

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        result = cg.get_price(ids=message.text, vs_currencies='usd,rub')
        #get price from ids
        if message.text in result:
            cost1name = result[message.text]['usd']
            cost2name = result[message.text]['rub']
            await bot.send_message(message.from_user.id, f"Chosen coin: {message.text}\nPrice in USD: {cost1name}$\nPrice in RUB: {cost2name}₽")
        else:
            await bot.send_message(message.from_user.id, f"Coin {message.text} not found.")


@dp.callback_query_handler(text_contains='cc_')
async def crypt(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    currency = str(callback_data[3:])
    res = cg.get_price(ids=currency, vs_currencies='usd,rub')
#get price for user search
    if currency in res:
        cost1 = res[currency]['usd']
        cost2 = res[currency]['rub']
        await bot.send_message(call.from_user.id, f"Chosen coin: {currency}\nPrice in USD: {cost1}$\nPrice in RUB: {cost2}₽", reply_markup=nav.coinlist)
    else:
        await bot.send_message(call.from_user.id, f"Can't find information about this coin {currency}", reply_markup=nav.coinlist)

executor.start_polling(dp)
#start polling xD