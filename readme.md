## Introduction
Welcome to the Word Guessing Game, a console-based game where you need to guess words associated with shuffled letters within a time limit. This game challenges your vocabulary and quick thinking skills. 

## Getting Started

### Prerequisites
Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ybakyurek/BBM103-AS3-wordguessing.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BBM103-AS3-wordguessing

    ```

### Running the Game
1. Open your terminal and navigate to the project directory.

2. Run the following command to start the game:

    ```bash
    python wordguessing.py correct_words.txt letter_points.txt
    ```

    Note: Replace `words.txt` and `letter_points.txt` with the actual names of your word list and letter points files.

## Game Rules

1. The game presents you with shuffled letters.
2. You have 30 seconds to guess words associated with the given letters.
3. Each correctly guessed word earns you points based on the value of its letters.
4. You cannot guess the same word multiple times.
5. The game ends when the time runs out.

## Example Gameplay

```plaintext
Shuffled letters are: HSTAAME
Please guess words for these letters with a minimum of three letters
Guessed word: hasta
You have 28 seconds left
Guessed word: temas
You have 0 seconds left
You have run out of time
Score for HSTAAME is 40 and guessed words are: hasta
```

## Enjoy the Game!

Have fun playing the Word Guessing Game! Test your word knowledge and try to achieve the highest score within the time limit. If you encounter any issues or have suggestions for improvement, feel free to contribute or provide feedback. Happy gaming!
