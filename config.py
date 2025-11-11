from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24094487")
    API_HASH = environ.get("API_HASH", "f03452631b3a79c1c96b4908c5c41b33")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8516741165:AAFXOOlVE9wkDbUNcf-DVAwU-XU7maPBLfE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://dbUser:dbUserPassword@ava-cluster.ewss0ln.mongodb.net/?appName=ava-cluster")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1369876116').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
