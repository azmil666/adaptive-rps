# Adaptive Rock-Paper-Scissors (AI Opponent)

This is an advanced Rock-Paper-Scissors game where the computer *learns* from the player's behavior and adapts its strategy over time.  
It is not random — it uses prediction models to counter your moves.

## 🧠 Features
- Tracks frequency of player moves  
- Uses transition probabilities (Markov-like logic)  
- Reacts differently based on win/lose/tie pattern  
- Combines 3 predictions using a voting system  
- Computer chooses the *counter* to predicted human move  
- Shows score and total rounds  

## 🛠 Prediction System
The AI predicts your next move using:

1. **Frequency Model**  
2. **Transition Model** (previous move → next move)  
3. **Outcome Model** (based on win/lose/tie)

Each model votes, and the final prediction is chosen by majority.

Then the computer plays the **counter move**.

## ▶️ Run the Game
```bash
python3 rps.py
