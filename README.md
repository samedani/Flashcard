# Flashcard App

A simple flashcard app built with Python's Tkinter library, designed to help users study Spanish vocabulary by flipping between Spanish and English translations. The app displays a flashcard with a word in Spanish, and after a few seconds, it flips to show the English translation. Users can mark words they know, and those words will be removed from the study list.

## Features
- Displays a Spanish word on the front of the card.
- Flips the card to show the English translation after a few seconds.
- Allows users to mark words they know and remove them from the list.
- Saves the remaining words in a CSV file for future study sessions.

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- pandas library (can be installed via `pip install pandas`)

## Setup
1. Clone or download the repository.
2. Make sure you have the following folder structure:

```
/your_project
│
├── data/
│   ├── spanish_words.csv        # Original list of Spanish words (if words_to_learn.csv does not exist)
│   └── words_to_learn.csv       # List of words to learn (after user marks known words)
│
├── images/
│   ├── card_back.png            # Back image of the flashcard
│   ├── card_front.png           # Front image of the flashcard
│   ├── right.png                # Image for the "right" button
│   └── wrong.png                # Image for the "wrong" button
│
├── main.py                      # Python script for the Flashcard app
└── README.md                    # This file
```

3. Ensure the CSV files and images are placed in their respective directories (`data/` and `images/`).

## How to Use
1. Run `main.py` to start the flashcard app.
2. The app will display a Spanish word on the front of the card.
3. After a few seconds, the card will flip to show the English translation.
4. You can mark the word as "known" by clicking the right button, which removes it from the study list.
5. Words the user doesn't know can be skipped by clicking the wrong button.
6. The words that remain in the study list are saved to `data/words_to_learn.csv` for the next study session.

## CSV File Structure
The CSV file (`words_to_learn.csv`) should have two columns:  
- **Spanish**: The Spanish word to learn.
- **English**: The English translation.

Example:

| Spanish   | English   |
|-----------|-----------|
| Hola      | Hello     |
| Comida    | Food      |
| Libro     | Book      |

If `words_to_learn.csv` doesn't exist, the app will use `spanish_words.csv` as the default source.

## License
This project is open-source and available under the MIT License.
