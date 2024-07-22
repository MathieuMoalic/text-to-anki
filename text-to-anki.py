import genanki
import re

def chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


# Define a function to read the words from the text file
def read_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    words = []
    for a,b,c in chunks(lines, 3):
        pl = a.strip().replace('\n', '').replace('\r', '')
        en = c.strip().replace('\n', '').replace('\r', '')
        words.append((pl,en))
            
    return words

# Define the words from your text file
words = read_words('words.txt')

# Define a model for the Anki cards
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Polish'},
        {'name': 'English'}
    ],
    templates=[
        {
            'name': 'Polish to English',
            'qfmt': '{{Polish}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{English}}'
        },
        {
            'name': 'English to Polish',
            'qfmt': '{{English}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Polish}}'
        }
    ]
)

# Create a new deck
my_deck = genanki.Deck(
    2059400110,
    'Polish Vocabulary'
)

# Add words to the deck
for pl_word, en_word in words:
    note = genanki.Note(
        model=my_model,
        fields=[pl_word, en_word]
    )
    my_deck.add_note(note)

# Save the deck to a .apkg file
genanki.Package(my_deck).write_to_file('polish_vocabulary.apkg')

print("Anki deck created successfully.")

