import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def leer_datos(shark_url):

    archivo = pd.read_excel(shark_url)
    return archivo


def leer_datos(url):
  
    df = pd.read_excel(url)
    return df

def clean_data(df):

    pd.set_option("display.max_columns", None)
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")   

    df = df.dropna(subset = ["date"])

    df = df[df["year"] != 0.0]

    df["year"] = df["year"].astype("Int64")

    año_inicio = 1974
    año_final = 2024
    df = df[(df["year"] >= año_inicio) & (df["year"] <= año_final)]

    df = df.drop(columns = ["pdf", "href_formula", "href", "case_number", "case_number.1", "original_order", "unnamed:_21", "unnamed:_22"])

    df = df.rename(columns = {"unnamed:_11": "fatal"})

    df["activity"] = df["activity"].fillna("Unknown")
    df["name"] = df["name"].fillna("Unknown")
    df["sex"] = df["sex"].fillna("U")
    df["species"] = df["species"].fillna("Unknown")
    df["fatal"] = df["fatal"].fillna("N")

    return df

def choosen_columns(df):

    target_columns = ["date", "year", "country", "state", "activity", "sex", "fatal"]
    df_mvp = df[target_columns]

    return df_mvp

def null_and_duplicates(df_mvp):
    df_mvp = df_mvp.dropna(subset=["country"])
    #df_mvp["country"].isnull().value_counts()

    df_mvp = df_mvp.drop_duplicates()

    return df_mvp

def value_and_type_change(df_mvp):
    df_mvp.loc[:, "country"] = df_mvp["country"].str.upper()
    #df_mvp["fatal"].unique()

    df_mvp.loc[:, 'fatal'] = df_mvp['fatal'].replace({'Y': 1, 'N': 0, "M": 0, "F": 0, "n": 0, "Nq": 0, "UNKNOWN": 0, 2017: 0, "Y x 2": 0})
    #df_mvp["fatal"].unique()

    df_mvp.loc[:, "fatal"] = df_mvp["fatal"].astype("int64")
    #df_mvp.dtypes

    return df_mvp

def pivot_table(df_mvp):
    pivot_fatal = df_mvp.pivot_table(values="fatal", index=["country", "year"], aggfunc="sum")

    print("Ataques fatales por año y país")

    return pivot_fatal


def top_5_country(df):
    group = df.groupby('country').size().reset_index(name='count')
    top_5 = group.sort_values(by='count', ascending=False).head(5)

    return top_5

def top_5_activities(df):
    group_activity = df.groupby('activity').size().reset_index(name='count')
    top_5_activity = group_activity.sort_values(by='count', ascending=False).head(5)

    return top_5_activity
    
def top_sex(df):
    group_sex = df.groupby('sex').size().reset_index(name='count')
    top_sexs = group_sex.sort_values(by='count', ascending=False).head(3)

    return top_sexs

def print_country(top_5):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='country', y='count', data=top_5)

    plt.title('SharkAttack last 50 years')
    plt.xlabel('Country')
    plt.ylabel('Attacks')
    plt.xticks(rotation=45)
    for index, value in enumerate(top_5['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')    

    return plt.show()

def print_activity(top_5_activity):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='activity', y='count', data=top_5_activity)

    plt.title('Activities more attacked')
    plt.xlabel('Activity')
    plt.ylabel('Attacks')
    plt.xticks(rotation=45)
    for index, value in enumerate(top_5_activity['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')  

    show_activity = plt.show()
    return show_activity

def print_top_sex(top_sexs):
    plt.figure(figsize=(12, 8))
    sns.barplot(x='sex', y='count', data=top_sexs)

    plt.title('Attack by sex')
    plt.xlabel('Sex')
    plt.ylabel('Attacks')
    plt.xticks(rotation=0)

    for index, value in enumerate(top_sexs['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')  

    show_top_sex = plt.show()
    return show_top_sex

def show_top(data, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x_col, y=y_col, data=data)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=0)

    for index, value in enumerate(data[y_col]):
        plt.text(index, value, str(value), ha='center', va='bottom')

    return plt.show()

