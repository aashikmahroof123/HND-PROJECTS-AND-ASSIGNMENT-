
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):
        pass


class PublicationTrendsOverTime(Analysis):
    def performAnalysis(self):
        #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Books Published Per Year")
        books_per_year = data['publication date'].value_counts().sort_index()
        print(books_per_year)
        books_per_year.plot(kind='line')
        plt.xlabel('Year')
        plt.ylabel('Number of Books')
        plt.title("Books Published Per Year")
        plt.show()


class Top5Authors(Analysis):
    def performAnalysis(self):
          #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
           #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Top 5 Authors by Number of Books")
        author_counts = data['author'].value_counts().head(5)
        print(author_counts)
        author_counts.plot(kind='bar', title='Top 5 Authors')
        plt.ylabel('Books Written')
        plt.show()


class LanguageDistribution(Analysis):
    def performAnalysis(self):
          #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
           #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Language Distribution")
        language_counts = data['language'].value_counts()
        print(language_counts)
        language_counts.plot(kind='pie', autopct='%1.1f%%', title='Languages of Books')
        plt.ylabel('')
        plt.show()


class BooksPerPublisher(Analysis):
    def performAnalysis(self):
          #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
           #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Books Per Publisher")
        publisher_counts = data['book publisher'].value_counts().head(10)
        print(publisher_counts)
        publisher_counts.plot(kind='bar', title='Top 10 Publishers')
        plt.ylabel('Number of Books')
        plt.show()


class MissingISBNAnalysis(Analysis):
    def performAnalysis(self):
          #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
           #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Missing ISBN Analysis")
        total = len(data)
        missing_isbn = data['ISBN'].isnull().sum()
        percent_missing = (missing_isbn / total) * 100
        print(f"Missing ISBN count: {missing_isbn}")
        print(f"Missing ISBN percentage: {percent_missing:}%")


class BooksPerYearByLanguage(Analysis):
    def performAnalysis(self):
          #load csv
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
           #column name
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Books Published Per Year by Language")
        year_lang = data.groupby(['publication date', 'language']).size().unstack().fillna(0)
        print(year_lang.tail())
        year_lang.plot(kind='bar', stacked=True, figsize=(12, 6), title='Books Per Year by Language')
        plt.xlabel('Year')
        plt.ylabel('Number of Books')
        plt.legend(title='Language')
        plt.tight_layout()
        plt.show()



#main method
analysis = PublicationTrendsOverTime()
analysis.performAnalysis()

analysis = Top5Authors()
analysis.performAnalysis()

analysis = LanguageDistribution()
analysis.performAnalysis()

analysis = BooksPerPublisher()
analysis.performAnalysis()

analysis = MissingISBNAnalysis()
analysis.performAnalysis()

analysis = BooksPerYearByLanguage()
analysis.performAnalysis() 
