import pandas as pd
import json

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


    #mean_left = 0
    #mean_right = 0


    # Calculate the total mean of the left ear
    #for num in list_left_ear:
    #    mean_left += num

    # Calculate the total mean of the right ear
    #for num in list_right_ear:
    #    mean_right += num

    #mean_left = mean_left / 6
    #print ("Mean left: " + str(mean_left))
    #mean_right = mean_right / 6
    #print ("Mean right: " + str(mean_right))

    print ("Frequency mean: ")
    print (frequency_mean)
    mean = 0

    for k, v in frequency_mean.items():
        mean = mean + v

    mean = mean / 6
    print ("Mean total: " + str(mean))

    with open("../variables.json", "r+") as f:
        data = json.load(f)
        #data["mean_left"] = mean_left
        #data["mean_right"] = mean_right
        data["mean"] = mean
        f.seek(0)
        json.dump(data, f)
        f.truncate()

    calc_age_related(frequency_mean, gender, age)


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
        df = pd.read_excel("../Result/hearing_age.xlsx", sheet_name="Kvinder")
    elif gender == "Mand":
        df = pd.read_excel("../Result/hearing_age.xlsx", sheet_name="Maend")

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
                elif float(v) <= df2.iat[0, 3]:
                    print ("Svag nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                elif float(v) <= df2.iat[0, 4]:
                    print ("Moderat nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                elif float(v) <= df2.iat[0, 5]:
                    print ("Alvorlig nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])
                elif float(v) <= df2.iat[0, 6]:
                    print ("Dybtgående nedsættelse")
                    age_related_loss[k] = float(v) - float(df2.iat[0, 2])

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

    calc_noise_induced(mean, age_related_loss)


# Calculate the noise induced hearing loss

def calc_noise_induced(mean, age_related_loss):

    noise_induced_loss = {'250': 0,
                          '500': 0,
                          '1000': 0,
                          '2000': 0,
                          '4000': 0,
                          '8000': 0}

    for k, v in mean.items():
        for f, h in age_related_loss.items():
            if int(f) > 0:
                loss = float(v) - float(h)
                noise_induced_loss[k] = loss
            else:
                pass

    print ("Noise induced loss: ")
    print (noise_induced_loss)

    with open("../variables.json", "r+") as f:
        data = json.load(f)
        data["noise_induced_loss"]["250"] = noise_induced_loss["250"]
        data["noise_induced_loss"]["500"] = noise_induced_loss["500"]
        data["noise_induced_loss"]["1000"] = noise_induced_loss["1000"]
        data["noise_induced_loss"]["2000"] = noise_induced_loss["2000"]
        data["noise_induced_loss"]["4000"] = noise_induced_loss["4000"]
        data["noise_induced_loss"]["8000"] = noise_induced_loss["8000"]
        f.seek(0)
        json.dump(data, f)
        f.truncate()


# Show the result

def show_result(mean, age_related, noise_induced):
    pass
