import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '26563318'))
API_HASH = environ.get('API_HASH', '0c56c2a16ea879f707bcfe077c4067f4')
BOT_TOKEN = environ.get('BOT_TOKEN', '7265868502:AAGIHIFqLKPNR66J1S88m4CIA4Xn5EqlVgg')

#Fill These Links
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5291901172').split()]
USERNAME = environ.get('USERNAME', "https://t.me/movies_x_alpha")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002188580270'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+uIjL4lSnAMs2YmE1')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002235887787').split()]

#Mongo DB Info
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vedevloper:Hiteshwar@cluster0.wr5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "TELEGRAM_BOT_INFO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002172557556'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/e5da76cf3389a7378c408.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/bdbc2b1e3b0c3efedaec4.png')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002227953693'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', '-1002123926060'))
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))

#VerifiCation And Shortlink Information 
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002172557556'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/+HdOtbk-_Xlk5NDY9")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "4f10081d8a8f9148317422acdfdce44e5a7a33da")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'ziplinker.net')
SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", '')
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", '')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1800"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "80000"))

#Filters Available In Bot
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]

#Premium And Referal 
REF_PREMIUM = 10
PREMIUM_POINT = 1000

#Fill Your Channel IDs 
auth_channel = environ.get('AUTH_CHANNEL', '-1002085214143') #Your Force Subscribe channel Id 
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002174840368'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002200124848') #Requested Content Channel Id
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002242695494')) #Payment Screenshot Sending Channel 
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002197417326')) #Movie Auto Udpate Channel


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = False
else:
    ON_HEROKU = True
URL = environ.get("URL", "https://brutal-movie-filter-u8x3.onrender.com")

import re
import os
from os import environ
from Script import script
import streamlink
import pyffmpeg

# ... (rest of your code remains the same)

# Stream Mode
STREAM_MODE = bool(environ.get('STREAM_MODE', True))

# Stream Options
STREAM_OPTIONS = {
    'stream_type': 'youtube',  # or 'bilibili', 'vimeo', etc.
    'quality': '720p',  # or '1080p', '1440p', etc.
    'format': 'mp4'  # or 'webm', etc.
}

def stream_movie(movie_url):
    stream = streamlink.streams(movie_url, STREAM_OPTIONS)
    if stream:
        ffmpeg_cmd = f'ffmpeg -i {stream} -c:v libx264 -c:a aac -f flv rtmp://localhost:1935/live/{movie_name}'
        subprocess.run(ffmpeg_cmd, shell=True)
    else:
        print(f"Error: Unable to stream {movie_url}")

# ... (rest of your code remains the same)

# Main function
if __name__ == '__main__':
    # ... (rest of your code remains the same)

    # Stream movie
    if STREAM_MODE:
        movie_url = "https://example.com/movie.mp4"
        movie_name = "Movie Name"
        stream_movie(movie_url)

    # ... (rest of your code remains the same)

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '10'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
