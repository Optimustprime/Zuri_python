# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,'r') as k:
        lines=k.read()
    return lines
    # print(filename)
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # counts=dict()
    per_word=text.split()

    counts=dict(enumerate(per_word,start=1))
    counts={v:k for k, v in counts.items()}
    unique=set(per_word)

    # for word in unique:
    #     if word not in counts:
    #         counts[word]=1
    #     else:
    #         counts[word]+=1
    return counts
print(count_words())