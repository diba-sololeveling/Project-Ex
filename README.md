# 🥋 Warrior Class

## 📖 Overview
A simple Python class that simulates a **warrior** who can:  
- Gain **experience (XP)**  
- Increase in **level** and **rank**  
- Do **training** (with achievements)  
- Fight **battles** with different outcomes  

---

## ⚙️ Features
- **Levels**: `level = experience // 100` (max 100)  
- **Ranks**: From *Pushover* → *Greatest* (every 1000 XP)  
- **Training**: Adds XP + achievements if level is high enough  
- **Battles**: Outcomes: *Easy fight*, *A good fight*, *An intense fight*, *Defeated*  

---

## 🧑‍💻 Example
```python
bruce = Warrior()
print(bruce.level)        # 1
print(bruce.rank)         # Pushover
bruce.training(["Beat Boss", 500, 1])
print(bruce.experience)   # 600
print(bruce.battle(2))    # "An intense fight"
