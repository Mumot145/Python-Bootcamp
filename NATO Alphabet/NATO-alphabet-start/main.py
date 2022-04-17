import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dataframe = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input = input("Provide a word: ").upper()
# input is a string provided by input
# for letter is splitting the input into letter by letter from the input string
# nato_dict[letter] is creating an array of the dictionary values that exist in the input letter array
output_list = [nato_dict[letter] for letter in input]
print(output_list)
