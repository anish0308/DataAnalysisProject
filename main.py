#These are the import statements
import datetime #to generate a unique timestamp while saving the file
import  pandas as pd #pandas df to manipulate and operate on the dataset csv file
import matplotlib.pyplot as plt #for plotting operations



#main class for Data objects
class myData:
    def __init__(self):             #constructor to initialize the object for the class myData
        print("Data object created")
        self.paths=[] #empty list to append file path
        self.names=[] #empty list to append file names
        self.data=[]  #list to append the data
        self.report=[] #creating an empty list to generate report log. Will append to this after each operation performed by the user
        self.report.append("Dataset Log Report\n")
        self.report.append("=" * 50 + "\n")

    def load_data(self,paths,names):
        """
           Method to load the dataset

            Args:
                paths:File path for the dataset
                names:Name assigned to the dataset by the user

            Output:
                Loads the datasets into the list data

            """
        for i in range(len(paths)):
            try:
                self.data.append(pd.read_csv(paths[i]))
                self.report.append(f"Loaded dataset from path: {paths[i]}\n")
                self.paths.append(paths[i])
                self.names.append(names[i])
                print("New Datasets added to the object!\n")
            except Exception as e:
                print("No such Dataset found!\n")
    def check_name(self,name):
        """
                   Method to check if the dataset provided by the user is present in the list name

                    Args:
                        name: input provided by the user

                    Returns:
                        j=-1 if dataset not found in name
                        else j=index of the dataset in name
                    """
        j = -1
        for i in range(len(self.names)):
            if name == self.names[i]:
                j = i
                break
        return j

    def list_data(self):
        """
                           Method to display number of rows and columns in the dataset

                            Args:
                                None

                            Output:
                                Number of Rows and Columns are displayed for the dataset
                            """
        for i in range(len(self.names)):
            print(i+1,"]",self.names[i])
            print("Rows:",self.data[i].shape[0])
            print("Columns:", self.data[i].shape[1])
            self.report.append(f"{i + 1}. {self.names[i]}\n")
            self.report.append(f"Rows: {self.data[i].shape[0]}\n")
            self.report.append(f"Columns: {self.data[i].shape[1]}\n")
        print("\n")

    def view_data(self,name):
        """
                                   Method to view the first 5 elements in the dataset(head)

                                    Args:
                                        name: input provided by the user(dataset name)

                                    Output:
                                        Returns first 5 rows of Dataset
                                    """
        j=self.check_name(name)  #check if present in the

        if j!=-1:
            print(self.data[j].head(5))
            self.report.append(f"First 5 rows of {name} dataset:\n{self.data[j].head(5).to_string()}\n")
        else:
            print("No such dataset found\n")
            self.report.append("No such dataset found\n")

    def analyse_data(self,index,func_number):
        """
                                           Method to display Statistics and data of missing values

                                            Args:
                                                index: index of the dataset in the list name
                                                func_number: to make choice between Summary and Missing Data Report

                                            Output:
                                                Summary of Mean,Median and Std Deviation of the Dataset
                                                Number of missing values in the dataset
                                            """
        if func_number == 1:
            print("Summary statistics\n")
            self.report.append("Summary statistics\n")
            print("Mean:\n",self.data[index].mean(numeric_only=True))
            self.report.append(f"Mean:\n{self.data[index].mean(numeric_only=True)}\n")
            print("\nMedian\n",self.data[index].median(numeric_only=True))
            self.report.append(f"Median:\n{self.data[index].median(numeric_only=True)}\n")
            print("\nStandard Deviation\n",self.data[index].std(numeric_only=True))
            self.report.append(f"Standard Deviation:\n{self.data[index].std(numeric_only=True)}\n")

        elif func_number == 2:
            print("Missing Data Report\n")
            self.report.append("Missing Data Report\n")
            print("Total number of missing data across the Dataset is:",self.data[index].isnull().sum().sum())
            self.report.append(f"Total number of missing data across the Dataset is: {self.data[index].isnull().sum().sum()}\n")


        else:
            print("No such function exists!\n")
            self.report.append("No such function exists!\n")

    def visualize_data(self, index, func_number):
        """
                                                   Method to plot histogram and box plots for specific columns in the dataset

                                                    Args:
                                                        index: index of the dataset in the list name
                                                        func_number: to make choice between Histogram and Box Plot

                                                    Output:
                                                        Histogram for the column asked by the user in .png format
                                                        Box Plot for the column asked by the user in .png format
                                                    """
        df = self.data[index]  # access the DataFrame
        print(f"\nAvailable columns in dataset: {df.columns.tolist()}")
        self.report.append(f"Available columns in dataset: {df.columns.tolist()}\n")
        print("\nColumn Data Types:\n", df.dtypes)
        self.report.append(f"Column Data Types:\n{df.dtypes}\n")

        if func_number == 1:
            col_name = input("\nEnter column name for the histogram: ").strip()
            self.report.append(f"User input for histogram column: {col_name}\n")
            if col_name in df.columns:
                if pd.api.types.is_numeric_dtype(df[col_name]):
                    plt.hist(df[col_name].dropna(), bins=20, edgecolor='black')
                    plt.title(f'Histogram of {col_name}')
                    plt.xlabel(col_name)
                    plt.ylabel('Frequency')
                    plt.grid(True)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"Plots/{self.names[j]}_{col_name}_{timestamp}.png"
                    plt.savefig(filename)
                    print(f"Histogram for_{col_name} generated and saved as_{filename}\n")
                    self.report.append(f"Histogram for_{col_name} generated and saved as_{filename}\n")
                    plt.show()
                else:
                    print(f"The column '{col_name}' is not numeric and cannot be plotted as a histogram.")
                    self.report.append(f"The column '{col_name}' is not numeric and cannot be plotted as a histogram.\n")
            else:
                print(f"Column '{col_name}' not found in the dataset.")
                self.report.append(f"Column '{col_name}' not found in the dataset.\n")

        elif func_number == 2:
            col_name = input("\nEnter column name for the Box plot: ").strip()
            self.report.append(f"\nEnter column name for the Box plot:_{col_name}\n ")
            if col_name in df.columns:
                if pd.api.types.is_numeric_dtype(df[col_name]):
                    plt.boxplot(df[col_name].dropna())
                    plt.title(f'Box Plot of {col_name}')
                    plt.ylabel(col_name)
                    plt.grid(True)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"Plots/{self.names[j]}_{col_name}_{timestamp}.png"
                    plt.savefig(filename)
                    print(f"Box Plot for_{col_name} generated and saved as_{filename}\n")
                    self.report.append(f"Box Plot for_{col_name} generated and saved as_{filename}\n")
                    plt.show()
                else:
                    print(f"The column '{col_name}' is not numeric and cannot be plotted as a box plot.")
                    self.report.append(f"The column '{col_name}' is not numeric and cannot be plotted as a box plot.")
            else:
                print(f"Column '{col_name}' not found in the dataset.")
                self.report.append(f"Column '{col_name}' not found in the dataset.","\n")

    def clean_data(self,index,func_number):
        """
                                                           Method to clean data of duplicates and missing data

                                                            Args:
                                                                index: index of the dataset in the list name
                                                                func_number: to make choice between Removing Duplicates and to handle missing data

                                                            Output:
                                                                Remove duplicate rows
                                                                Handle missing Data(drop,replace with mean, replace with mode)
                                                            """
        df = self.data[index]
        if func_number == 1:
            duplicates = df[df.duplicated()]
            print("Duplicate rows:\n", duplicates)
            self.report.append(f"Duplicate rows:\n{duplicates.to_string()}\n")
            df.drop_duplicates()
            print("\nAfter removing duplicates:\n", df)
            self.report.append(f"After removing duplicates:\n{df.to_string()}\n")

        elif func_number == 2:
            print("Missing Data Handling operations:\n")
            self.report.append("Missing Data Handling operations:\n")
            print("1. Remove rows with missing values\n")
            self.report.append("1. Remove rows with missing values\n")
            print("2. Fill missing values with mean (numerical columns)\n")
            self.report.append("2. Fill missing values with mean (numerical columns)\n")
            print("3. Fill missing values with mode (categorical columns)\n")
            self.report.append("3. Fill missing values with mode (categorical columns)\n")
            missing_choice = int(input("Enter your choice (1-3): ").strip())
            self.report.append(f"Enter your choice (1-3):_{missing_choice}")
            if missing_choice == 1:
                df.dropna(inplace=True)
                print("\n After removing missing values:\n", df)
                self.report.append(f"After removing missing values:\n{df.to_string()}\n")
                print("Updated Rows:", df.shape[0])

            elif missing_choice == 2:
                df.fillna(df.mean(numeric_only=True),inplace=True)
                print("\n After replacing missing values with mean:\n", df)
                self.report.append(f"After filling missing values with mean:\n{df.to_string()}\n")
                print("Updated Rows:", df.shape[0])

            elif missing_choice == 3:
                for col in df.columns:
                    if df[col].dtype == 'object':
                        mode_val = df[col].mode()
                        if not mode_val.empty:
                            df[col].fillna(mode_val[0],inplace=True)

                print("\nAfter filling categorical NaNs with mode:\n", df)
                self.report.append(f"After filling categorical NaNs with mode:\n{df.to_string()}\n")
                print("Updated Rows:", df.shape[0])


            else:
                print("\nInvalid choice just enter numbers between ranges 1-3")
                self.report.append("\nInvalid choice just enter numbers between ranges 1-3\n")

    def generate_report(self,index):
        """
                                                                   Method to generate a log of the data to the users based on the actions done on the command line

                                                                    Args:
                                                                        index: index of the dataset in the list name


                                                                    Output:
                                                                        Generate a .txt with log of actions and data presented to the user
                                                                    """
        dataset_name = self.names[index]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Reports/{dataset_name}_Report_{timestamp}.txt"
        try:
            with open(filename, "w") as f:
                f.writelines([str(line) if isinstance(line, str) else str(line) + "\n" for line in self.report])
            print(f"Report saved successfully as '{filename}'")
        except Exception as e:
            print("Failed to save report:", e)













print("Welcome to Python Data Analysis Assistant!")
#flags
stop=0
load_data=0

while stop==0:
    command=input("Available commands:  \n- load [file_path] [dataset_name]: Load a dataset from a CSV file.\n- list: List all loaded datasets.\n- view [dataset_name]: View the first few rows of a dataset.\n- analyze [dataset_name]: Perform data analysis on a dataset.\n- visualize [dataset_name]: Generate visualizations for a dataset.\n- clean [dataset_name]: Perform data cleaning operations.\n- report [dataset_name]: Generate a report for a dataset.\n- help: Show this help message.\n- exit: Exit the program.\n")

    global obj #to make a global scope for obj

    if command=="exit":
        print("Thank you for using the Python Data Analysis Assistant. Goodbye!")
        if 'obj' in globals(): #check in place to see if obj is in the globals dictionary
            obj.report.append("Thank you for using the Python Data Analysis Assistant. Goodbye!\n")
        stop=1
    elif command=="help":
        if 'obj' in globals():
            obj.report.append("User asked for help.\n")
        pass
    elif command.split(" ")[0]=="load":
        paths_inp=[]
        names_inp=[]

        for i in range(1,len(command.split(" "))):
            if i%2==0: #in even places we have the name assigned
                names_inp.append(command.split(" ")[i])
            else:# else it's odd which contains the dataset path
                paths_inp.append(command.split(" ")[i])

        if load_data==0:
            obj= myData()

        obj.load_data(paths_inp,names_inp)
        load_data=1 #set to 1 after load_data() has been called
        obj.report.append("User loaded datasets.\n")
    elif command=="list":
        if load_data!=0: #if loaded
            obj.list_data()
            obj.report.append("User listed all datasets.\n")
        else:
            print("Please load a dataset first!")
    elif command.split(" ")[0]=="view":
        if load_data!=0:
            dataset_name = command.split(" ")[1]
            obj.view_data(command.split(" ")[1])
            obj.report.append(f"User viewed dataset: {dataset_name}\n")
        else:
            print("Please load a dataset first!")
    elif command.split(" ")[0]=="analyze":
        if load_data!=0:
            dataset_name = command.split(" ")[1]
            j = obj.check_name(command.split(" ")[1])

            if j!=-1:
                var = int(input("Select analysis type:\n1. Summary statistics\n2. Missing data report\nEnter your choice(1-2):\n"))
                obj.report.append(f"User selected analysis type {var} for {dataset_name}\n")
                obj.analyse_data(j, var)
            else:
                print("No such dataset found!")
        else:
                print("Please load a dataset first!")
    elif command.split(" ")[0]=="visualize":
        if load_data!=0:
            j = obj.check_name(command.split(" ")[1])

            if j!=-1:
                var = int(input("Select plot type:\n1. Histogram\n2. Box Plot\nEnter your choice(1-2):\n"))
                obj.visualize_data(j, var)
            else:
                print("No such dataset found!")
        else:
                print("Please load a dataset first!")
    elif command.split(" ")[0]=="clean":
        if load_data!=0:
            j = obj.check_name(command.split(" ")[1])

            if j!=-1:
                var = int(input("Select the cleaning operation:\n1.Remove duplicates\n2. Handle missing values\nEnter your choice (1-2): "))
                obj.clean_data(j, var)
            else:
                print("No such dataset found!")
        else:
                print("Please load a dataset first!")

    elif command.split(" ")[0]=="report":

        if load_data!=0:
            j = obj.check_name(command.split(" ")[1])
            dataset_name = command.split(" ")[1]
            if j!=-1:
                obj.generate_report(j)
                obj.report.append(f"User requested report generation for {dataset_name}\n")
            else:
                print("No such dataset found!")
        else:
                print("Please load a dataset first!")





