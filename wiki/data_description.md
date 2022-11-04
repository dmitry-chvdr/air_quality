* Данные по г. Берлин за период 2013-2020. Источник данных: https://discomap.eea.europa.eu/map/fme/AirQualityExport.htm
* Структура данных


| Field                    | Type     | Description                                                                                                          |
|--------------------------|----------|----------------------------------------------------------------------------------------------------------------------|
| Countrycode              | String   | Country iso code                                                                                                     |
| Namespace                | String   | Unique namespace as provided by the country                                                                          |
| AirQualityNetwork        | String   | Network identifier                                                                                                   |
| AirQualityStation        | String   | Localid of the station                                                                                               |
| AirQualityStationEoICode | String   | Unique station identifier as used in the past AirBase system                                                         |
| Samplingpoint            | String   | Localid of the samplingpoint                                                                                         |
| Samplingpoint            | String   | Localid of the samplingpoint                                                                                         |
| SamplingProcess          | String   | Localid of the samplingprocess                                                                                       |
| Sample                   | String   | Localid of the sample (also known as the feature of interest)                                                        |
| AirPollutant             | String   | Short name of pollutant. Full list: http://dd.eionet.europa.eu/vocabulary/aq/pollutant/view                          |
| AirPollutantCode         | String   | Reference (URL) to the definition of the pollutant in data dictonary                                                 |
| AveragingTime            | String   | Defines the time for which the measure have been taken (hour, day, etc)                                              |
| Concentration            | Value    | The measured value/concentration                                                                                     |
| UnitOfMeasurement        | String   | Defines the unit of the concentration                                                                                |
| DateTimeBegin            | Datetime | Defines the start time (yyyy-mm-dd hh:mm:ss Z) of the measurement (includes timezone)                                |
| DateTimeEnd              | Datetime | Defines the end time (yyyy-mm-dd hh:mm:ss Z)of the measurement (includes timezone)                                   |
| Validity                 | Integer  | The validity flag for the measurement. See http://dd.eionet.europa.eu/vocabulary/aq/observationvalidity/view         |
| Verification             | Integer  | The verification flag for the measurement. See http://dd.eionet.europa.eu/vocabulary/aq/observationverification/view |

* Загрязнители

| Загрязнитель | Описание                                                                                                                                                                                                                                                                                    |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CO           | Бесцветный газ не имеющий запаха известен также под названием «угарный газ».Образуется в результате неполного сгорания ископаемого топлива  в условиях недостатка кислорода и при низкой температуре.                                                                                       |
| SO2          | Образуется в процессе сгорания серосодержащих ископаемых видов топлива в основном угля а также при переработке сернистых руд.Он в первую очередь участвует в формировании кислотных дождей.                                                                                                 |
| NO2          | При всех процессах горения образуются окислы азота причем большей частью в виде оксида.Чем выше температура сгорания тем интенсивнее идет образование окислов азота.                                                                                                                        |
| O3           | Газ с характерным запахом более сильный окислитель чем кислород.Его относят к наиболее токсичным из всех обычных загрязняющих воздух примесей. В нижнем атмосферном слое озон образуется в результате фотохимических процессов с участием диоксида азота и летучих органических соединений. |
| PM2.5        | Мелкодисперсные взвешенные частицы ≤ 2.5 микрон.                                                                                                                                                                                                                                            |
| PM10         | Крупнодисперсные твердые частицы частицы  2.5 ≤ x ≤ 10 микрон.                                                                                                                                                                                                                              |                                                                                                                                                                                                                            |