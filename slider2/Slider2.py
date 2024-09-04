
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def bengali_converter(pre):
    pre_int = int(pre) - 1
    pre_float = pre - pre_int
    bangla_list = [['Poush','Magh'],['Magh','Falgun'],['Falgun','chaitra'],['chaitro','Boisakh'],['Boisakh','Joistho'],['Joistho','Ashar'],['Ashar','shraban'],['shraban','bhadro'],['bhadro','ashwin'],['ashwin','kartik'],['kartik','agrahayan'],['agrahayan','Poush']]
    bangla_month_list = bangla_list[pre_int]
    if pre_float > 0.5:
        bangla_month = bangla_month_list[1]
        if pre_float > 0.75 :
            bangla_week = 2
        else:
            bangla_week = 1
    else:
        bangla_month = bangla_month_list[0]
        if pre_float > 0.25 :
            bangla_week = 2
        else:
            bangla_week = 1
    return bangla_month,bangla_week


def get_month_and_week(number):
    number_int = int(number) - 1
    number_float = number - number_int
    if number_float > 0.5:
        if number_float > 0.75 :
            week = 4
        else:
            week = 3
    else:
        if number_float > 0.25 :
            week = 2
        else:
            week = 1
    return number_int,week


def model2(inputs,outputs,input_list):
    INFO = "F:\He_is_enough03 X UniqoXTech X Dreams\Academic\cse 2102\project\Agriqo\slider2\Agriqo(slider2).csv"
    data = pd.read_csv(INFO)

    data_without_duplicates = data.drop_duplicates()
    # print(data_without_duplicates.shape)

    # model = HistGradientBoostingClassifier(random_state=42)
    model = LinearRegression()
    model.fit(data_without_duplicates[inputs],data_without_duplicates[outputs])
    predicted_values=model.predict(data_without_duplicates[inputs])
    mse = mean_squared_error(data_without_duplicates[outputs], predicted_values)
    # print(mse)
    pre = model.predict([input_list])
    pre = pre[0][0]
    # print(pre[0][0])
    bangla_month,bangla_week = bengali_converter (pre)
    english_month,eng_week = get_month_and_week(pre)
    
    return pre,bangla_month,bangla_week,english_month,eng_week


agricultural_zone = 3
crop_list = ['Aman', 'red lentil', 'tomato', 'wheat/gom', 'banana',
       'robi brinjal', 'khorip brinjal', 'sugarcane', 'soybean', 'Boro',
       'potato', 'mango', 'robi pointed gourd', 'khorip pointed grourd',
       'pineapple', 'robi green chilli ', 'khorip green chilli', 'Tula',
       'Rabi Cucumber', 'Kharif cucumber', 'garlic', 'robi lau (gourd)',
       'khorip lau (grourd)', 'Khorip Mug 1', 'Robi Mug', 'Badam robi',
       'Badam Kharip - 1', 'Guava', 'jackfruit', 'indian jujube', 'jute',
       'licchi', 'corn khorip-1', 'corn robi', 'masterd seed',
       'robi onion', 'khorip onion', 'papaya', 'robi pumpkin Cucurbita',
       'khorip pumpkin Cucurbita', 'Aush']
# print(len(crop_list))
crop = 13
input_list = [agricultural_zone,crop]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
pre,bangla_month,bangla_week,english_month,eng_week= model2(['Agricultural zone','label count'],['month(chara)'],input_list)

print(f"week {eng_week} of {months[english_month]}<br/>week {bangla_week} of {bangla_month}")


