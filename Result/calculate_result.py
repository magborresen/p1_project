import pandas as pd
import json
import tkinter as tk

# Create a dictionary of all the frequencies
frequency_mean = {'250': 0, '500': 0, '1000': 0, '2000': 0, '4000': 0, '8000': 0}


def calc_mean():

    with open('../variables.json', 'r') as f:
        data = json.load(f)
        frequency_mean['250'] = (data["left_ear_test"]["250"] +
                                 data["right_ear_test"]["250"]) / 2
        frequency_mean['500'] = (data["left_ear_test"]["500"] +
                                 data["right_ear_test"]["500"]) / 2
        frequency_mean['1000'] = (data["left_ear_test"]["1000"] +
                                  data["right_ear_test"]["1000"]) / 2
        frequency_mean['2000'] = (data["left_ear_test"]["2000"] +
                                  data["right_ear_test"]["2000"]) / 2
        frequency_mean['4000'] = (data["left_ear_test"]["4000"] +
                                  data["right_ear_test"]["4000"]) / 2
        frequency_mean['8000'] = (data["left_ear_test"]["8000"] +
                                  data["right_ear_test"]["8000"]) / 2
        gender = data["Gender"]
        age = data["Age"]


    print ("Frequency mean: ")
    print (frequency_mean)
    mean = 0

    for k, v in frequency_mean.items():
        mean = mean + v

    mean = mean / 6
    print ("Mean total: " + str(mean))

    with open("../variables.json", "r+") as f:
        data = json.load(f)
        data["mean"] = mean
        f.seek(0)
        json.dump(data, f)
        f.truncate()

    calc_age_related_new(frequency_mean, gender, age)


def calc_age_related_new(mean, gender, age):

    age_related_loss_new = {'250':0,
                            '500':0,
                            '1000':0,
                            '2000':0,
                            '4000':0,
                            '8000':0}
    
    if gender == "Kvinde":
        df = pd.read_excel("Hearing_data.xlsx", sheet_name="Female")
        df_median = pd.read_excel("Hearing_data.xlsx", sheet_name="Median_Female")
    else:
        df = pd.read_excel("Hearing_data.xlsx", sheet_name="Male")
        df_median = pd.read_excel("Hearing_data", sheet_name="Median_Male")

    for k, v in mean.items():
        for freq in df_median['Hz']:
            if int(k) == freq:
                sorted_df_median = df_median[df_median['Hz'] == freq]
                alpha = sorted_df_median['alpha'][0]
                beta = sorted_df_median['beta'][0]
                calc_median = alpha*(age-18)**beta
                calc_loss = mean[k] - calc_median
                age_related_loss_new[k] = calc_loss


    with open("../variables.json", "r+") as f:
        data = json.load(f)
        data["age_related_loss"]["250"] = age_related_loss_new["250"]
        data["age_related_loss"]["500"] = age_related_loss_new["500"]
        data["age_related_loss"]["1000"] = age_related_loss_new["1000"]
        data["age_related_loss"]["2000"] = age_related_loss_new["2000"]
        data["age_related_loss"]["4000"] = age_related_loss_new["4000"]
        data["age_related_loss"]["8000"] = age_related_loss_new["8000"]
        f.seek(0)
        json.dump(data, f)
        f.truncate()


# Calculate the difference in age related hearing loss

def calc_age_related(mean, gender, age):

    age_related_loss = {'250': 0,
                        '500': 0,
                        '1000': 0,
                        '2000': 0,
                        '4000': 0,
                        '8000': 0}

    # Choose sheetname according to gender and convert to openpyxl workbook
    if gender == "Kvinde":
        df = pd.read_excel("Hearing_data.xlsx", sheet_name="Female")
    elif gender == "Mand":
        df = pd.read_excel("Hearing_data.xlsx", sheet_name="Male")

    # Compare hearing loss for every frequency relative to the users age
    for age_num in df['Alder [år]']:
        if age in range(int(age_num[0:2]), int(age_num[3:])):
            age_range = age_num

    sort_df = df[df['Alder [år]'] == age_range]

    for k, v in mean.items():
        for freq in sort_df['Frekvens [Hz]']:
            if int(k) == freq:
                df2 = sort_df[sort_df['Frekvens [Hz]'] == freq]
                if float(v) <= df2.iat[0, 2]:
                    print ("Ingen nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))
                elif float(v) <= df2.iat[0, 3]:
                    print ("Svag nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))
                elif float(v) <= df2.iat[0, 4]:
                    print ("Moderat nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))
                elif float(v) <= df2.iat[0, 5]:
                    print ("Alvorlig nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))
                elif float(v) <= df2.iat[0, 6]:
                    print ("Dybtgående nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))
                else: 
                    print ("Uden for skala")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                    print (float(v) - float(df2.iat[0, 2]))

    print ("Age related loss: ")
    print (age_related_loss)

    with open("../variables.json", "r+") as f:
        data = json.load(f)
        data["age_related_loss"]["250"] = age_related_loss["250"]
        data["age_related_loss"]["500"] = age_related_loss["500"]
        data["age_related_loss"]["1000"] = age_related_loss["1000"]
        data["age_related_loss"]["2000"] = age_related_loss["2000"]
        data["age_related_loss"]["4000"] = age_related_loss["4000"]
        data["age_related_loss"]["8000"] = age_related_loss["8000"]
        f.seek(0)
        json.dump(data, f)
        f.truncate()
