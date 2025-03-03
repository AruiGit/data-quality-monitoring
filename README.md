User Data Validation and Correction

This project is designed to validate, correct, and store user data in a database. It uses Python libraries such as Faker, Pandas, and Matplotlib, along with SQL for database operations. Additionally, it generates reports that visualize data errors and stores users with invalid data in CSV files for further analysis.
Features

    Data Generation: Generates fake user data using the Faker library.
    Data Validation: Validates the generated data for issues like:
        Duplicates
        Typos in email addresses WIP
        Missing values
        Invalid phone number formats WIP
    Data Correction: Corrects certain types of errors, such as fixing typos or filling missing values.
    Database Integration: Stores the validated and corrected user data in a database.
    Reporting: Generates and saves CSV files containing users with errors, allowing for further review and analysis.
    Visualization: Uses Matplotlib to create visual reports that highlight errors and data quality issues, helping to monitor data integrity.
    BPMN Models: The project follows BPMN (Business Process Model and Notation) models to ensure efficient and correct data flow throughout the process.
