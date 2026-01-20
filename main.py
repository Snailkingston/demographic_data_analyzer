import pandas as pd

def count_by_race(df):
    return df['race'].value_counts()

def average_age_men(df):
    return round(df[df['sex']=='Male']['age'].mean(), 1)

def percentage_bachelors(df):
    return round((df['education']=='Bachelors').mean()*100, 1)

def percentage_advanced_edu_rich(df):
    adv_ed = ['Bachelors', 'Masters', 'Doctorate']
    total = df[df['education'].isin(adv_ed)]
    return round((total[total['salary']=='>50K'].shape[0]/total.shape[0])*100, 1)

def percentage_non_advanced_edu_rich(df):
    adv_ed = ['Bachelors', 'Masters', 'Doctorate']
    total = df[~df['education'].isin(adv_ed)]
    return round((total[total['salary']=='>50K'].shape[0]/total.shape[0])*100, 1)

def min_hours(df):
    return df['hours-per-week'].min()

def rich_percentage_min_hours(df):
    min_h = df['hours-per-week'].min()
    subset = df[df['hours-per-week']==min_h]
    return round((subset[subset['salary']=='>50K'].shape[0]/subset.shape[0])*100, 1)

def country_highest_earning(df):
    grouped = df.groupby('native-country')
    perc = ((grouped.apply(lambda x: (x['salary']=='>50K').sum()/x.shape[0]))*100).round(1)
    country = perc.idxmax()
    return country, perc[country]

def top_occupation_india_rich(df):
    subset = df[(df['native-country']=='India') & (df['salary']=='>50K')]
    return subset['occupation'].value_counts().idxmax()
