import pandas as pd

# Create a dictionary of all the frequencies
frequency_mean = {'0.25', '0.5', '1', '2', '4', '8'}


def calc_mean(list_left_ear, list_right_ear, gender, age):

    mean_left = 0
    mean_right = 0

    # Calculate the mean of both ears for every frequency
    frequency_mean['0.25'] = (list_left_ear[0] + list_right_ear[0]) / 2
    frequency_mean['0.5'] = (list_left_ear[1] + list_right_ear[1]) / 2
    frequency_mean['1'] = (list_left_ear[2] + list_right_ear[2]) / 2
    frequency_mean['2'] = (list_left_ear[3] + list_right_ear[3]) / 2
    frequency_mean['4'] = (list_left_ear[4] + list_right_ear[4]) / 2
    frequency_mean['8'] = (list_left_ear[5] + list_right_ear[5]) / 2

    # Calculate the total mean of the left ear
    for num in list_left_ear:
        mean_left += num

    # Calculate the total mean of the right ear
    for num in list_right_ear:
        mean_right += num

    mean_left = mean_left / 6
    mean_right = mean_right / 6

    mean = (mean_left + mean_right) / 2

    calc_age_related(mean, gender, age)


# Calculate the difference in age related hearing loss

def calc_age_related(mean, gender, age):

    # Choose sheetname according to gender and convert to openpyxl workbook
    if gender == "Kvinde":
        df = pd.read_excel("hearing_age.xlsx", sheetname="Kvinder")
    elif gender == "Mand":
        df = pd.read_excel("hearing_age.xlsx", sheetname="Maend")

    # Compare hearing loss for every frequency relative to the users age
    for age_num in df['Alder [år]']:
        if age in range(int(age_num[0:2]), int(age_num[3:])):
            age_range = age_num

    sort_df = df[df['Alder [år]'] == age_range]

    for k, v in frequency_mean.items():
        for freq in sort_df['Frekvens [kHz]']:
            if float(k) == freq:
                df2 = sort_df[sort_df['Frekvens [kHz]'] == freq]

# Calculate the noise induced hearing loss

def calc_noise_induced(mean, age_related_loss):

    noise_induced_loss = mean - age_related_loss






# Show the result

def show_result(mean, age_related, noise_induced):
    pass
