class script(object):
    START_TXT = """๐ท๐ด๐ป๐พ {},
๐ผ๐ข ๐๐๐๐ , <a href='https://t.me/bheeshma2_rejaBot'>๐ฌ๐๐๐๐๐๐แดแด๊ฑแดสแดแดฉแดฉแด</a>, ๐ธ๐'๐ ๐๐๐๐ข ๐๐๐๐ข ๐๐๐๐ ๐๐๐ ๐๐ ๐๐ ๐ข๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐ ๐๐๐๐๐, ๐๐๐๐๐ ๐๐๐ ๐ธ'๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ โฅ๏ธ
"""
    HELP_TXT = """๐ท๐ด๐ {}
๐๐ฆ๐ณ๐ฆ ๐๐ด ๐๐ฉ๐ฆ ๐๐ฆ๐ญ๐ฑ ๐๐ฐ๐ณ ๐๐บ ๐๐ฐ๐ฎ๐ฎ๐ข๐ฏ๐ฅ๐ด."""
    ABOUT_TXT = """
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
โโโโโโโฐ๐ป๐ฌ๐จ๐ด ๐ช๐น๐ฐ๐ด๐ฌโฑ
โโญโโโโโโโโโโโโโโโโคออออโ 
โโฃโชผ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด - <a href="https://t.me/bheeshma2_rejaBot"> ๐ฌ๐๐๐๐๐๐แดแด๊ฑแดสแดแดฉแดฉแด </a>
โโฃโชผ ๐ฒ๐๐ด๐ฐ๐๐พ๐ - <a href="https://t.me/pushpa_reju"> ๐๐ถ-๐ฟ๐๐๐ท๐ฟ๐ฐ๐๐ด๐น๐ </a>
โโฃโชผ ๐ป๐ธ๐ฑ๐๐ฐ๐๐ - ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โโฃโชผ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด - ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โโฃโชผ ๐ณ๐ฐ๐๐ฐ๐ฑ๐ฐ๐๐ด - ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
โโฃโชผ ๐๐ด๐๐๐ด๐ -  ๐ท๐ด๐๐พ๐บ๐
โโฃโชผ ๐ฑ๐๐ธ๐ป๐ ๐๐๐ฐ๐๐ - v1.0.2 [ ๐ฟ๐๐ ]
โโฐโโโโโโโโโโโโโโโโคออออโ โโโโโโโโโโโโโโโโโโโโชผ๐"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐๐พ๐ ๐ผ๐พ๐๐ท๐ด๐ ๐ต๐๐ฒ๐บ๐ด๐ ๐ธ๐ฐ๐ผ ๐ฝ๐พ๐ ๐ฐ ๐พ๐ฟ๐ด๐ฝ ๐๐พ๐๐๐ฒ๐ด๐คญ. 

๐ ๐๐ฆ๐ง๐๐ฅ:
<a href="https://t.me/pushpa_reju"> ๐ป๐ฌ๐จ๐ด ๐ช๐น๐ฐ๐ด๐ฌ </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

โข/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
โข /alive - check me alive or dead๐"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
โก๏ธ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

โก๏ธ <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>COMMAND /stickerid\n๐จ๐ฟ ๐ธ๐๐ ๐ญ๐พ๐พ๐ฝ ๐ณ๐พ๐๐พ๐๐๐บ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ ๐ข๐๐๐ผ๐ /stickerid ๐ณ๐ ๐ฆ๐พ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ (๐ฑ๐พ๐๐๐ ๐ถ๐๐๐ ๐ฒ๐๐๐ผ๐๐พ๐)</b>"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

๐ Command

โข /song or /mp3 (songname) - download song from yt servers.
โข /video or /mp4 (songname) - download video from yt servers

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>๐ Commands & Usage:</b>

โ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

โ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>๐ฒ NOTHING MUCH JUST SOME FUN THINGS</b>
t๐๐ ๐๐๐๐ ๐ฎ๐๐: 
๐ฃ. /dice - Roll The Dice 
๐ค. /Throw ๐๐ /Dart - ๐ณ๐ ๐ฌ๐บ๐๐พ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - add a filter in chat.
โข /filters - list all the filters of a chat.
โข /del - delete a specific filter in chat.
โข /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - connect a particular chat to your PM.
โข /disconnect  - disconnect from a chat.
โข /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
โข /paste [text] - paste the given text on Pasty
โข /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
โข /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
โข /id - get id of a specifed user.
โข /info  - get information about a user.
โข /json - get the json details of a message.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
โข /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข More search tools can be found on inline.
โข Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
โข /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on group.
โข These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
โข /ban - ban a user.
โข /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
โข /mute - mute a user.
โข /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
โข /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on group.
โข These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - to get the rescent errors.
โข /stats - to get status of files in db.
โข /delete - to delete a specific file from db.
โข /users - to get list of my users and ids.
โข /chats - to get list of the my chats and ids.
โข /leave - to leave from a chat.
โข /disable - do disable a chat.
โข /ban_users - to ban a user.
โข /unban_users - to unban a user.
โข /channel - to get list of total connected channels.
โข /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>โ Total Files โบโบ</b> <code>{}</code>
<b>โ Total Users โบโบ</b> <code>{}</code>
<b>โ Total Chats โบโบ</b> <code>{}</code>
<b>โ Used Storage โบโบ</b> <code>{}</code> MB
<b>โ Free Storage โบโบ</b> <code>{}</code> MB"""

    FORCESUB_TXT = """**โฆ๏ธ READ THIS INSTRUCTION โฆ๏ธ**

__๐ฃ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately ๐__

**๐ JOIN THIS CHANNEL & TRY AGAIN ๐**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """โYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """๐ฎ Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """โI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
