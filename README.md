# Expense Tracker CLI

## Overview
A robust Command-Line Interface (CLI) tool designed for efficient personal finance management. Track your spending, categorize expenses, and monitor your budget directly from your terminal with persistent JSON storage.

## Key Features
- Easy Logging: Add expenses with descriptions, amounts, and categories.
- - JSON Storage: All data is saved locally in a structured JSON format.
  - - Advanced Filtering: View expenses by category or date ranges.
    - - Monthly Summaries: Get detailed insights into your monthly spending habits.
      - - Budget Alerts: Set spending limits and receive alerts when you're close to exceeding them.
        - - Full CRUD: Seamlessly add, view, update, and delete entries.
         
          ## Installation
          - 1. Clone the repository:
            2.    git clone https://github.com/Shiv-0707/expense-tracker-cli.git
            3.   cd expense-tracker-cli
            4.   2. Install dependencies (if any):
                 3.    pip install -r requirements.txt
              
                 ## Usage
                 Here are some common commands to get you started:
                 - Add an expense: python main.py add --description "Lunch" --amount 15.50 --category "Food"
                 - - View all expenses: python main.py list
                   - - Get a summary for a month: python main.py summary --month 3
                    
                     - ## Data Storage
                     - Expenses are stored in expenses.json in the root directory. This allows for easy manual backup and portability.
