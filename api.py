#!/usr/bin/env python
import os
import yaml
import json

SPEAKERS_TEMPLATE = """
{
  bio": "Kirill has been doing professional client-side development over the last decade in a variety of UI toolkits and libraries that spanned Motif, MFC, VB, Ada, Delphi, Swing and SWT. Since 2009 he's been part of the Android team at Google. He has a particular interest in creating polished, responsive and well-behaving, user-facing applications that help the end users achieve their goals quickly and painlessly.",
  "name": "Kirill Grouchnikov",
  "company": "Google",
  "plusoneUrl": "https://plus.google.com/+KirillGrouchnikov",
  "thumbnailUrl": "http://storage.googleapis.com/iosched-updater-dev.appspot.com/images/speakers/__w-200-400-600-800-1000__/b5ca32e2-a5c6-e311-b297-00155d5066d7.jpg",
  "id": "b5ca32e2-a5c6-e311-b297-00155d5066d7"
}
"""

SESSION_TEMPLATE = """
{
   "id": "SESSION123"
   "url": "https://...."
   "title": "Web Components in Action",
   "description": "Web components are cool.",
   "tags": [
       "TYPE_SESSION",
       "TOPIC_ANDROID",
       "TOPIC_CHROME",
       "THEME_DEVELOP",
       "THEME_DESIGN"
   ]
   "mainTag": "TOPIC_ANDROID",
   "startTimestamp": "2014-06-25T22:10:00Z",
   "endTimestamp": "2014-06-25T22:55:00Z"
   "photoUrl": "https://...../photo.jpg",
   "youtubeUrl": "https://youtu.be/YCUZ01yFtsM",
   "speakers": [
       "SPEAKER123",
       "SPEAKER456"
   ],
   "room": "ROOM123",
   "isLivestream": true,
   "captionsUrl": "http://......",
   "color": "#607d8b",
   "hashtag": "webcomponents"
}
"""

# read data
schedule = None
with open("_data/schedule.yml", "r") as f:
  schedule = yaml.safe_load(f)

sessions = None
with open("_data/sessions.yml", "r") as f:
  sessions = yaml.safe_load(f)

speakers = None
with open("_data/speakers.yml", "r") as f:
  speakers = yaml.safe_load(f)

data = {
  "schedule": schedule,
  "sessions": sessions,
  "speakers": speakers
}


with open("data.json", "w") as f:
  json.dump(data, f)

