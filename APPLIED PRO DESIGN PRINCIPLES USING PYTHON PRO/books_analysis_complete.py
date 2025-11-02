
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from pandas.testing import assert_frame_equal

# Abstract class
class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):
        pass

# Menu class
class strategyselector:
    def openmenu(self):
        print("Data analytics and visual representation of Dream Book Shop")    
        print("1 - Publication Trends Over Time")
        print("2 - Top 5 Most Prolific Authors")
        print("3 - Language Distribution")
        print("4 - Publisher Count")
        print("5 - Top Subjects by Book Count")
        print("6 - Books per Decade")
        print("0 - Exit")
        
    def run(self):
        while True:
            self.openmenu()
            choice = int(input("Enter your option: "))
            if choice == 1:
                analysis = PublicationTrendsOverTime()
            elif choice == 2:
                analysis = Top5Authors()
            elif choice == 3:
                analysis = BooksPerLanguage()
            elif choice == 4:
                analysis = BooksPerPublisher()
            elif choice == 5:
                analysis = TopSubjects()
            elif choice == 6:
                analysis = BooksPerDecade()
            elif choice == 0:
                break
            else:
                print("Invalid option")
                continue
            analysis.performAnalysis()

# Option 1
class PublicationTrendsOverTime(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        df['book publish date'] = pd.to_datetime(df['book publish date'], errors='coerce')
        df = df.dropna(subset=['book publish date'])
        df['Year'] = df['book publish date'].dt.year
        result = df['Year'].value_counts().sort_index()
        print(result)
        result.plot(kind='line', title='Publication Trends Over Time')
        plt.xlabel('Year')
        plt.ylabel('Number of Books')
        plt.grid(True)
        plt.show()

# Option 2
class Top5Authors(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        top_authors = df['book author'].value_counts().head(5)
        print(top_authors)
        top_authors.plot(kind='barh', title='Top 5 Authors with Most Books')
        plt.xlabel('Number of Books')
        plt.ylabel('Author')
        plt.show()
        actual_result = top_authors.reset_index()
        actual_result.columns = ['Author', 'Book Count']
        exp_results = pd.DataFrame({
            'Author': ['William Shakespeare', 'Charles Dickens', 'Mark Twain', 'Jane Austen', 'Jules Verne'],
            'Book Count': [53, 44, 41, 36, 33]
        })
        print("Expected Results:")
        print(exp_results)
        print("Actual Results:")
        print(actual_result)
        assert_frame_equal(actual_result, exp_results)

# Option 3
class BooksPerLanguage(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        language_counts = df['book language'].value_counts()
        print(language_counts)
        language_counts.plot(kind='pie', autopct='%1.1f%%', title='Books by Language')
        plt.ylabel('')
        plt.show()
        actual_result = language_counts.head(5).reset_index()
        actual_result.columns = ['Language', 'Book Count']
        exp_results = pd.DataFrame({
            'Language': ['eng', 'fre', 'ger', 'spa', 'ita'],
            'Book Count': [3934, 487, 268, 230, 133]
        })
        print("Expected Results:")
        print(exp_results)
        print("Actual Results:")
        print(actual_result)
        assert_frame_equal(actual_result, exp_results)

# Option 4
class BooksPerPublisher(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        actual_result = df['book publisher'].value_counts().head(40).reset_index()
        actual_result.columns = ['Publisher', 'Book Count']
        exp_results = pd.read_csv("publishers_expected.csv")
        print("Expected Results:")
        print(exp_results)
        print("Actual Results:")
        print(actual_result)
        assert_frame_equal(actual_result, exp_results)

# Option 5
class TopSubjects(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        top_subjects = df['book subject'].value_counts().head(5)
        print(top_subjects)
        top_subjects.plot(kind='bar', title='Top Subjects by Book Count')
        plt.xlabel('Subject')
        plt.ylabel('Number of Books')
        plt.show()
        actual_result = top_subjects.reset_index()
        actual_result.columns = ['Subject', 'Book Count']
        exp_results = pd.DataFrame({
            'Subject': ['English literature', 'World War, 1939-1945', 'Science fiction', 'American literature', 'Detective and mystery stories'],
            'Book Count': [455, 318, 294, 287, 204]
        })
        print("Expected Results:")
        print(exp_results)
        print("Actual Results:")
        print(actual_result)
        assert_frame_equal(actual_result, exp_results)

# Option 6
class BooksPerDecade(Analysis):
    def performAnalysis(self):
        df = pd.read_csv("Books.CSV.csv")
        df['book publish date'] = pd.to_datetime(df['book publish date'], errors='coerce')
        df = df.dropna(subset=['book publish date'])
        df['Decade'] = (df['book publish date'].dt.year // 10) * 10
        result = df['Decade'].value_counts().sort_index()
        print(result)
        result.plot(kind='bar', title='Books Published per Decade')
        plt.xlabel('Decade')
        plt.ylabel('Number of Books')
        plt.grid(True)
        plt.show()
        actual_result = result.reset_index()
        actual_result.columns = ['Decade', 'Book Count']
        exp_results = pd.DataFrame({
            'Decade': [1890, 1900, 1910, 1920, 1930],
            'Book Count': [11, 62, 85, 153, 182]
        })
        print("Expected Results:")
        print(exp_results)
        print("Actual Results:")
        print(actual_result)
        assert_frame_equal(actual_result, exp_results)

if __name__ == "__main__":
    selector = strategyselector()
    selector.run()
