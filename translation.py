from pyrogram.types import InlineKeyboardButton


class Translation(object):
    START_TEXT = "Hi {},\nI'm MangaLoader!\nYou can upload any manga to Telegram as Zipfile!\n\n/help for more details!"
    HELP_TEXT = "How to use MangaLoader?!\n\n1. Send manga url from [supported resources](https://github.com/X-Gorn/MangaLoader/tree/cleandir#url-options-and-examples)\n2. Choose subdir option. (will uploaded as Zipfile)\n3. Wait a few minutes and you will receive your archived manga\n\nIf bot didn't respond, contact @GhoulHaise2"
    UPLOAD = 'Choose subdirs option. (will uploaded as Zipfile)'
    CLEANDIR_SUCCESS = 'Successfully cleaned your download dir, now you can sent another link'
    CLEANDIR_UNSUCCESS = 'Your download dir are empty, use this command only if your bot are stuck'
    
    upload_buttons=[
        [
            InlineKeyboardButton('as PDF', callback_data='pdf'),
            InlineKeyboardButton('as ZIP', callback_data='zip'),
        ],
        [InlineKeyboardButton('as Folder', callback_data='folder')],
    ]
    
    start_buttons=[
        [
            InlineKeyboardButton('ᴄʜᴀᴛ ɢʀᴏᴜᴘ', url='https://t.me/anime_chat_ocean'), 
            InlineKeyboardButton('ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/anime_ocean'),
        ],
        [InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/GhoulHaise2')],
    ]
