import glob
import os

import numpy as np
import pandas as pd
import scipy as sc


def concat_files_to_df(path):
    # Собираем данные в один датасет
    files = glob.glob(os.path.join(path, "*.csv"))
    data = [pd.read_csv(filename, index_col=None, header=0) for filename in files]
    return pd.concat(data, axis=0, ignore_index=True)


def validate_data(dataframe):
    # Отбираем только валидные данные
    clean_dataframe = dataframe[dataframe["Validity"] == 1].copy()
    return clean_dataframe


def count_not_valid_rows(dataframe):
    # Подсчитаем количество невалидных строк
    not_valid_data_df = dataframe[dataframe["Validity"] != 1]
    cnt_all_data, _ = dataframe.shape
    cnt_not_valid_data, _ = not_valid_data_df.shape
    percentage_not_valid_data = round((cnt_not_valid_data / cnt_all_data) * 100, 2)
    return f"Количество ошибочных значений: {cnt_not_valid_data} в процентном отношении {percentage_not_valid_data}"


def process_data(main_path, dir):
    # Обработка сырых данных из файлов
    path = main_path + dir

    raw_df = concat_files_to_df(path)
    valid_df = validate_data(raw_df)
    valid_df["date"] = pd.to_datetime(valid_df["DatetimeBegin"])
    valid_df.sort_values(["AirQualityStation", "DatetimeBegin"], inplace=True)

    # https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf
    if dir in ["CO", "O3"]:
        valid_df[f"{dir}_Concentration"] = (
            valid_df.groupby("AirQualityStation")["Concentration"]
            .rolling(window=8, min_periods=1)
            .max()
            .values
        )
    else:
        valid_df[f"{dir}_Concentration"] = (
            valid_df.groupby("AirQualityStation")["Concentration"]
            .rolling(window=24, min_periods=1)
            .mean()
            .values
        )

    return valid_df.groupby([valid_df["date"].dt.date]).mean(
        numeric_only=True
    ).reset_index(), count_not_valid_rows(raw_df)


def make_processed_dataframes(main_path, dirs, print_result=True):
    processed_dfs = {}
    for dir in dirs:
        df, validated_info = process_data(main_path, dir)
        processed_dfs[dir] = df
        if print_result:
            print(f"{dir} - {validated_info}")
    return processed_dfs


def get_result_data(*args, **kwargs):
    processed_dfs = make_processed_dataframes(*args, **kwargs)
    # Соберём в один df и удалим дублирующие строки
    marked_by_pollutant_data = []
    for pollutant, pollutant_df in processed_dfs.items():
        marked_by_pollutant_data.append(pollutant_df)

    marked_df = pd.concat(marked_by_pollutant_data, axis=1)
    marked_df["Date"] = marked_df.iloc[:, 0]

    duplicate_cols = marked_df.columns[marked_df.columns.duplicated()]
    marked_df.drop(columns=duplicate_cols, inplace=True)

    # Найдём индекс по каждому загрязнителю
    marked_df["SO2_index"] = marked_df["SO2_Concentration"].apply(
        lambda x: get_so2_index(x)
    )
    marked_df["PM10_index"] = marked_df["PM10_Concentration"].apply(
        lambda x: get_10pm_index(x)
    )
    marked_df["PM2.5_index"] = marked_df["PM2.5_Concentration"].apply(
        lambda x: get_25pm_index(x)
    )
    marked_df["O3_index"] = marked_df["O3_Concentration"].apply(
        lambda x: get_o3_index(x)
    )
    marked_df["NO2_index"] = marked_df["NO2_Concentration"].apply(
        lambda x: get_no2_index(x)
    )
    marked_df["CO_index"] = marked_df["CO_Concentration"].apply(
        lambda x: get_co_index(x)
    )

    # Найдём общий индекс воздуха
    marked_df["aqi"] = (
        marked_df[
            [
                "SO2_index",
                "PM10_index",
                "PM2.5_index",
                "O3_index",
                "NO2_index",
                "CO_index",
            ]
        ]
        .max(axis=1)
        .astype(int)
    )
    return marked_df


def get_so2_index(x):
    # SO2 index calculation
    x = x / 2.62  # 1 ppb = 2.62 µg/m3
    if x <= 35:
        return 50 / 35 * x
    elif x <= 75:
        return (100 - 51) / (75 - 36) * (x - 36) + 51
    elif x <= 185:
        return (150 - 101) / (185 - 76) * (x - 76) + 101
    elif x <= 304:
        return (200 - 151) / (304 - 186) * (xb - 186) + 151
    elif x <= 604:
        return (300 - 201) / (604 - 305) * (x - 305) + 201
    elif x <= 804:
        return (400 - 301) / (804 - 605) * (x - 605) + 301
    elif x <= 1004:
        return (500 - 401) / (1004 - 805) * (x - 805) + 401


def get_o3_index(x):
    # O3 index calculation
    x = x / 1000  # 1 ppm = 1000 μg/m3
    if x <= 0.054:
        return 50 / 0.054 * x
    elif x <= 0.070:
        return (100 - 51) / (0.070 - 0.055) * (x - 0.055) + 51
    elif x <= 0.085:
        return (150 - 101) / (0.085 - 0.071) * (x - 0.071) + 101
    elif x <= 0.105:
        return (200 - 151) / (0.105 - 0.086) * (x - 0.086) + 151
    elif x <= 0.200:
        return (300 - 201) / (0.200 - 0.106) * (x - 0.106) + 201


def get_no2_index(x):
    # NO2 index calculation
    x = x / 1.88  # 1 ppb = 1.88 µg/m3
    if x <= 53:
        return 50 / 53 * x
    elif x <= 100:
        return (100 - 51) / (100 - 54) * (x - 54) + 51
    elif x <= 360:
        return (150 - 101) / (360 - 101) * (x - 101) + 101
    elif x <= 649:
        return (200 - 151) / (649 - 361) * (x - 361) + 151
    elif x <= 1249:
        return (300 - 201) / (1249 - 650) * (x - 650) + 201
    elif x <= 1649:
        return (400 - 301) / (1649 - 1250) * (x - 1250) + 301
    elif x <= 2049:
        return (500 - 401) / (2049 - 1650) * (x - 1650) + 401


def get_co_index(x):
    # CO index calculation
    x = x / 1000  # 1 ppm = 1000 mg/m3
    if x <= 4.4:
        return 50 / 4.4 * x
    elif x <= 9.4:
        return (100 - 51) / (9.4 - 4.5) * (x - 4.5) + 51
    elif x <= 12.4:
        return (150 - 101) / (12.4 - 9.5) * (x - 9.5) + 101
    elif x <= 15.4:
        return (200 - 151) / (15.4 - 12.5) * (x - 12.5) + 151
    elif x <= 30.4:
        return (300 - 201) / (30.4 - 15.5) * (x - 15.5) + 201
    elif x <= 40.4:
        return (400 - 301) / (40.4 - 30.5) * (x - 30.5) + 301
    elif x <= 50.4:
        return (500 - 401) / (50.4 - 40.5) * (x - 40.5) + 401


def get_25pm_index(x):
    # 2.5PM index calculation
    if x <= 12.0:
        return 50 / 12 * x
    elif x <= 35.4:
        return (100 - 51) / (35.4 - 12.1) * (x - 12.1) + 51
    elif x <= 55.4:
        return (150 - 101) / (55.4 - 35.5) * (x - 35.5) + 101
    elif x <= 150.4:
        return (200 - 151) / (150.4 - 55.5) * (x - 55.5) + 151
    elif x <= 250.4:
        return (300 - 201) / (250.4 - 150.5) * (x - 150.5) + 201
    elif x <= 350.4:
        return (400 - 301) / (350.4 - 250.5) * (x - 250.4) + 301
    elif x <= 500.4:
        return (500 - 401) / (500.4 - 350.5) * (x - 350.5) + 401


def get_10pm_index(x):
    # 10PM index calculation
    if x <= 54:
        return 50 / 54 * x
    elif x <= 154:
        return (100 - 51) / (154 - 55) * (x - 55) + 51
    elif x <= 254:
        return (150 - 101) / (254 - 155) * (x - 155) + 101
    elif x <= 354:
        return (200 - 151) / (354 - 255) * (x - 255) + 151
    elif x <= 424:
        return (300 - 201) / (424 - 355) * (x - 355) + 201
    elif x <= 504:
        return (400 - 301) / (504 - 425) * (x - 425) + 301
    elif x <= 604:
        return (500 - 401) / (604 - 505) * (x - 505) + 401


def get_autoregrmatrix(x, h, K):
    T = len(x)
    X = sc.linalg.hankel(x[: T - h - K + 1], np.hstack((x[T - h - K : T - h])))
    y = x[K + h - 1 :]
    return X, y
