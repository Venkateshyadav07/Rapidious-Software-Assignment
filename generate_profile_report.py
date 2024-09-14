import pandas as pd
import sweetviz as sv

# Load the dataset
dataset_path = r"C:\Users\venkatesh\Downloads\epi_r_processed (1).csv"
df = pd.read_csv(dataset_path)

# Generate a profile report
report = sv.analyze(df)

# Save the report to an HTML file
report.show_html("epi_r_processed_sweetviz_report.html")

print("Sweetviz report saved as 'epi_r_processed_sweetviz_report.html'")
