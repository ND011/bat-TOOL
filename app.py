import os
import pandas as pd

folder = r"C:\0ND\Project\ibm\fake_news_detector\NEWS dete\DATA"

for filename in os.listdir(folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder, filename)
        try:
            df = pd.read_csv(file_path, nrows=1, encoding='utf-8')
            print(f"\n📄 {filename}")
            print("Columns:", list(df.columns))
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, nrows=1, encoding='ISO-8859-1')
                print(f"\n📄 {filename}")
                print("Columns:", list(df.columns))
            except Exception as e:
                print(f"\n❌ {filename} — Failed to read: {e}")
        except Exception as e:
            print(f"\n❌ {filename} — Failed to read: {e}")
