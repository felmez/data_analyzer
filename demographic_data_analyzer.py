import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', index_col=None, sep=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']
    average_age_men = round(average_age_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(percentage_bachelors) / len(df.education == 'Bachelors'))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[
        ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))])
    educated_and_rich = df[
        ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
        & (df['salary'] == '>50K')]
    lower_education = len(df[
        ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))])
    uneducated_and_rich = len(df[
        ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))
        & (df['salary'] == '>50K')])

    # percentage with salary >50K
    higher_education_rich = round((len(educated_and_rich) / higher_education)*100,1)
    lower_education_rich = round((uneducated_and_rich / lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == 1])
    rich_percentage = len(df[
    ((df['hours-per-week'] == 1) & (df['salary'] == '>50K'))])
    rich_percentage = round((rich_percentage / num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    top_country = ''
    top_percentage = 0
    earn_over_50k = df[df['salary'] == '>50K']
    country_count_over_50k = earn_over_50k['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    for k,v in country_count_over_50k.items():
        #print('>50k',k,v)
        percentage = v/country_counts[k]
        if percentage >= top_percentage:
            top_percentage = percentage
            top_country = k
    top_percentage = round(top_percentage * 100,1)
    highest_earning_country = top_country
    highest_earning_country_percentage = top_percentage

    # Identify the most popular occupation for those who earn >50K in India.
    india_jobs_over_50k =df[
        ((df['native-country'] == 'India') & (df['salary'] == '>50K'))]
    job_array = india_jobs_over_50k['occupation'].value_counts()
    job_index = 0
    top_job = ''
    for k,v in job_array.items():
        if job_index == 0:
            top_job = k
            job_index += 1
    top_IN_occupation = top_job

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
