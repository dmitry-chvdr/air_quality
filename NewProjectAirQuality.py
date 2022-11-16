'''
Программа предназначена для "фильтрации" данных
из файлов csv за временной период
и для отображения основных статистик для вещественных и категориальных признаков
'''

# Испортируем модули
import os
import pandas as pd


def main():

    ''' Функция извлекает данных из папки, очищает их, обеспечивает индексацию по дате
     ,сохраняет датасет в формает 'pkl' в удобную папку

     !!!!ОТКОРРЕКТИРУЙ ПУТЬ ПАПОК!!!!!

     '''

    #Создаем листы для работы внутри программы
    list2 = []

    # Сброс ограничений на число отображаемых столбцов
    pd.set_option('display.max_columns', None)

    # Прописываем адреса исходных папок с данными
    directory = (r'C:/Users/George/Desktop/Magistratyra/Project/New Data') #Адрес где леждат данные
    dir1 = (r"C:/Users/George/Desktop/Magistratyra/Project/New Data")      #Адрес для работы в программе

    #dir_test=(r'C:/Users/George/Desktop/Magistratyra/Project/New Data/CO_data/DE_10_7740_2013_timeseries.csv')
    #print(pd.read_csv(dir_test, delimiter=','))

    '''
    Работаем с данными из папок с параметрами качества воздуха
    Удаляем ненужные столбцы ; корректируем имеющиеся
    '''

    for filename in os.listdir(directory):
        dir1 = f'C:/Users/George/Desktop/Magistratyra/Project/New Data/{filename}'

        #Работаем с каждым файлом с имеющийся директории
        for i in os.listdir(dir1):
            dir2 = dir1 + f'/{i}'
            #Прочитываем массив данных
            data = pd.read_csv(dir2, delimiter=',')

            #Формируем массив только с интересующими строками
            data_new = data[['AirPollutant', 'Concentration', 'DatetimeBegin', 'AirQualityStation']]

            #Для корректировки "временного" столбца формирует список данных
            time = data_new['DatetimeBegin'].tolist()

            #Корректируем каждое временное значение отрезая лишнее (формируем новый список значений времени)
            for n in time:
                list2.append(n[0:19])

            #Создаем датасеты для конкантенации
            conkat = {'TIME': list2}
            con = pd.DataFrame(conkat)
            data_new = data_new[['AirPollutant', 'Concentration', 'AirQualityStation']]

            #Формируем конечный датасет
            data_final = pd.concat([con, data_new], axis=1, join='inner')
            #print(data_final)

            #Сохраняем датасет в удобной папке
            if not os.path.isdir(f'C:/Users/George/Desktop/Magistratyra/Project/Main Data/{filename}'):    #Проверяем наличие папки для сохранения
                os.mkdir(f'C:/Users/George/Desktop/Magistratyra/Project/Main Data/{filename}')             #Если папки нет; то сохраняем
            adress = f'C:/Users/George/Desktop/Magistratyra/Project/Main Data/{filename}/{i}'
            data_final.to_csv(adress)

            #Формируем датасет индексируемый по дате
            data = pd.read_csv(adress, parse_dates=['TIME'], index_col='TIME')
            data = data[['AirPollutant', 'Concentration','AirQualityStation']]
            adress1 = f'C:/Users/George/Desktop/Magistratyra/Project/Main Data/{filename}/{i[0:26]}.pkl'   #Адрес сохраняемого датасета
            data.to_pickle(adress1)

def calculate_basic_statistics():

    '''Функция рассчитывает основные статистики для вещественных и категориальных признаков
        Выводит количество отсутствующих значений'''

    directory = (r'C:/Users/George/Desktop/Magistratyra/Project/Main Data')  # Адрес где леждат данные

    for filename in os.listdir(directory):
        dir1 = directory + f'/{filename}'

        # Работаем с каждым файлом с имеющийся директории
        for i in os.listdir(dir1):
            dir2 = dir1 + f'/{i[0:26]}.pkl'

            # Прочитываем данные с индексированным временем
            data = pd.read_pickle(dir2)

            # Подписываем выборку "загрязнитель"; "год"
            print(filename[0:3], i[11:15])
            print(data[['Concentration']].describe())

            #Проверяем на отсутствующие значения
            list_cont1 = []
            for i in data['Concentration'].isnull():
                if i == True:
                    list_cont1.append(1)

            #Выводим кол-во отсутсвующих значений
            print(f'\nОтсутсвующих значений:{len(list_cont1)}')

if __name__ == "__main__":
    main()
    calculate_basic_statistics()