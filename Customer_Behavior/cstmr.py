import pandas as pd

# Loading the dataset using pandas
df = pd.read_csv('cstmr_trends.csv')

# print(df.head)

# print(df.info())

# Summary statistics using .describe()
# print(df.describe(include='all'))

# Checking if missing data or null values are present in the dataset
# print(df.isnull().sum())

# Imputing missing values in Review Rating column with the median rating of the product category
# df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
# print(df.isnull().sum())

# Renaming columns according to snake casing for better readability and documentation
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
# print(df.columns)

# create a new column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
# print(df[['age','age_group']].head(10))

# create new column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

# print(df[['discount_applied','promo_code_used']].head(10))

# print((df['discount_applied'] == df['promo_code_used']).all()) 
# both are same columns show we drop the one of them

# Dropping promo code used column
df = df.drop('promo_code_used', axis=1)
# print(df.columns)

# Connecting Python script to PostgreSQL
# !pip install psycopg2-binary sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:urpass@localhost/customer_analysis')
df.to_sql('customer', engine, if_exists='replace', index=False)
import psycopg2
import sqlalchemy
import pandas 
print("All done successfully!")

# CSV -> Python -> PostgreSQL -> pgAdmin pipeline connection is complete




















































