import pandas as pd
import numpy as np

# Create date range
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

def generate_solar_data(country):
    np.random.seed(len(country))  # makes results stable per country

    return pd.DataFrame({
        "Date": dates,
        "GHI": np.random.uniform(4, 7, size=len(dates)).round(2),  # Global Horizontal Irradiance
        "DNI": np.random.uniform(3, 6, size=len(dates)).round(2),  # Direct Normal Irradiance
        "DHI": np.random.uniform(1, 3, size=len(dates)).round(2),  # Diffuse Horizontal Irradiance
        "Temperature": np.random.uniform(20, 35, size=len(dates)).round(1),
        "WindSpeed": np.random.uniform(1, 6, size=len(dates)).round(2)
    })

# Generate datasets for each country
benin = generate_solar_data("benin")
sierra = generate_solar_data("sierra_leone")
togo = generate_solar_data("togo")

# Save datasets
benin.to_csv("data/benin_clean.csv", index=False)
sierra.to_csv("data/sierra_leone_clean.csv", index=False)
togo.to_csv("data/togo_clean.csv", index=False)

print("Datasets created successfully!")
