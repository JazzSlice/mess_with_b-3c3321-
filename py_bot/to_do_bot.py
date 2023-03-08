import telebot

token = # your token
bot = telebot.TeleBot(token)
help = """
press:
    /help - print info
    /add - add task
    /show - print tasks"""
task_list = dict()

@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id, help)

@bot.message_handler(commands=['add'])
def addTask(message):
    _, task, date = message.text.split(maxsplit = 2)
    if len(task_list) < 10:
        if date not in task_list:
            task_list[date] = []
        task_list[date].append(task)
    else:
        print('Too much tasks, chill!')
    bot.send_message(message.chat.id, f'Task {task} was added')

@bot.message_handler(commands=['show'])
def showTasks(message):
    text = f''
    for i in task_list.keys():
        text += f'Tasks for {i}:\n'
        for j in task_list[i]:
            text += f'- {j}\n'
    bot.send_message(message.chat.id, text)

# @bot.message_handler(content_types=["text"])
# def echo(message):
#     bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)




# while True:
#     command = input('Print command: ')
#     match command:
#         case 'help':
#             print(help)
#         case 'add':
#             if len(task_list) < 10:
#                 task = input('Print task: ')
#                 date = input('Print deadline: ')
#                 if date not in task_list:
#                     task_list[date] = []
#                 task_list[date].append(task)
#             else:
#                 print('Too much tasks, chill!')
#         case 'show':
#             for i in task_list.keys():
#                 print(f'Tasks for {i}:')
#                 for j in task_list[i]:
#                     print('- ', j)
#             # date = input('Pick date for show tasks: ')
#             # if date in task_list:
#             #     for i in task_list[date]:
#             #         print('- ', i)
#         case 'exit':
#             print('Have a nice day!')
#             break
