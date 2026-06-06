# Snake Water Gun Game

A command-line game built in Python as my first project. It works like Rock Paper Scissors but with Snake, Water, and Gun instead.

I'm a second-year B.Tech student (AI & ML) and this is where my GitHub journey starts.

---

## About the Project

I built this after learning Python basics — if/else, functions, dictionaries, and loops. Wanted to build something I could actually run and play, not just a practice exercise that sits in a folder.

The code is simple and readable. No libraries, no installation, just Python.

---

## Game Rules

- Snake beats Water (snake drinks water)
- Water beats Gun (water damages gun)
- Gun beats Snake (gun kills snake)

---

## Features

- Play against the computer
- Input validation — handles wrong input without crashing
- Shows both choices after each round
- Play as many rounds as you want in one session

---

## How to Run

Make sure Python 3 is installed:

```bash
python --version
```

Clone the repository:

```bash
git clone https://github.com/Kashish7714/snake-water-gun-game-python.git
cd snake-water-gun-game-python
```

Run the game:

```bash
python snake_water_gun.py
```

---

## Sample Output

```
Welcome to Snake Water Gun!

--- Snake Water Gun ---
Rules: Snake beats Water | Water beats Gun | Gun beats Snake

Enter your choice (s = Snake, w = Water, g = Gun): s

You chose:      Snake
Computer chose: Water

You Win!

Play again? (y/n): n

Thanks for playing! Goodbye
```

---

## Project Structure

```
snake-water-gun-game-python/
├── snake_water_gun.py
├── README.md
├── .gitignore
└── LICENSE
```

---

## What I Want to Add Next

- Score tracker across rounds
- Best of 3 or best of 5 mode
- Save scores to a file
- Simple GUI using Tkinter

---

## Technologies Used

- Python 3
- random module (built-in)

---

## Author

Kashish Arya  
B.Tech CSE (AI & ML)  
GitHub: [Kashish7714](https://github.com/Kashish7714)

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
