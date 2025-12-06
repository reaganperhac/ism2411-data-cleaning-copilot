#Reflection

## What Copilot created

In this project, I used GitHub Copilot to assist me with the two functions `load_data` and `clean_column_names`. To get the suggestions to pop up, I started each function with a comment explaining what the function should do, and then Copoliot created a response for loading the data and cleaning the column names. One of the things it did was replace spaces with underscores. The suggestions it gave helped me work more efficiently and build a stronger structure to my code.

## What I Modified

During this assignment, Copilot made the initial drafts, but I made modifications to work with the actual dataset and to prevent errors. For `load_data`, I added a `try/except` block and replaced the default behavior with a safer fallback return of an empty DataFrame instead of `None`. This prevented other functions from crashing if the file path was wrong. For `clean_column_names`, I made Copilot’s suggestion bigger by adding more checks, including replacing dashes with underscores and making sure all column names were lowercase.

Besides those two functions, I also wrote another cleaning step myself, which was `standardize_core_columns`. Its job was converting text to numeric values with `pd.to_numeric`, removing negative values, and dealing with missing values. These changes were necessary because the real dataset had problems that Copilot's suggestions could not help fix. Making these changes helped me make sure the script could run fully without errors.

## What I Learned

Through this assignment, I learned how to design a complete data cleaning pipeline in Python and how to structure a project in a professional way. I also learned that Copilot is the most helpful when I give it clear comments, function descriptions, or halfway written code. However, I also saw that the Copilot’s suggestions are not always correct. For example, its first try did not deal with missing values, negative numbers, or inconsistent column names in a great way. I had to think critically, fix the logic, and adjust the code to match the dataset and assignment requirements.

Overall, this project helped me to better understand the strengths and limits of AI coding tools. Copilot really can help with the early stages of writing code, but our human fixes are still needed to test, debug, and finish the script. This project made me more confident in both my data cleaning skills and my ability to use AI tools responsibly.
