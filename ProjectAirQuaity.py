
'''
Программа для выборки из массива данных нужных станции

Данные хранятся в виде папок за каждый день (Например 02.11.2022; 03.11.2022)
В папках собраны данные по всем отслеживаемым станциям в мире
По заранее интересуемым ID проверяем нужные станции , если есть в конкретной папке (день),
то копируем интересующий файл csv (выбран тоже по ID) в отдельную папку по стацнии

На выходе - директория с данными на каждую интересующую стацию
Внутри директории папки с названиями
Внутри папок - csv файлы с данными
'''



# Испортируем модули
import os
from pathlib import Path
import re
import shutil

# Прописываем адреса исходных папок
dir1 = (r"C:\Users\George\Desktop\Test")      #Адрес для работы в программе
directory = (r'C:\Users\George\Desktop\Test') #Адрес где леждат данные

# Итерируемся по папкам где лежат данные за все периоды

for filename in os.listdir(directory):
    #Формируем список всех станций в конкретный день (станция может отсутвовать)
    dir2 = dir1 + '\\'+ filename
    c = os.listdir(dir2)

    #Если станция есть в списке , то открываем папку со станцией по её ID, копируем файл с данным (тут РМ10) по ID в папку
    # где будут собиратся все данные по конкретной стации

    #Работа со станцией в Бускудниково
    if '5eece804ee9b25001bb9279d-MoscowSeligerskaya12k2' in  c:
        print('Станция Бескудниковская есть в списке')
        adress = dir2 + '\\' + '5eece804ee9b25001bb9279d-MoscowSeligerskaya12k2' + '\\' + '5eece804ee9b25001bb927a2' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\BeskydnikovoPM10')
        shutil.copy(adress,adress2)

    #Работа со станцией на ВТБ Арене
    if ('5c6409daa100840019d4d0bf-20228') in c:
        adress = dir2 + '\\' + '5c6409daa100840019d4d0bf-20228' + '\\' + '5c6409daa100840019d4d0c4' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\VTB_ArenaPM10')
        shutil.copy(adress, adress2)
        print( 'Станция Арена ВТБ есть в спике')

    #Работа со станцией в Долгопрудном
    if ('5d61362d953683001a679c4e-Feinstaubsensor-321476') in c:
        adress = dir2 + '\\' + '5d61362d953683001a679c4e-Feinstaubsensor-321476' + '\\' + '5d61362d953683001a679c53' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\DolgoprydniyPM10')
        shutil.copy(adress, adress2)
        print('Cтанция Долгопрудная есть в списке')


    #Работа со станцией в Жуковском
    if ('604761fd42d3c7001bc62975-airRohr-10271890') in c:
        adress = dir2 + '\\' + '604761fd42d3c7001bc62975-airRohr-10271890' + '\\' + '604761fd42d3c7001bc6297a' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\GykovskiyPM10')
        shutil.copy(adress, adress2)
        print('Станция Жуковский есть в списке')

    #Работа со станцией в Зеленограде
    if ('5ebfdf05e0b0b3001b37e1e9-Zel-1') in c:
        adress = dir2 + '\\' + '5ebfdf05e0b0b3001b37e1e9-Zel-1' + '\\' + '5ebfdf05e0b0b3001b37e1ee' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\ZelenogradPM10')
        shutil.copy(adress, adress2)
        print('Станция Зеленоградская есть в списке')

    #Работаем со станцией в Золотово
    if ('5eff36e4b9d0aa001c0c7ee7-zolotovo') in c:
        adress = dir2 + '\\' + '5eff36e4b9d0aa001c0c7ee7-zolotovo' + '\\' + '5eff36e4b9d0aa001c0c7eec' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\ZolotovoPM10')
        shutil.copy(adress, adress2)
        print('Станция Золотово есть в списке')

    #Работаем со станцией в Купавне
    if ('5d1579bf30bde6001ad36fe9-PMS5003') in c:
        adress = dir2 + '\\' + '5d1579bf30bde6001ad36fe9-PMS5003' + '\\' + '5d1579bf30bde6001ad36fed' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\Kypavna1PM10')
        shutil.copy(adress, adress2)
        print('Станция Купавна 1 есть в списке')

    #Работаем со станцией в Купавне 2
    if ('60773a965795a3001be46eb6-PMS5003___BME280') in c:
        adress = dir2 + '\\' + '60773a965795a3001be46eb6-PMS5003___BME280' + '\\' + '60773a965795a3001be46eba' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\Kypavna2PM10')
        shutil.copy(adress, adress2)
        print('Станция Купавна 2 есть в списке')

    #Работаем со станцией в Покрово-Стрешнево
    if ('5cfb5ad9a1ba9f001a3bd426-Outside') in c:
        adress = dir2 + '\\' + '5cfb5ad9a1ba9f001a3bd426-Outside' + '\\' + '5cfb5ad9a1ba9f001a3bd42b' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\Pokrovo_StreshevoPM10')
        shutil.copy(adress, adress2)
        print('Станция Покрово-Стрешнево 1 есть в списке')

    #Работаем со станцией в Покрово-Стрешнево2
    if ('5f7f6e39fa71a3001b7396cf-Outside') in c:
        adress = dir2 + '\\' + '5f7f6e39fa71a3001b7396cf-Outside' + '\\' + '5f7f6e39fa71a3001b7396d4' + (f'-{filename}.csv')
        adress2 = (r'C:\Users\George\Desktop\Results\Pokrovo_Streshevo2PM10')
        shutil.copy(adress, adress2)
        print('Станция Покрово-Стрешнево 2 есть в списке')




'''  for i in file:
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
'''