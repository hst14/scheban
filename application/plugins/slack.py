# -*- coding: utf-8 -*-
import sys
from slackbot.bot import respond_to
sys.path.append('..')
from google_calendar import events2text, search


@respond_to('今後の予定を教えて')
def respond_schedule(message):
    calendar_id = 'fuiiaj193eabmmr8i4di5431no@group.calendar.google.com'
    reply_message = events2text(calendar_id=calendar_id)
    calendar_id = 'apsc06pkhcnmbt0kng1os7ktqs@group.calendar.google.com'
    reply_message1 = events2text(calendar_id=calendar_id)
    calendar_id = 'b73akvp9fn7f1ogq3l7u1u4jrg@group.calendar.google.com'
    reply_message2 = events2text(calendar_id=calendar_id)

    message.reply(reply_message)
    message.reply(reply_message1)
    message.reply(reply_message2)



@respond_to('(.*)')
def refrection(message, something):
    rep_message = search(calendar_id=('fuiiaj193eabmmr8i4di5431no@group.calendar.google.com'),key=something,max_results=100)
    message.reply(rep_message)
    rep_message1 = search(calendar_id=('apsc06pkhcnmbt0kng1os7ktqs@group.calendar.google.com'), key=something,
                         max_results=100)
    message.reply(rep_message1)
    rep_message2 = search(calendar_id=('b73akvp9fn7f1ogq3l7u1u4jrg@group.calendar.google.com'), key=something,
                         max_results=100)
    message.reply(rep_message2)



