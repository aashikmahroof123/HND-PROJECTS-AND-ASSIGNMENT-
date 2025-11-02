class top5authors(Analysis):
    def performAnalysis(self):
        # Load CSV file
        data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV.csv")

        # Set column names
        columns = ['book', 'author', 'publication date', 'language', 'book publisher', 'ISBN', 'BNB id']
        data.columns = columns

        # Top 5 Most Prolific Authors
        print("Top 5 Authors by Number of Books")
        author_counts = data['author'].value_counts().head(5)
        print(author_counts)

        # Plot
        author_counts.plot(kind='bar', title='Top 5 Authors')
        plt.ylabel('Books Written')
        plt.tight_layout()
        plt.show()
