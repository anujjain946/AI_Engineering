import pandas as pd
import numpy as np

# -----------------------------
# Configuration
# -----------------------------
np.random.seed(42)
ROWS = 20000

# -----------------------------
# Generate Features
# -----------------------------
customer_id = np.arange(100001, 100001 + ROWS)

age = np.random.randint(18, 71, ROWS)

gender = np.random.choice(
    ["Male", "Female"],
    ROWS,
    p=[0.52, 0.48]
)

marital_status = np.random.choice(
    ["Single", "Married", "Divorced"],
    ROWS,
    p=[0.45, 0.45, 0.10]
)

education = np.random.choice(
    ["High School", "Graduate", "Post Graduate"],
    ROWS,
    p=[0.30, 0.45, 0.25]
)

occupation = np.random.choice(
    ["Student", "Employee", "Self-Employed", "Business", "Retired"],
    ROWS,
    p=[0.10, 0.50, 0.15, 0.15, 0.10]
)

annual_income = np.random.randint(20000, 150001, ROWS)

city_tier = np.random.choice(
    [1, 2, 3],
    ROWS,
    p=[0.30, 0.40, 0.30]
)

family_size = np.random.randint(1, 7, ROWS)

credit_score = np.random.randint(300, 901, ROWS)

purchase_history = np.random.randint(0, 41, ROWS)

avg_purchase_value = np.random.uniform(20, 1500, ROWS).round(2)

days_since_last_purchase = np.random.randint(1, 366, ROWS)

website_visits = np.random.randint(1, 31, ROWS)

app_usage_hours = np.random.uniform(1, 40, ROWS).round(1)

email_clicks = np.random.randint(0, 21, ROWS)

ads_clicked = np.random.randint(0, 11, ROWS)

discount_used = np.random.choice(
    [0, 1],
    ROWS,
    p=[0.35, 0.65]
)

loyalty_member = np.random.choice(
    [0, 1],
    ROWS,
    p=[0.45, 0.55]
)

cart_abandon_rate = np.random.uniform(0, 100, ROWS).round(2)

product_rating = np.random.uniform(1, 5, ROWS).round(1)

customer_satisfaction = np.random.randint(1, 11, ROWS)

payment_method = np.random.choice(
    ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking"],
    ROWS
)

device = np.random.choice(
    ["Mobile", "Desktop", "Tablet"],
    ROWS,
    p=[0.60, 0.25, 0.15]
)

# -----------------------------
# Purchase Probability Score
# -----------------------------
score = (
    (annual_income / 150000) * 15 +
    (credit_score / 900) * 20 +
    (purchase_history / 40) * 15 +
    (website_visits / 30) * 10 +
    (app_usage_hours / 40) * 10 +
    (email_clicks / 20) * 8 +
    (ads_clicked / 10) * 5 +
    loyalty_member * 8 +
    discount_used * 6 +
    (customer_satisfaction / 10) * 8 +
    (product_rating / 5) * 8 -
    (cart_abandon_rate / 100) * 15 -
    (days_since_last_purchase / 365) * 10
)

# Normalize score to probability
probability = 1 / (1 + np.exp(-(score - 45) / 8))

purchased = np.random.binomial(1, probability)

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame({
    "CustomerID": customer_id,
    "Age": age,
    "Gender": gender,
    "MaritalStatus": marital_status,
    "Education": education,
    "Occupation": occupation,
    "AnnualIncome": annual_income,
    "CityTier": city_tier,
    "FamilySize": family_size,
    "CreditScore": credit_score,
    "PurchaseHistory": purchase_history,
    "AvgPurchaseValue": avg_purchase_value,
    "DaysSinceLastPurchase": days_since_last_purchase,
    "WebsiteVisits": website_visits,
    "AppUsageHours": app_usage_hours,
    "EmailClicks": email_clicks,
    "AdsClicked": ads_clicked,
    "DiscountUsed": discount_used,
    "LoyaltyMember": loyalty_member,
    "CartAbandonRate": cart_abandon_rate,
    "ProductRating": product_rating,
    "CustomerSatisfaction": customer_satisfaction,
    "PaymentMethod": payment_method,
    "Device": device,
    "Purchased": purchased
})

# -----------------------------
# Save CSV
# -----------------------------
df.to_csv("dataset.csv", index=False)

print("=" * 50)
print("Dataset Generated Successfully!")
print("=" * 50)
print("Rows :", len(df))
print("Columns :", len(df.columns))
print("\nTarget Distribution:")
print(df["Purchased"].value_counts())
print("\nFirst 5 Rows:")
print(df.head())
print("\nCSV File Saved As : customer_purchase.csv")