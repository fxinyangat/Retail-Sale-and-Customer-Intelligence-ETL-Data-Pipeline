import pandas as pd
import unicodedata

def clean_string(val):
    if isinstance(val, str):
        # Normalize weird unicode (e.g. √ß) and strip whitespace
        val = unicodedata.normalize("NFKD", val).encode("ascii", "ignore").decode("utf-8")
        return val.strip()
    return val

def extract_country_code(phone):
    if isinstance(phone, str) and phone.startswith("("):
        return phone[1:4].replace(")", "")
    return None

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 2. Clean all string-type fields
    for col in df.columns:
        df[col] = df[col].apply(clean_string)

    # 3. Normalize contact title to lowercase
    df["contacttitle"] = df["contacttitle"].str.lower()

    # 4. Create 'full_address'
    df["full_address"] = df["address"] + ", " + df["city"] + ", " + df["region"] + ", " + df["country"]

    # 5. Extract country code from phone
    df["country_code"] = df["phone"].apply(extract_country_code)

    # 6. Flag if from Latin America
    latin_american_countries = ["brazil", "venezuela", "argentina", "chile", "colombia"]
    df["is_latin_america"] = df["country"].str.lower().isin(latin_american_countries)

    # 7. Drop unused columns
    df.drop(columns=["fax"], inplace=True)

    # 8. Reorder columns
    final_cols = [
        "customerid", "companyname", "contactname", "contacttitle",
        "full_address", "postalcode", "country", "country_code", "is_latin_america", "phone"
    ]
    df = df[final_cols]

    return df