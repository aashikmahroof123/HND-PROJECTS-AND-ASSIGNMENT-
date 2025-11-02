import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):
        pass

class strategyselector:
    def openmenu(self):
        print("Data analytics and visual representation of Dream Book Shop")    
        print("1 - Publication Trends Over Time")
        print("2 - Top 5 Most Prolific Authors")
        print("3 - Language Distribution")
        print("4 - Publisher Count")
        print("5 - Missing ISBN Analysis")
        print("6 - Books Per Year by Language")
        print("7 - Exit")

    def run(self):
        while True:
            self.openmenu()
            try:
                choice = int(input("Enter choice [1|2|3|4|5|6|7]: "))

                if choice == 1:
                    analysis = PublicationTrendsOverTime()
                    analysis.performAnalysis()

                elif choice == 2:
                    analysis = Top5Authors()
                    analysis.performAnalysis()

                elif choice == 3:
                    analysis = LanguageDistribution()
                    analysis.performAnalysis()

                elif choice == 4:
                    analysis = BooksPerPublisher()
                    analysis.performAnalysis()

                elif choice == 5:
                    analysis = MissingISBNAnalysis()
                    analysis.performAnalysis()

                elif choice == 6:
                    analysis = BooksPerYearByLanguage()
                    analysis.performAnalysis()

                elif choice == 7:
                    print("****Exit from dream book shop****...")
                    break

                else:
                    print("********** END *********.")

            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")

#ADMIN CLASS
class Admin:
    count=0
    def __init__ (self,username,password):
        if (Admin.count==0):
            self.username = username
            self.password = password
            Admin.count = Admin.count + 1
        else :
            print ("Admin already exists")

    def logon(self):
       print("Data analytics and visual representation of Dream Book Shop")
       print("------***--------------***************---------------***-----------")
       un = input ("Enter the User Name :")
       pw = input ("Enter the Password :")
       if (un == self.username and pw == self.password):
          selector = strategyselector()
          selector.run() 
       else:
           print("Incorrect User Name OR Password")


class PublicationTrendsOverTime(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
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
        print("\n")


class Top5Authors(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Top 5 Authors by Number of Books")
        author_counts = data['author'].value_counts().head(5)
        print(author_counts)
        author_counts.plot(kind='bar')
        plt.title("Top 5 Authors")
        plt.xlabel("Name")
        plt.ylabel('Books Written')
        plt.show()
        print("\n")


class LanguageDistribution(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Language Distribution")
        language_counts = data['language'].value_counts()
        print(language_counts)
        language_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Languages of Books')
        plt.show()
        print("\n")


class BooksPerPublisher(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Books Per Publisher")
        publisher_counts = data['book publisher'].value_counts().head(40)
        print(publisher_counts)
        publisher_counts.plot(kind='bar', width=0.2)
        plt.xlabel('Name')
        plt.title('Publishers')
        plt.ylabel('Number of Books')
        plt.show()
        print("\n")


class MissingISBNAnalysis(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Missing ISBN Analysis")
        total = len(data)
        missing_isbn = data['ISBN'].isnull().sum()
        percent_missing = (missing_isbn / total) * 100
        print(f"Missing ISBN count: {missing_isbn}")
        print(f"Missing ISBN percentage: {percent_missing:.2f}%")
        print("\n")


class BooksPerYearByLanguage(Analysis):
    def performAnalysis(self):
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        print("Books Published Per Year by Language")
        year_lang = data.groupby(['publication date', 'language']).size().unstack().fillna(0)
        print(year_lang.tail())
        year_lang.plot(kind='bar', figsize=(12, 6), title='Books Per Year by Language')
        plt.xlabel('Year')
        plt.ylabel('Number of Books')
        plt.legend
        plt.title('Language')
        plt.show()
        print("\n")


# Main method
a1 = Admin("MOHAMMED AASHIK","1234567")
a1.logon()
      
if __name__ == "__main__":          
    selector = strategyselector()
    selector.run()


     



