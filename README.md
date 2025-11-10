# Mehta
**A beginner-friendly telegram sdk providing intuitive command decorators.**<br>
This package is a **wrapper** that uses [pyTeleBot](https://github.com/eternnoir/pyTelegramBotAPI) and [Telethon](https://github.com/LonamiWebs/Telethon) for Telegram-related features.  
When you install it, all required dependencies including [pyTeleBot](https://github.com/eternnoir/pyTelegramBotAPI), [Telethon](https://github.com/LonamiWebs/Telethon), and others are automatically installed to ensure full functionality and seamless integration.


## Installation
```bash
pip install mehta
```

## Basic Setup
```python
from mehta import telegram

bot = telegram()

@bot.commands(['start'])
def start(message):
    return "Hello! Bot started."

@bot.message()
def echo(message):
    return f"You said: {message.text}"

bot.run("YOUR_BOT_TOKEN")
```

## Decorators Reference

| Decorator       | Parameters                                | Use Case                             |
|-----------------|-------------------------------------------|--------------------------------------|
| `@bot.commands` | `commandlist`, `rate_limit=None`, `timeout=None` | Bind handler to Telegram commands    |
| `@bot.message`  | **None**                                  | Handles all non-command messages     |
| `@bot.callback` | **None**                                  | Handles callback queries (inlines)   |
| `@bot.error`    | **None**                                  | Handles errors for all handlers      |

**Example:**
```python
@bot.commands(['hi'], rate_limit=1, timeout=3)
def hi(message): return "Hi, rate limit 1/min, timeout 3s!"
```
- `command([""])`: list of `commands`
- `rate_limit`: int, calls/user/min
- `timeout`: int, seconds for auto-timeout

## Functions and Parameters
| Function        | Parameters            | Use Case                | Example                                            | Example                     |
|-----------------|----------------------------------------------|-------------------------|------------------------------------------------------------|------------------------------------------|
| **text**        | **content**, parse, receiver, reply_to, preview, notify | Send plain text         | `{'type': 'text', 'text': 'hi', 'parse': 'Markdown'}`      | `text('hi', parse='Markdown')`           |
| **photo**       | **file**, caption, parse, receiver, reply_to, notify   | Send image/photo        | `{'type': 'photo', 'file': 'x.jpg', 'caption':'txt'}`      | `photo('x.jpg', caption='txt')`          |
| **video**       | **file**, caption, parse, receiver, reply_to, notify   | Send video              | `{'type': 'video', 'file': 'v.mp4', 'caption':'c'}`        | `video('v.mp4', caption='c')`            |
| **audio**       | **file**, caption, parse, receiver, reply_to, notify   | Send audio              | `{'type': 'audio', 'file': 'a.mp3'}`                       | `audio('a.mp3')`                         |
| **document**    | **file**, caption, parse, receiver, reply_to, notify   | Send file/document      | `{'type': 'document', 'file': 'd.pdf'}`                    | `document('d.pdf')`                      |
| **sticker**     | **file**, receiver, reply_to, notify                  | Send sticker            | `{'type': 'sticker', 'file': 't.webp'}`                    | `sticker('t.webp')`                      |
| **voice**       | **file**, caption, parse, receiver, reply_to, notify   | Send voice msg          | `{'type': 'voice', 'file': 'x.ogg'}`                       | `voice('x.ogg')`                         |
| **animation**   | **file**, caption, parse, receiver, reply_to, notify   | Send GIF/animation      | `{'type': 'animation','file':'fun.gif','caption':'ha'}`    | `animation('fun.gif',caption='ha')`      |
| **location**    | **lat**, **lon**, receiver, reply_to, notify          | Send location           | `{'type': 'location','lat':0.0,'lon':0.0}`                 | `location(0.0,0.0)`                      |
| **venue**       | **lat**, **lon**, **title**, **address**, receiver, reply_to, notify | Venue                  | `{'type': 'venue','lat':1,'lon':2,'title':'X','address':'Y'}` | `venue(1,2,'X','Y')`                     |
| **contact**     | **phone**, **first_name**, last_name, receiver, reply_to, notify | Send contact           | `{'type': 'contact','phone':'+9','first_name':'X','last_name':'Y'}` | `contact('+9','X','Y')`          |
| **poll**        | **question**, **options**, receiver, reply_to, notify | Telegram poll           | `{'type': 'poll','question':'?','options':['A','B']}`      | `poll('?',['A','B'])`                    |
| **dice**        | emoji, receiver, reply_to, notify                      | Dice game               | `{'type':'dice','emoji':'🎯'}`                             | `dice('🎯')`                              |
| **delete**      | message_id, receiver                                   | Delete msg              | `{'type': 'delete','message_id': 1}`                       | `delete(1)`                               |
| **edit**        | message_id, **text**, parse, receiver, preview         | Edit text/caption       | `{'type': 'edit','message_id':1,'text':'upd'}`             | `edit(1,'upd')`                           |
| **forward**     | **to_chat**, **message_id**, receiver, notify          | Forward message         | `{'type': 'forward','to':22,'message_id':1}`               | `forward(22,1)`                           |
| **copy**        | **to_chat**, **message_id**, caption, parse, receiver, notify | Copy message           | `{'type': 'copy','to':22,'message_id':1}`                  | `copy(22,1)`                              |
| **keyboard**    | **text**, **buttons**, parse, receiver, reply_to, preview, notify | Reply keyboard     | `{'type': 'keyboard','text':'pick','buttons':[['A','B']]}` | `keyboard('pick',[['A','B']])`            |
| **inline**      | **text**, **buttons**, parse, receiver, reply_to, preview, notify | Inline buttons, data | `{'type': 'inline','text':'tap','buttons':[[{'text':'Y','data':'cb'}]]}` | `inline('tap',[[{'text':'Y','data':'cb'}]])`|
| **remove_keyboard** | **text**, parse, receiver, reply_to, preview, notify | Hide keyboard       | `{'type':'remove_keyboard','text':'OK'}`                   | `remove_keyboard('OK')`                   |
| **force_reply** | **text**, parse, receiver, reply_to, preview, notify   | Force reply             | `{'type':'force_reply','text':'enter'}`                    | `force_reply('enter')`                     |
| **pin**         | message_id, receiver, notify                           | Pin message             | `{'type': 'pin','message_id':1}`                           | `pin(1)`                                  |
| **unpin**       | message_id, receiver                                   | Unpin message           | `{'type': 'unpin','message_id':1}`                         | `unpin(1)`                                |
| **unpin_all**   | receiver                                               | Unpin all               | `{'type': 'unpinall'}`                                     | `unpin_all()`                             |
| **ban**         | **user_id**, until_date, receiver                      | Ban user                | `{'type': 'ban','user':88}`                                | `ban(88)`                                 |
| **unban**       | **user_id**, receiver                                  | Unban user              | `{'type': 'unban','user':88}`                              | `unban(88)`                               |
| **restrict**    | **user_id**, permissions, until_date, receiver         | Restrict rights         | `{'type': 'restrict','user':88,'permissions':{}}`           | `restrict(88,permissions={})`             |
| **promote**     | **user_id**, privileges, receiver                      | Promote member          | `{'type':'promote','user':88,'privileges':{}}`              | `promote(88,privileges={})`               |
| **chat_info**   | receiver                                               | Chat info               | `{'type':'chatinfo'}`                                      | `chat_info()`                             |
| **member_count**| receiver                                               | Members in chat         | `{'type':'membercount'}`                                   | `member_count()`                          |
| **member_info** | **user_id**, receiver                                  | Info a user             | `{'type':'memberinfo','user':88}`                          | `member_info(88)`                         |
| **invite_link** | receiver                                               | Chat invite link        | `{'type':'invitelink'}`                                    | `invite_link()`                           |
| **set_title**   | **title**, receiver                                    | Set chat title          | `{'type':'settitle','title':'Z'}`                          | `set_title('Z')`                          |
| **set_description** | **description**, receiver                          | Set chat description    | `{'type':'setdescription','description':'info'}`           | `set_description('info')`                 |
| **set_photo**   | **file**, receiver                                     | Set chat photo          | `{'type':'setphoto','file':'img.jpg'}`                     | `set_photo('img.jpg')`                    |
| **delete_photo**| receiver                                               | Delete chat photo       | `{'type':'deletephoto'}`                                   | `delete_photo()`                          |
| **answer_callback**| **query_id**, text, show_alert, url                 | Answer inline cb        | `{'type':'answercallback','query_id':'qid','text':'OK'}`   | `answer_callback('qid',text='OK')`        |
| **edit_message**| **message_id**, text, parse, receiver, preview, buttons, caption, reply_markup | Edit with buttons      | `{'type':'editmessage','message_id':1,'text':'Upd'}`       | `edit_message(1,'Upd')`                   |
| **mediagroup**  | **media_list**, receiver, reply_to, notify             | Send media group        | `{'type':'mediagroup','media':[{'type':'photo','file':'a.jpg'}]}` | `mediagroup([{'type':'photo','file':'a.jpg'}])` |

**Tip:** Most parameters auto-fill to message context if omitted (e.g., `receiver`, `reply_to`).


## Response Type Usage

```python
@bot.commands(['types'])
def demo(message):
    # Text
    return text("A simple message.", parse='MarkdownV2')
    
    # Photo
    # return photo('img.jpg', caption='A cool pic!', notify=True)
    
    # Keyboard
    # return keyboard('Choose:', [['A','B']])
```

## Using Webhook & Polling
**Polling (default):**
```python
bot.run("YOUR_BOT_TOKEN")
```

**Webhook:**
```python
bot.webhook("YOUR_BOT_TOKEN", "https://yourdomain.com/" [,port]) # Registers webhook and listens for messages via HTTP.
```
- Second arg: webhook URL.
- Optional: set a custom port (default 8000)

**Which to use?**
- **Polling**: Easiest for dev/small apps.
- **Webhook**: Production or cloud deployments.

## Client Integration
```python
from mehta import client

bot = client()

@bot.commands(['start'])
def start(message):
    return text("Hello from Telethon client")

@bot.message()
def echo(message):
    return text(f"Echo: {message.text}")

bot.run(api_id=YOUR_API_ID', api_hash='YOUR_API_HASH')
```
- Works all **possible** functions (`text`, `photo`, `video`, ...).

## FAQ & Notes
- **Auto-injection:** Helper functions (`text`, `photo`, etc.) are imported as globals for you automatically when you create a bot/client instance.
- **Return style:** All handlers can return either a dictionary or use the provided helper function style.
- **Error handling:** For both pyTelebot and Telethon, errors are printed nicely by default.
- **CLI:** `mehta run:yourfile.py`—auto detects main bot and starts automatically.
- **Rate limits:** Use `rate_limit` in command decorators for anti-spam.
- **Timeout:** Force handlers to exit after N seconds if unresponsive.
- **Extending:** For new types/variants, copy the dict pattern.
