import pandas as pd

def load_data(nrows=50000):
    """
    Load sebagian data dari dataset besar (raw data)
    
    Parameters:
    nrows (int): jumlah baris yang ingin di-load (default: 50000)
    
    Returns:
    df (DataFrame): data mentah
    """
    
    # 📂 Path ke data raw
    file_path = "data/raw/US_Accidents_March23.csv"
    
    print("Loading data...")
    
    try:
        df = pd.read_csv(file_path, nrows=nrows)
        print(f"Data loaded successfully: {df.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
    return df


# 🔍 Untuk testing langsung
if __name__ == "__main__":
    df = load_data()
    
    if df is not None:
        print("\nPreview data:")
        print(df.head())