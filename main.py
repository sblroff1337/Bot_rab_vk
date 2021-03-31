# -*- coding: utf-8 -*-
import requests, json, schedule, threading, os
from random import randint, randrange
from time import sleep

with open("config.json", encoding='utf-8-sig') as f: # cfg
    config = json.load(f)

authorization = str(config["authorization"]).rstrip().lstrip()

"""Все настройки в Config.json"""
telegram_user_id = config['telegram_settings']['telegram_user_id']
telegram_bot_token = config['telegram_settings']['telegram_bot_token']  

print(f'   __      __        ________     ___         _____')
print(f'  |  \\    /  |      |        |   | _ \\       |   __|')
print(f'  |   \\  /   |      |   _    |   || | \\      |  |')
print(f'  | |\\ \\/ /| |      |  | |   |   || |  \\     |  |__ ')
print(f'  | | \\__/ | |      |  | |   |   || |   |    |  ___|')
print(f'  | |      | |      |  | |   |   || |   /    | |')
print(f'  | |      | |      |  |_|   |   ||_|  /     | |___')
print(f'  |_|      |_|      |________|   |___ /      |_____|')
print(f'')
print(f'Модефецированная версия by sblrov   vk.com/sblrov|TG: @sblrov')
print(f'Запуск через 5 сек')
print(f'1')
sleep(0.9)
print(f'2')
sleep(0.9)
print(f'3')
sleep(0.9)
print(f'4')
sleep(0.9)
print(f'5')
sleep(0.9)
print(f'Статус в "шапке" КМД: ' + str(config["windows_title"]) + '\nОтправка сообщений в телеграм: ' + str(config['telegram_settings']['telegram_notification']) + '\nНазвание(ия) работ(ы): '  + str(config['general_settings']['job_name']) + '\nМинимальная цена закупки: ' + str(config['general_settings']['min_price']) + '\nМаксимальная цена закупки: ' + str(config['general_settings']['max_price']) + '\nПокупка рабов: ' + str(config['general_settings']['buy_slave']) + '\nПокупка цепей: ' + str(config['general_settings']['buy_fetter']) + '\nПрокачка рабов до 1к в мин: ' + str(config['general_settings']['upgrade_slave']))
if config['telegram_settings']['telegram_notification'] == True:
    print(f'Что будет приходить в телеграм: ')
    print(f'Поставил ли работу: ' + str(config['telegram_settings']['telegram_notify_error']['job_name']))
    print(f'Покупка раба: ' + str(config['telegram_settings']['telegram_notify_error']['buy_slave']))
    print(f'Покупка цепей: ' + str(config['telegram_settings']['telegram_notify_error']['buy_fetter']))
    print(f'Продажа рабов: ' + str(config['telegram_settings']['telegram_notify_error']['sale_slave']))
    print(f'')
else:
    print('\n')

"""Получение информации о своем профиле"""
def myProfile():
    global authorization
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

"""Получение информации о профиле игрока"""
def userProfile(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

"""Получение информации о топерах"""
def topUsers():
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/topUsers'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()

"""Устройство рабов на работу"""
def jobSlave(slave_id):
    global job_name
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave'
    payload = json.dumps({'slave_id':slave_id, 
     'name':config['general_settings']['job_name'][randrange(0, len(config['general_settings']['job_name']))]})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Ошибка вызвана кулдауном на смену работы у раба ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
            if config['telegram_settings']['telegram_notify_error']['job_name'] == True:
               requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Ошибка вызвана кулдауном на смену работы у раба ID: {slave_id}")
    elif response.status_code == 200:
        print(f'Устанавливаем работу рабу ID: {slave_id}. Работа: ' + userProfile(slave_id)['job']['name'])
        if config['telegram_settings']['telegram_notification'] == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Устанавливаем работу рабу ID: {slave_id}. Работа: " + userProfile(slave_id)['job']['name'])
    else:
        print(f'Хуй пойми какая ошибка у раба с работай ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Хуй пойми какая ошибка у раба ID: {slave_id}")

    return response.json()

"""Покупка оков"""
def buyFetter(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buyFetter'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Ошибка вызвана кулдауном на поставление цепи у раба ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
            if config['telegram_settings']['telegram_notify_error']['buy_fetter'] == True:
               requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Ошибка вызвана кулдауном на поставление цепи у раба ID: {slave_id}")
    elif response.status_code == 200:
        print(f'Покупка цепей у раба ID: {slave_id}. Цена: ' + str(int(userProfile(slave_id)['fetter_price'])))
        if config['telegram_settings']['telegram_notification'] == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Покупка цепей у раба ID: {slave_id}. Цена: "+ str(int(userProfile(slave_id)['fetter_price'])))
    else:
        print(f'Хуй пойми какая ошибка у раба с цепями ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Unknown error. Slave: {slave_id}")
   
    return response.json()

"""Покупка рабов"""
def buySlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Ошибка вызвана кулдауном на покупку раба. Его ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
            if config['telegram_settings']['telegram_notify_error']['buy_slave'] == True:
               requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Ошибка вызвана кулдауном на покупку раба. Его ID: {slave_id}")
    elif response.status_code == 200:
        print(f'Покупаю: {slave_id}. Цена: ' + str(int(userProfile(slave_id)['price']/1.49998088027))) 
        if config['telegram_settings']['telegram_notification'] == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Покупаю: {slave_id}. Цена: " + str(int(userProfile(slave_id)['price']/1.5)))
    else:
        print(f'Хуй пойми какая ошибка с покупкой раба. Его ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Хуй пойми какая ошибка с покупкой раба. Его ID: {slave_id}")

    return response.json()

"""Получение списка рабов"""
def slaveList(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/slaveList?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()['slaves']

"""Продажа рабов"""
def saleSlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'Content-Type': "application/json",
     'authorization': authorization,
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Ошибка вызвана кулдауном на продажу раба. Его ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
            if config['telegram_settings']['telegram_notify_error']['sale_slave'] == True:
               requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Ошибка вызвана кулдауном на продажу раба. Его ID: {slave_id}")
    elif response.status_code == 200:
        print(f'Продаю: {slave_id}. Цена: ' + str(int(userProfile(slave_id)['sale_price']/1.49998088027)))
        if config['telegram_settings']['telegram_notification'] == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Продаю: {slave_id}. . Цена: " + str(int(userProfile(slave_id)['sale_price']/1.5)))
    else:
        print(f'Хуй пойми какая ошибка с продажей раба. Его ID: {slave_id}')
        if config['telegram_settings']['telegram_notification'] == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Хуй пойми какая ошибка с продажей раба. Его ID:: {slave_id}")

    return response.json()

"""Обновление оков и установка работ в своем профиле рабам"""
def Profile():
    me = myProfile()['me']

    if me['fetter_to'] != 0:
        if me['balance'] >= me['price']:
            if str(int(config['general_settings']['buy_slave'])) == True:
                if int(slave['price']) >= config['general_settings']['min_price']:
                        if int(slave['price']) <= config['general_settings']['max_price']:
                           sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                           buySlave(int(str(slave['id'])))
    me = myProfile()['me']
    slaves = myProfile()['slaves']
    
    sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))

    for slave in slaves:
        if slave['job']['name'] == '':
            if config['other_settings']['sale_all_slaves'] == False:
                sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                jobSlave((slave['id']))

        if slave['fetter_price'] <= me['balance'] and slave['fetter_to'] == 0:
            if config['other_settings']['sale_all_slaves'] == False:
                if config['general_settings']['buy_fetter'] == True:
                               sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                               buyFetter(int(str(slave['id'])))

        if config['other_settings']['sale_all_slaves'] == True:
            sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
            saleSlave(int(str(slave['id'])))

"""Скупать рабов у чела прописанного в кфг"""
def triggerProfile():
    if config['other_settings']['sale_all_slaves'] == False:
        sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
        me = myProfile()['me']
        if config['other_settings']['trigger_user_id'] > 0:
            slaves = slaveList(config['other_settings']['trigger_user_id'])

            for slave in slaves:
                if config['general_settings']['buy_slave'] == True:
                    if slave['fetter_price'] <= me['balance'] and slave['fetter_to'] == 0:
                        sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                        buySlave(int(str(slave['id'])))
                        sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                        jobSlave(int(str(slave['id'])))
                        if config['general_settings']['buy_fetter'] == True:
                            sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                            buyFetter(int(str(slave['id'])))

threading.Thread(target=Profile).start()
sleep(10)
threading.Thread(target=triggerProfile).start()

while True:
    try:
        me = myProfile()['me']
        if config['windows_title'] == True:
           os.system(f'title Твой id: ' + str(me['id']) +  ", Твоих рабов: " + str(me['slaves_count']) + ", Баланс: " + str(me['balance']) + ", Сколько прибыли: " + str(me['slaves_profit_per_min']) + "р в мин")
    except Exception as e:
        print(f'ПИЗДА ПИЗДОЙ ОТПРАВЛЯЙ СОЗДАТЕЛЮ ОШИБУЦ - {e}')
        input
    try:
        schedule.run_pending()
        if config['general_settings']['buy_slave'] == True:
            if config['other_settings']['sale_all_slaves'] == False:
                if config['other_settings']['trigger_user_id'] <= 0:
                    randomid = randint(500, 647000000)
                    slave = userProfile(randomid)
                    print('Slave: ' + str(randomid))

                    if int(myProfile()['me']['balance']) >= int(slave['fetter_price']):
                        if int(slave['fetter_to']) == 0:
                            if int(slave['price']) >= config['general_settings']['min_price']:
                                if int(slave['price']) <= config['general_settings']['max_price']:
                                    sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                    if config['general_settings']['buy_slave'] == True:
                                        if config['general_settings']['upgrade_slave'] == True:
                                           if int(me["balance"]) >= 39214:
                                            buySlave(randomid)
                                            while int(userProfile(randomid)['price']/1.49998088027)  < 26151:
                                                  sleep(1)
                                                  saleSlave(randomid)
                                                  sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                                  buySlave(randomid)
                                                  if int(userProfile(randomid)['price']/1.49998088027) >= 26151:
                                                    print(f'Проапал раба LvL up. ID раба: {randomid}')
                                                    if config['telegram_settings']['telegram_notification'] == True:
                                                        requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Проапал раба LvL up. ID раба: {randomid}")
                                           else:
                                            buySlave(randomid)
                                            sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                        else:
                                            sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                            buySlave(randomid)
                                        sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                        jobSlave(randomid)
                                        if config['general_settings']['buy_fetter'] == True:
                                            if slave['fetter_price'] <= me['balance'] and slave['fetter_to'] == 0:
                                               sleep(randint(config['general_settings']['min_delay'],config['general_settings']['max_delay']))
                                               buyFetter(randomid)

    except Exception as inst:
        try:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            inst = None
            del inst