#!/usr/bin/env python
# -*- coding: utf-8 -*-
import contextlib

import telebot,random         # Coded By: Github: @PluginX | Telegram: @rosnw2
from telebot import types

bot_token = "5013666196:AAFDDH4R45qGUfddWsU8atPrIPWmMkPo3YA"
bot = telebot.TeleBot(bot_token)

words = int(1096)
englist = []
meanlist = []
w1 = []
w2 = []
w3 = []

f = open("words.txt","r",encoding="utf-8")
for line in f.readlines():
    one = line.split("\n")
    two = one[0]
    sp = two.split(",")
    eng = sp[0]
    mean = sp[1]
    wrong1 = sp[1]
    wrong2 = sp[1]
    wrong3 = sp[1]
    englist.append(eng)
    meanlist.append(mean)
    w1.append(wrong1)
    w2.append(wrong2)
    w3.append(wrong3)

try:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        ran = random.randint(0, words)
        words1 = random.randint(0, words)
        words2 = random.randint(0, words)
        words3 = random.randint(0, words)
        key = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text=f"{meanlist[ran]}", callback_data='True')
        b2 = types.InlineKeyboardButton(text=f"{w1[words1]}", callback_data='False')
        b3 = types.InlineKeyboardButton(text=f"{w2[words2]}", callback_data='False')
        b4 = types.InlineKeyboardButton(text=f"{w3[words3]}", callback_data='False')

        button = [b1, b2, b3, b4]
        random.shuffle(button)

        key.add(button[0])
        key.add(button[1])
        key.add(button[2])
        key.add(button[3])
        bot.send_audio(message.chat.id, audio=open(f'mp3/{englist[ran]}.mp3', 'rb'),caption=f"معنى كلمه: [ {englist[ran]} ]\n \n المطور: @rosnw2", reply_markup=key)

    @bot.callback_query_handler(func=lambda call: True)
    def calling(call):
        if call.message:
            if call.data == 'False':
                f(call.message)
            elif call.data == 'True':
                t(call.message)

    def f(message):
        bot.send_message(message.chat.id, "إجابتك خاطئة , ✖️")

    def t(message):
        try:
            bot.delete_message(message.chat.id, message.message_id - 2)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id - 3)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id - 4)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id + 1)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id + 2)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id + 3)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id - 1)
        except:
            pass
        try:
            bot.delete_message(message.chat.id, message.message_id + 0)
        except:
            pass

        ran = random.randint(0, words)
        words1 = random.randint(0, words)
        words2 = random.randint(0, words)
        words3 = random.randint(0, words)
        key = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text=f"{meanlist[ran]}", callback_data='True')
        b2 = types.InlineKeyboardButton(text=f"{w1[words1]}", callback_data='False')
        b3 = types.InlineKeyboardButton(text=f"{w2[words2]}", callback_data='False')
        b4 = types.InlineKeyboardButton(text=f"{w3[words3]}", callback_data='False')

        button = [b1, b2, b3, b4]
        random.shuffle(button)

        key.add(button[0])
        key.add(button[1])
        key.add(button[2])
        key.add(button[3])
        bot.send_audio(message.chat.id, audio=open(f'mp3/{englist[ran]}.mp3', 'rb'),caption=f"معنى كلمه: [ {englist[ran]} ]\n \n المطور: @rosnw2", reply_markup=key)
        bot.send_message(message.chat.id, "إجابتك صحيحه , ✔️")
except:
    def send(message):
        bot.send_message(message.chat.id, text="حدث خطاء الارجاء ارسال /start مرا اخرى")

bot.polling(True)
