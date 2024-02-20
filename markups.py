from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


btnBtc = InlineKeyboardButton(text='BTC', callback_data ='cc_bitcoin')
btnLtc = InlineKeyboardButton(text='LTC', callback_data ='cc_litecoin')
btnSol = InlineKeyboardButton(text='SOL', callback_data ='cc_solana')
btnDoge = InlineKeyboardButton(text='DOGE', callback_data ='cc_dogecoin')
btnTeth = InlineKeyboardButton(text='TETHER', callback_data ='cc_tether')
#create keyboard menu

coinlist = InlineKeyboardMarkup(row_width=1)
coinlist.insert(btnBtc)
coinlist.insert(btnLtc)
coinlist.insert(btnSol)
coinlist.insert(btnDoge)
coinlist.insert(btnTeth)
