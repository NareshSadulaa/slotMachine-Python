# 🎰 Slot Machine Game (Python)

A **console-based slot machine game** built in Python that allows players to deposit money, place bets on lines, and spin to try their luck. The game calculates winnings based on matching symbols and tracks the player’s balance across multiple spins.

---

## ✨ Features

* **Deposit System** – Players can deposit money before playing.
* **Multiple Lines Betting** – Bet on 1 to 3 lines at once.
* **Configurable Betting Limits** – Minimum and maximum bets per line.
* **Randomized Spins** – Uses Python’s `random` module to shuffle symbols.
* **Winnings Calculation** – Based on symbol values and bet amount.
* **Balance Tracking** – Updates after every spin.

---

## 🛠️ Technologies Used

* **Python 3** – Core programming language.
* **Random Module** – To simulate slot spins and random symbol placement.

---

## 🎮 How to Play

1. **Deposit money** to start the game.
2. **Choose number of lines** to bet on (1–3).
3. **Set bet amount** per line.
4. **Spin** and see the results:

   * Matching symbols across a line win money.
   * Payout is based on the symbol’s value × bet amount.
5. **Play again** or quit — your balance updates automatically.

---

## 📊 Symbol Values

| Symbol | Count in Machine | Value (Multiplier) |
| ------ | ---------------- | ------------------ |
| A      | 2                | 5× bet             |
| B      | 4                | 4× bet             |
| C      | 6                | 3× bet             |
| D      | 8                | 2× bet             |

---

## 🚀 How to Run

1. Clone this repository or download the `.py` file.
2. Run the game in terminal:

   ```bash
   python slot_machine.py
   ```
3. Follow on-screen prompts to play.

---

## 📌 Example Gameplay

```
What amount would you like to deposit? $50
Enter the number of lines to bet on (1-3)? 3
Enter the amount you would like to bet on each line? $5
You're betting $5 on 3 lines. Your total bet is $15
A | C | D
B | C | D
A | A | A
You Won $15.
You Won on 3
Current balance is $50
Press Enter to Play Again or q to quit:
```

---

## 📜 License

This project is open-source and available under the **MIT License**.
