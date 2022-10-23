#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "10247139"
    API_HASH = "96b46175824223a33737657ab943fd6a"
    BOT_TOKEN = "96b46175824223a33737657ab943fd6a"
    DEV = 1664850827
    OWNER = "1443454117"
    ffmpegcode = ["-preset medium -c:v h264 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1 -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
