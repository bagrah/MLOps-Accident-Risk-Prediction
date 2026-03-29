from src.data.preprocess import preprocess_data

def run_pipeline():
    print("🚀 Starting Data Pipeline...\n")
    
    preprocess_data()
    
    print("\n✅ Pipeline finished successfully!")


if __name__ == "__main__":
    run_pipeline()