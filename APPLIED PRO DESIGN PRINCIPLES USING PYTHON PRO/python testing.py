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
            'publication date': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
            'book count': [8 ,61 ,8 ,51, 32 ,17, 28 ,47, 24 ,58, 128 ,65 ,77]
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
            'book count': [26,22 ,12 ,12 ,10 ]
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
        import pandas as pd
        from pandas.testing import assert_frame_equal

        # Load CSV
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Group by publisher
        actual_result = df['book publisher'].value_counts().reset_index()
        actual_result.columns = ['book publisher', 'book count']

        print("Actual Results")
        print(actual_result)

        # Expected data (example only)
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
        4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
        })
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
        print("\n")


class BooksPerLanguage(Analysis):
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
            'book count': [153, 150, 129, 93, 56, 23]
        })
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
        print("\n")


class BooksPeryear(Analysis):
    def performAnalysis(self):
        import pandas as pd
        from pandas.testing import assert_frame_equal

        # Load CSV
        df = pd.read_csv('C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv')

        # Rename columns
        df.columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']

        # Convert to decade
        df['decade'] = (df['publication date'] // 10) * 10

        # Group by decade
        actual_result = df['year'].value_counts().sort_index().reset_index()
        actual_result.columns = ['year', 'book count']

        print("Actual Results")
        print(actual_result)

        # Expected results (example)
        exp_results = pd.DataFrame({
    'year': [2019, 2020, 2021, 2022, 2023],
    'Chinese': [0.0, 14.0, 43.0, 23.0, 13.0],
    'English': [13.0, 9.0, 11.0, 11.0, 30.0],
    'French': [0.0, 0.0, 0.0, 0.0, 20.0],
    'German': [0.0, 0.0, 45.0, 27.0, 14.0],
    'Italian': [8.0, 27.0, 17.0, 4.0, 0.0],
    'Japanese': [3.0, 8.0, 12.0, 0.0, 0.0]

    
        })

        
        print("\n")
        print("Expected Results")
        print(exp_results)

        # Assertion
        assert_frame_equal(actual_result, exp_results)
        
        print("\n")
        print("Test Passed - Expected and Actual Frames are the same")
        print("\n")
