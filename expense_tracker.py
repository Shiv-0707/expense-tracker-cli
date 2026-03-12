#!/usr/bin/env python3
"""
Personal Expense Tracker - CLI Application
Track, categorize, and analyze personal expenses with ease.
"""

import json
import os
from datetime import datetime, date
from collections import defaultdict
from typing import Optional, List, Dict

# Configuration
DATA_FILE = "expenses.json"
CATEGORIES = [
    "Food & Dining", "Transportation", "Housing", "Utilities",
    "Entertainment", "Healthcare", "Shopping", "Education",
    "Travel", "Other"
]
MONTHLY_BUDGET = 2000.00


class ExpenseTracker:
    """Main expense tracker class."""
    
    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
        self.expenses = self._load_expenses()
    
    def _load_expenses(self) -> List[Dict]:
        """Load expenses from JSON file."""
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    
    def _save_expenses(self) -> bool:
        """Save expenses to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.expenses, f, indent=2, default=str)
            return True
        except IOError:
            return False
    
    def add_expense(self, amount: float, description: str, 
                   category: str, expense_date: str = None) -> bool:
        """Add a new expense."""
        if amount <= 0:
            return False
        if not description:
            return False
        if category not in CATEGORIES:
            return False
        
        expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "description": description,
            "category": category,
            "date": expense_date or date.today().isoformat(),
            "created_at": datetime.now().isoformat()
        }
        self.expenses.append(expense)
        return self._save_expenses()
    
    def get_total(self) -> float:
        """Calculate total expenses."""
        return sum(e["amount"] for e in self.expenses)
    
    def get_by_category(self, category: str) -> List[Dict]:
        """Get expenses by category."""
        return [e for e in self.expenses if e["category"] == category]
    
    def get_monthly_total(self, month: str) -> float:
        """Get total expenses for a specific month (YYYY-MM)."""
        return sum(e["amount"] for e in self.expenses 
                   if e["date"].startswith(month))
    
    def delete_expense(self, exp_id: int) -> bool:
        """Delete an expense by ID."""
        for i, exp in enumerate(self.expenses):
            if exp["id"] == exp_id:
                self.expenses.pop(i)
                return self._save_expenses()
        return False
    
    def get_statistics(self) -> Dict:
        """Get expense statistics."""
        if not self.expenses:
            return {}
        
        amounts = [e["amount"] for e in self.expenses]
        return {
            "total": sum(amounts),
            "count": len(amounts),
            "average": sum(amounts) / len(amounts),
            "highest": max(amounts),
            "lowest": min(amounts)
        }


def main():
    """Main application loop."""
    tracker = ExpenseTracker()
    print("\n" + "="*50)
    print("💰 EXPENSE TRACKER")
    print("="*50)
    
    # Example usage
    print(f"\n✓ Loaded {len(tracker.expenses)} expenses")
    print(f"✓ Total spent: ${tracker.get_total():.2f}")
    
    # Add a sample expense
    tracker.add_expense(45.50, "Lunch at restaurant", "Food & Dining")
    print("✓ Added sample expense")
    
    # Get statistics
    stats = tracker.get_statistics()
    if stats:
        print(f"\n📊 Statistics:")
        print(f"  Average: ${stats['average']:.2f}")
        print(f"  Highest: ${stats['highest']:.2f}")
        print(f"  Lowest: ${stats['lowest']:.2f}")


if __name__ == "__main__":
    main()
