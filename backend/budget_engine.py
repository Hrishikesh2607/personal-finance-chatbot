import pandas as pd
from datetime import datetime

DATA_PATH= "rasa_data/transactions.csv"

def load_transaction():
    df=pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'], format='mixed')
    return df

def get_monthly_spending(category):
    df = load_transaction()
    df = filter_curr_month(df)

    if category not in df['category'].unique():
        return 0

    return df[df['category'] == category]['amount'].sum()

def filter_curr_month(df):
    now= datetime.now()
    return df[
        (df['date'].dt.month==now.month) &
        (df['date'].dt.year==now.year)
    ]

def get_monthly_by_category(category):
    df=load_transaction()
    df=filter_curr_month(df)
    df=df[df['category']==category]
    return df['amount'].sum()

def monthly_summary():
    df= load_transaction()
    df=filter_curr_month(df)
    if df.empty:
        return 0
    return df.groupby('category')['amount'].sum().to_dict()

BUDGET_PATH= "rasa_data/budgets.csv"

def load_budgets():
    return pd.read_csv(BUDGET_PATH)

def remaining_budget(category):
    budgets= load_budgets()
    limit= budgets[budgets['category']== category]['monthly_limit']

    if limit.empty:
        return None
    
    spend= get_monthly_spending(category)
    return int(limit.values[0]- spend)

def budget_advice(category):
    remaining= remaining_budget(category)
    budgets= load_budgets()
    row = budgets[budgets['category'] == category]
    if row.empty:
     return "No budget set for this category."

    limit = row['monthly_limit'].values[0]


    if remaining is None:
        return "No budget set for this category."
    
    if remaining<0:
        return f"You have exceeded your {category} budget. Consider cutting back."
    elif remaining < 0.2*limit:
        return f"You are close to your {category} budget. Spend carefully."
    else:
        return f"You are doing well on your {category} spending."




