
# Quiz App

A simple interactive quiz application built using Python and Tkinter. This app fetches quiz questions from an online API, presents them to the user, and provides feedback based on the user's answers. It keeps track of the score and displays it in real-time.

## Features
- Fetches quiz questions from the Open Trivia Database API.
- Presents true/false quiz questions.
- Provides feedback on the user's answer (Green for correct, Red for incorrect).
- Tracks and displays the user's score.
- Ends the quiz and displays a message when all questions have been answered.

## Technologies Used
- **Python**: The main programming language used.
- **Tkinter**: For creating the graphical user interface (GUI).
- **Requests**: To fetch quiz questions from the Open Trivia Database API.

## How to Run

### Requirements:
- Python 3.x
- `requests` library
- `tkinter` library (comes with Python)

### Steps to Run:
1. Install the required libraries (if not already installed) using the following command:
    ```bash
    pip install requests
    ```
2. Download or clone the project files.
3. Run the main script that starts the quiz:
    ```bash
    python main.py
    ```
4. Enjoy the quiz! The application will display a question and give you options to answer with True or False.

## Code Explanation

### 1. `Questions` Class:
- A class that represents a question, containing the question text and the correct answer.
- It is used to store the questions retrieved from the API.

### 2. `Quizbrain` Class:
- Manages the quiz logic.
- Tracks the user's score and the current question number.
- Provides methods to fetch the next question and check the user's answer.

### 3. `QuizInterface` Class:
- Manages the graphical user interface using Tkinter.
- Displays the current question, options (True/False), and the user's score.
- Updates the interface based on the user's answer and gives feedback (green for correct, red for incorrect).

### 4. `API Integration`:
- The app retrieves 10 true/false questions using the [Open Trivia Database API](https://opentdb.com/api_config.php).
- The questions are then used in the quiz.

## File Structure
- `main.py`: The main script to run the quiz app.
- `ui.py`: Contains the `QuizInterface` class (GUI logic).
- `data.py`: Contains the question data fetched from the API.
- `question_model.py`: Contains the `Questions` class to represent quiz questions.
- `quizbrain.py`: Contains the `Quizbrain` class to manage quiz logic.

## License
This project is open-source and available under the MIT License.

## Acknowledgements
- [Open Trivia Database API](https://opentdb.com) for providing free trivia questions.
- Python community for making Tkinter and other libraries available for easy use.
