# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE
 
import re, random, asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from LuciferMoringstar_Robot import temp, PICS, MOVIE_TEXT as REQUEST_TEXT, FILTER_DEL_SECOND
from LuciferMoringstar_Robot.functions import get_size, split_list, get_settings
from database.autofilter_mdb import get_filter_results

async def group_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", update.text):
        return
    if 1 < len(message.text) < 100:    
        btn = []
        search = message.text
        mo_tech_yt = f">✪ {search} </b><b>𝙐𝙥𝙡𝙤𝙖𝙙𝙚𝙙 𝘽𝙮 ☟</b>\n<b>@ReQuest_Movies_V3</b>\n<b>⚜ 𝙁𝙤𝙪𝙣𝙙𝙚𝙙 𝙍𝙚𝙨𝙪𝙡𝙩𝙨 𝙁𝙤𝙧 𝙔𝙤𝙪𝙧</b>\n<b>𝙍𝙚𝙦𝙪𝙚𝙨𝙩 💚</b>"
        nyva=BOT.get("username")
        if not nyva:
            botusername=await client.get_me()
            nyva=botusername.username
            BOT["username"]=nyva
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"[{get_size(file.file_size)}] {file.file_name}"
                btn.append(
                        [InlineKeyboardButton(text=f"{filename}", url=f"https://telegram.dog/{nyva}?start=pr0fess0r_99_-_-_-_{file_id}")]
                        )
        else:
            one_button = InlineKeyboardMarkup([[InlineKeyboardButton("✆ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴀᴅᴍɪɴ", url="http://t.me/AakankshaV2bot")]])
            Ansh = await message.reply("<b>⚜ 𝐓𝐡𝐢𝐬 𝐌𝐨𝐯𝐢𝐞 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 ⚜/b>\n\n<b>✪ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ᴏɴ</b>\n<b>ɢᴏᴏɢʟᴇ & ᴛʀʏ ᴀɢᴀɪɴ ✅</b>\n\n<b>☟ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴀᴅᴍɪɴs ғᴏʀ ᴜᴘʟᴏᴀᴅɪɴɢ ❤️‍🔥</b>", reply_markup = one_button)
            await asyncio.sleep(8)
            await k.delete()
            await message.delete()
            return

        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton("📃 Pages 1/1",callback_data="pages"),
                            InlineKeyboardButton("Close 🗑️", callback_data="close")])

            buttons.append([InlineKeyboardButton("🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}?")])

            try:             
                if settings["photo"]:
                    try:
                        remove = await update.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await remove.delete()
                    except:
                        remove = await update.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await remove.delete()
                else:
                    try:
                        remove = await update.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await remove.delete()
                    except:
                        remove = await update.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await remove.delete()
            except:
                remove = await update.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(FILTER_DEL_SECOND)
                await remove.delete()
            return

        data = temp.BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
   
        buttons.append([InlineKeyboardButton(f"📃 1/{data['total']}",callback_data="pages"),
                        InlineKeyboardButton("🗑️", callback_data="close"),
                        InlineKeyboardButton("➡",callback_data=f"nextgroup_0_{keyword}")])

        buttons.append([InlineKeyboardButton("🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")])

        try:             
            if settings["photo"]:
                try:
                    remove = await message.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await remove.delete()
                except:
                    remove = await message.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await remove.delete()
            else:
                try:
                    remove = await message.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{mesaage.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await remove.delete()
                except :
                    remove = await message.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await remove.delete()
        except:
            remove = await message.reply_photo(photo=random.choice(PICS), caption=mo_tech_yt.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(FILTER_DEL_SECOND)
            await remove.delete()

@Client.on_message(filters.private & filters.command('pmautofilter'))
async def pmautofilter(client, msg):        
    try:
        cmd=msg.command[1] 
        if cmd == "on":   
            if msg.chat.id in temp.PMAF_OFF:
                temp.PMAF_OFF.remove(msg.chat.id)
                await msg.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")  
            else:
                await msg.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")                           
        elif cmd == "off": 
            if msg.chat.id in temp.PMAF_OFF:
                await msg.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")                                             
            else:
                temp.PMAF_OFF.append(msg.chat.id)
                await msg.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")
        else:
            await msg.reply_text("𝚄𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙵𝙾𝚁𝙼𝙰𝚃.!\n\n • /pmautofilter on\n • /pmautofilter off")    
    except:
        pass

