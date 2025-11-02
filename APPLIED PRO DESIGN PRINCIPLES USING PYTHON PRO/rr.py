Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... import matplotlib.pylab as plt
... from abc import ABC,abstractmethod
... from datetime import datetime
... 
... class Analysis(ABC):
...     @abstractmethod
...     def performAnalysis():
...         pass
... 
... class PublicationTrendsOverTime(Analysis):
...     def performanceAnalysis(self):
...        # Load CSV file
...        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
...        # Clean up column names
...        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
...        data.columns = (columns)
...        # Convert year to numeric
...        data['publication date'] = pd.to_numeric(data['publication date'], errors='coerce')
...        # 1. Publication Trends Over Time
...        print("\n--- Books Published Per Year ---")
...        books_per_year = data['publication date'].value_counts().sort_index()
...        print(books_per_year)
...        books_per_year.plot(kind='line')
...        plt.xlabel('Year')
...        plt.ylabel('Number of Books')
...        plt.title("Books Published Per Year")
...        plt.show()
...        
SyntaxError: multiple statements found while compiling a single statement
