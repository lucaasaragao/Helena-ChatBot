#-*- conding: utf-8 -*-

from chatterbot.trainer import ListTrainer #Treinando chat
from chatterbot import ChatBot #chatBot
import os

bot = ChatBot("Helena")


bot.set_trainer(ListTrainer)


for arq in os.lisrdir("arq"):
    chats = open("arqs" + arq, 'r').readlines()
    bot.train(chats)

while True:
    resq = input("Você: ")
    resp = bot.get_response(resq)
    print("Bot: " + resp)

    
