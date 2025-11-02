import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from pandas.testing import assert_frame_equal

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

class PublicationTrendsOverTime(Analysis):
    def performAnalysis(self):
        # Import necessary libraries
        import pandas as pd #IGNORE TYPE
        import matplotlib.pyplot as plt
        from pandas.testing import assert_frame_equal

        # Load the dataset
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns to readable format
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Group by publication year and count number of books per year
        actual_result = df['publication date'].value_counts().sort_index().reset_index()
        actual_result.columns = ['publication date', 'book count']

        print("Actual Results")
        print(actual_result) # print summary

        # Manually prepare expected data for testing (example years and counts)
        exp_results = pd.DataFrame({
            'publication date': [2011, 2012, 2016, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
            'book count': [8 ,1 ,6 ,77, 32 ,7, 28 ,47, 24 ,5, 18 ,65 ,77]
        })

        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion to test actual vs expected
        assert_frame_equal(actual_result, exp_results)

        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
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
        
class Top5Authors(Analysis):
    def performAnalysis(self):
        import pandas as pd # ignore type
        from pandas.testing import assert_frame_equal

        # Load CSV file
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Calculate top 5 authors by book count
        actual_result = df['author'].value_counts().head(5).reset_index()
        actual_result.columns = ['author', 'book count']

        print("Actual Results")
        print(actual_result)#print summary

        # Expected results (example, update values as needed)
        exp_results = pd.DataFrame({
            'author': ['Zuri Day', 'Valerie Jackson', 'Jenni Fagan', 'Jeffrey Haynes', 'Matt Jones'],
            'book count': [6,227 ,12 ,128 ,10 ]
        })
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
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

class LanguageDistribution(Analysis):
    def performAnalysis(self):
        import pandas as pd
        from pandas.testing import assert_frame_equal

        # Load CSV
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Count by language
        actual_result = df['language'].value_counts().reset_index()
        actual_result.columns = ['language', 'book count']

        print("Actual Results")
        print(actual_result)

        # Expected results (example)
        exp_results = pd.DataFrame({
            'language': ['English',  'German' ,'French', 'Chinese', 'Italian' , 'Japanese'],
            'book count': [13, 150, 19, 93, 56, 123]
        })
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
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

class BooksPerPublisher(Analysis):
    def performAnalysis(self):
        import pandas as pd
        from pandas.testing import assert_frame_equal

        # Load CSV
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Group by publisher
        actual_result = df['book publisher'].value_counts().head(40).reset_index()
        actual_result.columns = ['book publisher', 'book count']
        print("Actual Results")
        print(actual_result)

        # Expected data 
        exp_results = pd.DataFrame({
            'book publisher': ['Routledge', 'Elsevier/Masson', 'SpringerGabler', 'Peter Lang',
        'Chartered Insurance Institute', 'Mills&Boon', ': Springer', 'Wiley-VCH',
        'Dafina', 'Luyi Publishing', 'Cambridge University Press', 'ISTE Editions',
        'ISTE Editions Ltd', 'Kimani', 'DeGruyter', 'The Chartered Insurance Institute',
        'Hatje Cantz', 'North-Holland Biomedical Press', 'Better Link Press',
        'Austin Macauley Publishers', 'Wiley', 'BAR Publishing', 'Mc Graw-Hill',
        'Amberley Publishing', 'Morning Star', 'ACC Art Books',
        'Grosvenor House Publishing Limited', 'AcademicaPress', 'Oxford University Press',
        'Cambridge Text Education', 'Collins', 'SilvanaEditoriale', 'Brill',
        'BBC Active', 'Wiley-VCH Verlag GmbH&Co KGaA', 'P Lang',
        'The Crowood Press', 'Berlitz', 'Gower', 'Packt Publishing' ],
            'book count': [ 61, 41, 18, 16, 15, 14, 13, 12, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4,
        4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3 ]
        })
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
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

 

class BooksPeryearByLanguage(Analysis):
    def performAnalysis(self):
        import pandas as pd
        from pandas.testing import assert_frame_equal

        # Load CSV
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Group by year and language
        (exp_results) = df.groupby(['publication year', 'language']).size().unstack().fillna(0)

        # Filter last 5 years for comparison
        actual_result = [[2019, 2020, 2021, 2022, 2023]]
        print("Actual Books Published Per Year by Language:")
        print(actual_result)

        # Expected results 
        exp_results = pd.DataFrame({
            'Chinese': [0.0, 14.0, 43.0, 23.0, 13.0],
            'English': [13.0, 9.0, 11.0, 11.0, 30.0],
            'French': [0.0, 0.0, 0.0, 0.0, 20.0],
            'German': [0.0, 0.0, 45.0, 27.0, 14.0],
            'Italian': [8.0, 27.0, 17.0, 4.0, 0.0],
            'Japanese': [3.0, 8.0, 12.0, 0.0, 0.0]})
        PublicationYear=[2019, 2020, 2021, 2022, 2023]
        print("Expected results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("Test Passed - Expected and Actual Frames are the same.")

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


# Main method

      
if __name__ == "__main__":          
    selector = strategyselector()
    selector.run()


     





