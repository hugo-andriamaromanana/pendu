input_letter='a'
word_to_guess=list('anaconda')
word_to_guess_display = list('_'*len(word_to_guess))

def get_all_index_to_replace():
    global word_to_guess
    if input_letter in word_to_guess:
        count=0
        index_arr=[]
        for i in word_to_guess:
            if i == input_letter:
                index_arr.append(count)
            count+=1
        return index_arr

def display_matching_letters():
    global word_to_guess_display
    global input_letter
    for i in get_all_index_to_replace():
        word_to_guess_display[i]=input_letter
    input_letter=''

display_matching_letters()
print(' '.join(word_to_guess_display))