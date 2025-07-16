import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"[✘] File not found: {filepath}")
        return None
    try:
        df = pd.read_csv(filepath)
        print("[✓] Data loaded successfully.")
        return df
    except Exception as e:
        print(f"[✘] Error loading data: {e}")
        return None

def clean_data(df):
    return df.dropna()

def plot_line_chart(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Month'], df['Revenue'], marker='o', color='green')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.savefig("Line_Chart.png")
    plt.close()

def plot_bar_chart(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['Product'], df['Sales'], color='orange')
    plt.title('Product Sales')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.savefig("Bar_Chart.png")
    plt.close()

def plot_pie_chart(df):
    plt.figure(figsize=(8, 8))
    grouped = df.groupby("Region")["MarketShare"].sum()
    plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90)
    plt.title('Market Share by Region')
    plt.savefig("Pie_Chart.png")
    plt.close()

def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include='number')  # ✅ Only numeric columns
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.savefig("Heatmap.png")
    plt.close()

def generate_summary(df):
    with open("Summary_Report.txt", "w", encoding="utf-8") as f:
        f.write("📊 Data Summary Report\n")
        f.write("-" * 30 + "\n")
        f.write(str(df.describe()))
        f.write("\n\nCorrelation Matrix:\n")
        numeric_df = df.select_dtypes(include='number')
        f.write(str(numeric_df.corr()))
    print("[✓] Summary report saved.")


def main():
    file_path = "sales.csv"  # Make sure sales.csv is in the same folder
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        plot_line_chart(df)
        plot_bar_chart(df)
        plot_pie_chart(df)
        plot_correlation_heatmap(df)
        generate_summary(df)

if __name__ == "__main__":
    main()
