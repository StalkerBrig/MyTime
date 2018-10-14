import nltk
import sys

print "Video Text Array Format... ",
sys.stdout.flush()

video_text_file = sys.argv[1]
file_type = ".txt"

word_type_exclusion_list = ["IN", "TO", "DT", "CC"]

full_file_name = video_text_file + file_type

read_text_file_path = "video_text/" + full_file_name

seconds_array = []
word_list_dict = {}
word_list_array = []
word_per_second_matrix = []

word_list_array_index = 0
current_second = 0

with open(read_text_file_path, "r") as read_file:
    for line in read_file:
        token_string = nltk.word_tokenize(line)
        if token_string == []:
            continue
        elif token_string[0] == "zzzzzzzzzzzsecond":
            current_second = int(token_string[2].strip())
            seconds_array.append(current_second)
            if current_second == 0:
                word_per_second_matrix.append([])
            else:
                word_per_second_matrix.append([0]*len(word_per_second_matrix[0]))
        else:
            tagged_string = nltk.pos_tag(token_string)
            for word_and_type_pair in tagged_string:
                word = word_and_type_pair[0]
                word_type = word_and_type_pair[1]
                if word_type in word_type_exclusion_list:
                    continue
                elif len(word) == 1:
                    continue
                else:
                    if word not in word_list_dict:
                        word_list_dict[word] = word_list_array_index
                        word_list_array.append(word)
                        word_list_array_index += 1
                        for second in seconds_array:
                            word_per_second_matrix[int(second)].append(0)

                    word_index = word_list_dict[word]
                    word_per_second_matrix[current_second][word_index] += 1

    matrix_path = "time_matrix/"
    matrix_file_name = matrix_path + video_text_file + "_matrix_data" + file_type
    matrix_file = open(matrix_file_name, "w")

    matrix_file.write(','.join(word_list_array))
    matrix_file.write("\n")

    for row in word_per_second_matrix:
        row = map(str, row)
        matrix_file.write(','.join(row))
        matrix_file.write("\n")

    matrix_file.close()

print("complete!")
sys.stdout.flush()
