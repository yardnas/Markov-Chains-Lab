"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # open and read entire file
    new_file = open(file_path).read()
    # close the file
    #new_file.close()

    return new_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    #use string.split() to separate by white space
    words = text_string.split()
    #loop over each piece(word) comparing pairs of words next to each other

    #loop by index to create tuples and list values
    for idx in range(len(words) - 2):
        #create key as tuple
        key = (words[idx], words[idx + 1]) #CHECK AGAIN - doesn't include last I am
        #create value as list
        value = words[idx + 2]
    
        # handle condition where key is not in chains
        if key not in chains:
            chains[key] = []

        #append key/value to dictionary chains
        chains[key].append(value)
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
