import pandas as pd
import os

def ingest_data(nrows=50000):
    file_path = "data/raw/US_Accidents_March23.csv"
    
    print("Loading raw data...")
    df = pd.read_csv(file_path, nrows=nrows)
    
    # Convert ke datetime
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    
    # Filter Los Angeles
    df = df[df['City'] == 'Los Angeles']
    
    print(f"Total data LA: {df.shape}")
    
    # 🔥 Ambil bulan pertama yang ada
    df['year_month'] = df['Start_Time'].dt.to_period('M')
    
    first_period = df['year_month'].min()
    
    print(f"Selected period: {first_period}")
    
    df_month = df[df['year_month'] == first_period]
    
    print(f"Data for {first_period}: {df_month.shape}")
    
    # Simpan
    os.makedirs("data/raw/batch", exist_ok=True)
    
    output_file = f"data/raw/batch/accidents_{first_period}.csv"
    df_month.to_csv(output_file, index=False)
    
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    ingest_data()