from src.data.load_data import load_data

def preprocess_data():
    df = load_data()
    
    print("Filtering Los Angeles data...")
    df = df[df['City'] == 'Los Angeles']
    
    print(f"Data after filtering: {df.shape}")
    
    output_path = "data/processed/los_angeles_accidents.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Data saved to: {output_path}")


if __name__ == "__main__":
    preprocess_data()