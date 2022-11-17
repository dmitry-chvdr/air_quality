"""
Программа предназначена для "фильтрации" данных
из файлов csv за временной период
и для отображения основных статистик для вещественных и категориальных признаков
"""


import os
import pandas as pd

# TODO: вынести в .env
WORK_DIR_PATH = "C:/Users/George/Desktop/Magistratyra/Project/New Data"
RESULT_DIR_PATH = "C:/Users/George/Desktop/Magistratyra/Project/Main Data"


def clean_data(work_dir, result_dir):
    """
    Функция извлекает данных из папки, очищает их, обеспечивает индексацию по дате ,сохраняет датасет в формает 'pkl'.
    """

    # Сброс ограничений на число отображаемых столбцов
    pd.set_option("display.max_columns", None)

    """
    Работаем с данными из папок с параметрами качества воздуха
    Удаляем ненужные столбцы ; корректируем имеющиеся
    """

    for filename in os.listdir(work_dir):
        directory = f"{work_dir}/{filename}"

        # TODO: Проверить нейминг: file, file_path.
        # Работаем с каждым файлом с имеющийся директории
        for file in os.listdir(directory):
            file_path = directory + f"/{file}"
            # Прочитываем массив данных
            data = pd.read_csv(file_path, delimiter=",")

            # Формируем массив только с интересующими строками
            data_new = data[
                ["AirPollutant", "Concentration", "DatetimeBegin", "AirQualityStation"]
            ]

            # TODO: Здесь скорее всего можно обойтись стандартным методами pandas или библиотекой datetime
            # Для корректировки "временного" столбца формирует список данных
            date_time_begin_data = data_new["DatetimeBegin"].tolist()

            # Корректируем каждое временное значение отрезая лишнее (формируем новый список значений времени)
            process_datetime = []
            for date_time in date_time_begin_data:
                process_datetime.append(date_time[0:19])

            # Создаем датасеты для конкантенации
            process_datetime_data = {"TIME": process_datetime}
            df_process_datetime_data = pd.DataFrame(process_datetime_data)
            df_data_new = data_new[
                ["AirPollutant", "Concentration", "AirQualityStation"]
            ]

            # Формируем конечный датасет
            data_final = pd.concat(
                [df_process_datetime_data, df_data_new], axis=1, join="inner"
            )

            # Если нет папки, то создаём
            if not os.path.isdir(f"{result_dir}/{filename}"):
                os.mkdir(f"{result_dir}/{filename}")

            result_dir_path = f"{result_dir}/{filename}/{file}"
            data_final.to_csv(result_dir_path)

            # Формируем датасет индексируемый по дате
            data = pd.read_csv(result_dir_path, parse_dates=["TIME"], index_col="TIME")
            data = data[["AirPollutant", "Concentration", "AirQualityStation"]]
            result_path = f"{result_dir}/{filename}/{file[0:26]}.pkl"
            data.to_pickle(result_path)


def calculate_basic_statistics(work_dir):
    """
    Функция рассчитывает основные статистики для вещественных и категориальных признаков.
    Выводит количество отсутствующих значений.
    """
    # TODO: Проверь мой нейминг: file_path,filename,line т.к. возможно он неверный я не запускал
    for filename in os.listdir(work_dir):
        file_path = work_dir + f"/{filename}"

        # Работаем с каждым файлом с имеющийся директории
        for line in os.listdir(file_path):
            directory = file_path + f"/{line[0:26]}.pkl"

            # Прочитываем данные с индексированным временем
            data = pd.read_pickle(directory)

            # Подписываем выборку "загрязнитель", "год"
            print(filename[0:3], line[11:15])
            print(data[["Concentration"]].describe())

            # Проверяем на отсутствующие значения
            null_elements = []
            for element in data["Concentration"].isnull():
                null_elements.append(element)

            # Выводим кол-во отсутствующих значений
            print(f"Отсутствующих значений:{len(null_elements)}")


if __name__ == "__main__":
    clean_data(WORK_DIR_PATH, RESULT_DIR_PATH)
    calculate_basic_statistics(WORK_DIR_PATH)
