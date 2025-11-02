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
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice < 1 or choice > 7:
                print("Invalid choice")
                continue

            elif ("choice == 1"):
                analysis = PublicationTrendsOverTime()
                analysis.performAnalysis()

            elif ("choice == 2"):
                analysis = Top5Authors()
                analysis.performAnalysis()

            elif ("choice == 3"):
                analysis = LanguageDistribution()
                analysis.performAnalysis()

            elif ("choice == 4"):
                analysis = BooksPerPublisher()
                analysis.performAnalysis()

            elif ("choice == 5"):
                analysis = MissingISBNAnalysis()
                analysis.performAnalysis()

            elif ("choice == 6"):
                analysis = BooksPerYearByLanguage()
                analysis.performAnalysis()

            elif ("choice == 7"):
                print("****Exit from dream book shop****...")
                break

            else:
                print("********** END *********.")

# main
if __name__ == "__main__":
    selector = strategyselector()
    selector.run()
