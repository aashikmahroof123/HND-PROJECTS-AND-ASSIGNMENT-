class strategyselector:
    def openmenu(self):
        while (True):
        print("data analytics and visual representation of  Dream Book Shop")    
        print("1. Publication Trends Over Time")
        print("2. Top 5 Most Prolific Authors")
        print("3. Language Distribution")
        print("4. Publisher Count")
        print("5. Missing ISBN Analysis")
        print("6. Books Per Year by Language")
        print("q. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice (q to quit): ")

            if choice == '1':
                analysis = PublicationTrendsOverTime()
                analysis.performAnalysis()
            elif choice == '2':
                analysis = Top5Authors()
                analysis.performAnalysis()
            elif choice == '3':
                analysis = LanguageDistribution()
                analysis.performAnalysis()
            elif choice == '4':
                analysis = BooksPerPublisher()
                analysis.performAnalysis()
            elif choice == '5':
                analysis = MissingISBNAnalysis()
                analysis.performAnalysis()
            elif choice == '6':
                analysis = BooksPerYearByLanguage()
                analysis.performAnalysis()
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please select again.")
#main
     if __name__ == "__main__":           
    selector = strategyselector()
    selector.run()            
