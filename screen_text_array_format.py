import nltk
import sys

print "Screen Text Array Format... ",
sys.stdout.flush()

video_text_file = sys.argv[1]
file_type = ".txt"

#this will be used in the tokenizer; can get rid of common words like "to", "a", "for", etc
word_type_exclusion_list = ["IN", "TO", "DT", "CC"]

full_file_name = video_text_file + file_type
read_text_file_path = "screen_text/" + full_file_name

iteration_array = []
word_list_dict = {}
word_list_array = []
word_per_iteration_matrix = []

word_list_array_index = 0
current_iteration = 0

'''
Going through the text generated from the OCR, this makes a matrix that shows:
The amount of times a word was seen at x iteration

Example matrix would be:

//begin example
this,is,an,example
4,5,0,0
5,2,1,3
8,2,1,4
2,0,10,1
//end example

The first row shows all the words found

The second row shows that "this" was seen 4 times in the (first) screen shot, and "is" 5 times. 
  "an" and "example" was not seen at all

The third row shows that "this" was seen 5 times in the (second) screen shot, "is" 2 times, "an" 1 time, and 
   "example" 3 times.

'''
with open(read_text_file_path, "r") as read_file:
    for line in read_file:
        #tokenizes the current line
        token_string = nltk.word_tokenize(line)

        #if nothing on the line, can skip it
        if token_string == []:
            continue

        #checks for the key "zzzzzzzzzzziteration", to see what iteration it is on
        elif token_string[0] == "zzzzzzzzzzziteration":
            current_iteration = int(token_string[2].strip())
            iteration_array.append(current_iteration)

            #If first iteration, just append an empty list row for matrix, since nothing is known yet
            if current_iteration == 0:
                word_per_iteration_matrix.append([])
            #if not first iteration, then make a row of the size of the already established first iteration
            else:
                word_per_iteration_matrix.append([0]*len(word_per_iteration_matrix[0]))

        #looking at the actual string data
        else:
            #tags the words to tell what type of word it is; like proper noun, verb, etc
            tagged_string = nltk.pos_tag(token_string)

            #goes through each tagged word in the tokenized string
            for word_and_type_pair in tagged_string:
                #gets the word
                word = word_and_type_pair[0]
                #gets the word type
                word_type = word_and_type_pair[1]

                #if word is in the type of words we don't care about, can skip it (stuff like "to", "a", etc
                if word_type in word_type_exclusion_list:
                    continue
                #Shouldn't have to worry about 1 letter words, is it is either Junk or the letter I
                elif len(word) == 1:
                    continue
                #is a word we want to look at
                else:
                    #if word isn't in our dictionary class
                    if word not in word_list_dict:
                        #make the key based on where it is in the word list array (its index)
                        word_list_dict[word] = word_list_array_index
                        #put word into the word list array
                        word_list_array.append(word)
                        #increase index so that next word will have the correct key value
                        word_list_array_index += 1

                        #Since a new word is added, it goes back through all the iterations (rows) in the matrix
                        # so that is can add a new column for this word
                        for iteration in iteration_array:
                            word_per_iteration_matrix[int(iteration)].append(0)

                    #gets the index (column number) of the current word
                    word_index = word_list_dict[word]

                    #increases its count by one, to indicate how many times it was seen in this iteration
                    word_per_iteration_matrix[current_iteration][word_index] += 1


    matrix_path = "time_matrix/"
    matrix_file_name = matrix_path + video_text_file + "_matrix_data" + file_type

    matrix_file = open(matrix_file_name, "w")

    #first row of file is the word list; this is the column titles
    matrix_file.write(','.join(word_list_array))
    matrix_file.write("\n")

    #goes through the matrix made and writes it to a text file
    for row in word_per_iteration_matrix:
        row = map(str, row)
        matrix_file.write(','.join(row))
        matrix_file.write("\n")

    matrix_file.close()

print("complete!")
sys.stdout.flush()
