# 💰 Expense Tracker (Python)

A simple Expense Tracker built using Python and the CSV module. This application allows users to record daily expenses, view all saved expenses, and calculate the total amount spent. All expense records are stored in an `expenses.csv` file.

---

## 🚀 Features

- Add a new expense
- Save expenses in a CSV file
- View all saved expenses
- Calculate the total amount spent
- Date validation (DD-MM-YYYY format)
- User-friendly menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- CSV Module
- OS Module
- Datetime Module

---

## 📂 Project Structure

```
ExpenseTracker/
│── main.py
│── expenses.csv (created automatically)
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Open the project folder.

```bash
cd expense-tracker
```

3. Run the program.

```bash
python main.py
```

---

## 💻 Example Output

```
===================================
        EXPENSE TRACKER
===================================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit

Enter Your Choice: 1

Enter Date (DD-MM-YYYY): 29-06-2026
Enter Category: Food
Enter Amount: 250

Expense Added Successfully!
```

---

## 📄 Sample CSV File

```
Date,Category,Amount
29-06-2026,Food,250
30-06-2026,Travel,500
01-07-2026,Shopping,1200
```

---

## 📖 How It Works

1. The user selects an option from the menu.
2. The program asks for the expense details (Date, Category, Amount).
3. The expense is saved in the `expenses.csv` file.
4. Users can view all saved expenses.
5. The program calculates and displays the total amount spent.

---

## 📚 Key Concepts Used

- Functions
- File Handling
- CSV Module
- Loops
- Conditional Statements
- Exception Handling
- Date Validation
- User Input
- Lists

---

## 🎯 Future Improvements

- Edit an existing expense
- Delete an expense
- Search expenses by category
- Monthly expense report
- Expense charts using Matplotlib
- GUI version using Tkinter
- Database support using SQLite

---

## 👨‍💻 Author

**Aryan Kumar**

---

⭐ If you found this project helpful, consider giving it a Star on GitHub!
