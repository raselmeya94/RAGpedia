import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the RAG-LIST.md file
with open('RAG-LIST.md', 'r') as file:
    content = file.read()

# Regex to extract publication dates (Assuming format "Published Date: DD MMM YYYY")
date_pattern = r"Published Date: (\d{1,2})\s([A-Za-z]+)\s(\d{4})"
dates = re.findall(date_pattern, content)

# Print extracted dates to ensure they are correct
print(f"Extracted Dates: {dates}")

# Convert the extracted dates to a pandas DataFrame
date_objects = [datetime.strptime(f"{day} {month} {year}", "%d %b %Y") for day, month, year in dates]
df = pd.DataFrame(date_objects, columns=['Publication Date'])

# Print the first few rows of the DataFrame for debugging
print(f"DataFrame Head: \n{df.head()}")

# Count the number of publications for each specific day
publication_count = df.groupby('Publication Date').size()

# Print the publication count by day to check the distribution
print(f"Publication Count by Day: \n{publication_count}")

# Plotting the data with day-wise x-axis
plt.figure(figsize=(12, 6))
publication_count.plot(kind='line', marker='o', color='b')

# Customize the plot
plt.title("Number of RAG Benchmarks Published per Day")
plt.xlabel("Date")
plt.ylabel("Number of Publications")
plt.grid(True)
plt.xticks(rotation=45)

# Ensure tight layout to avoid label overlap
plt.tight_layout()

# Save the plot as an image in the assets folder
plt.savefig('assets/publication_daywise_line_plot.png')

# Show the plot
plt.show()
