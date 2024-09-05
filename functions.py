import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def leer_datos(shark_url):

    archivo = pd.read_excel(shark_url)
    return archivo


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

def top_5_country(df_mvp):
    group = df_mvp.groupby('country').size().reset_index(name='count')
    top_5 = group.sort_values(by='count', ascending=False).head(5)

    return top_5

def top_5_activities(df_mvp):
    group_activity = df_mvp.groupby('activity').size().reset_index(name='count')
    top_5_activity = group_activity.sort_values(by='count', ascending=False).head(5)

    return top_5_activity
    
def top_sex(df_mvp):
    group_sex = df_mvp.groupby('sex').size().reset_index(name='count')
    top_sexs = group_sex.sort_values(by='count', ascending=False).head(3)

    return top_sexs

def show_top(data, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x_col, y=y_col, data=data)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=0)

    for index, value in enumerate(data[y_col]):
        plt.text(index, value, str(value), ha='center', va='bottom')

    plt.show()

