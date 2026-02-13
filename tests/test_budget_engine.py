from backend.budget_engine import (
    get_monthly_spending,
    remaining_budget,
    budget_advice,
    monthly_summary
)

def test_spending_food():
    assert get_monthly_spending("food") >=0

def test_remaining_budget():
    remaining= remaining_budget("food")
    assert remaining is not None

def test_budget_advice():
    advice= budget_advice("food")
    assert isinstance(advice, str)

def test_unknown_category():
    assert get_monthly_spending("unknown")==0

def test_monthly_summary():
    summary= monthly_summary()
    assert isinstance(summary, dict)

