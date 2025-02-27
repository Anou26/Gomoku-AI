# **Gomoku-AI**  
An AI-powered Gomoku player leveraging **Convolutional Neural Networks (CNNs)** and the **Minimax Algorithm** to make strategic moves and outplay opponents. This project combines deep learning with classical game theory to create a formidable AI opponent.  

---

## **🛠️ Tech Stack**
- **Programming Language**: Python 🐍  
- **AI & ML**: PyTorch, NumPy, Scikit-learn  
- **Game Logic**: Minimax Algorithm with a Custom Heuristic  
- **Deep Learning Model**: Convolutional Neural Network (CNN)  
- **Development Tools**: VS Code, Git, GitHub  
- **Visualization & Performance**: Matplotlib, Pandas  

---

## **📜 Project Overview**
This AI was developed to play **Gomoku**, a strategy board game where two players compete to get five stones in a row on a 15x15 board. The AI makes decisions using:  
1. **CNN-Based State Evaluation**: The neural network predicts the value of board states, helping guide strategic play.  
2. **Minimax Algorithm with Alpha-Beta Pruning**: The AI simulates future moves and selects the best option while considering opponent responses.  
3. **Hybrid Approach**: If the neural network is uncertain, the minimax algorithm takes over to ensure optimal moves.  

By combining **machine learning** and **game heuristics**, this AI exhibits both **adaptability** and **strategic depth** in gameplay.  

---

## **📂 Folder Structure**
```
📦 Gomoku-AI
│── 📜 .gitignore           # Ignored files (virtual env, cache, logs)
│── 📜 README.md            # Project documentation (this file)
│── 📜 requirements.txt      # Dependencies for the project
│── 📂 gomoku                # Core game logic
│   ├── gomoku.py           # Board and rules implementation
│   ├── minimax.py          # Minimax algorithm for AI decision-making
│   ├── cnn_model.py        # Convolutional Neural Network for board evaluation
│   ├── compete.py          # AI vs AI or Human vs AI gameplay logic
│   ├── performance.py      # Benchmarking AI performance
│── 📂 policies              # Different AI strategies
│   ├── human.py            # Manual gameplay (human-controlled)
│   ├── random.py           # AI that plays randomly
│   ├── minimax.py          # Minimax AI opponent
│   ├── submission.py       # Combined CNN + Minimax AI strategy
```

---

## **🚀 Getting Started**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Anou26/Gomoku-AI.git
cd Gomoku-AI
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python -m venv gomoku-ai-env
source gomoku-ai-env/bin/activate  # macOS/Linux
gomoku-ai-env\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Game**
To play a game between two AIs (Minimax vs. Random):
```bash
python compete.py -b 15 -w 5 -x Minimax -o Random
```

To evaluate AI performance:
```bash
python performance.py
```

---

## **🤖 Training the Neural Network**
To train the CNN model:
```bash
python cnn_model.py
```
The dataset consists of **2,880 game states** from the **GomoCup 2022** dataset, and training is performed for **20 epochs** using the **Adam optimizer**. The final model is stored in `models/model_best.pth`.

---

## **🎯 Features**
✔️ **15x15 Gomoku Board**  
✔️ **CNN-Based Board Evaluation**  
✔️ **Minimax with Alpha-Beta Pruning**  
✔️ **Custom Heuristic Function for Game Scoring**  
✔️ **AI vs AI and AI vs Human Modes**  
✔️ **Performance Benchmarking & Visualization**  

---

## **🛠️ Future Enhancements**
- ✅ Reinforcement Learning Integration (Q-Learning / Deep Q-Networks)  
- ✅ Smarter Heuristic Improvements for the Minimax Algorithm  
- ✅ Optimized Model with Larger Dataset Training  
- ✅ UI-Based Game Interface for Better Player Experience  
