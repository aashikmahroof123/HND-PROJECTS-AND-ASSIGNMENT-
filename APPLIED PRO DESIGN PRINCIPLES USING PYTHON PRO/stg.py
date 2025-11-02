import pandas as pd
import matplotlib.pyplot as plt  # Correct import
from abc import ABC, abstractmethod
from datetime import datetime

class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):
        pass

class PublicationTrendsOverTime(Analysis):
    def performAnalysis(self):
        try:
            # Load CSV file
            data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
            
            # Rename columns if necessary
            columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
            data.columns = columns

            # Convert publication date to numeric
            data['publication date'] = pd.to_numeric(data['publication date'], errors='coerce')

            # Drop NaN years
            data = data.dropna(subset=['publication date'])

            # Group by year
            print("\n--- Books Published Per Year ---")
            books_per_year = data['publication date'].value_counts().sort_index()
            print(books_per_year)

            # Plotting
            books_per_year.plot(kind='line', figsize=(10, 5))
            plt.xlabel('Year')
            plt.ylabel('Number of Books')
            plt.title("Books Published Per Year")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
