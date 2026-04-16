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
    
    # Ambil periode per bulan
    df['year_month'] = df['Start_Time'].dt.to_period('M')
    
    # Ambil semua periode lalu pilih bulan ke-2
    all_periods = sorted(df['year_month'].unique())
    selected_period = all_periods[1]  # bulan ke-2
    
    print(f"Selected period: {selected_period}")
    
    df_month = df[df['year_month'] == selected_period]
    
    print(f"Data for {selected_period}: {df_month.shape}")
    
    # Simpan hasil
    os.makedirs("data/raw/batch", exist_ok=True)
    
    output_file = f"data/raw/batch/accidents_{selected_period}.csv"
    df_month.to_csv(output_file, index=False)
    
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    ingest_data()