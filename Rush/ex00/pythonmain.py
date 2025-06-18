from typing import List, Dict

class Transaction:
    def __init__(self, description: str, amount: float, category: str, date: str):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

class FinanceManager:
    def __init__(self):
        self.transactions: List[Transaction] = []
    
    def add_transaction(self, description: str, amount: float, category: str, date: str):
        """เพิ่มรายการรายรับ/รายจ่ายใหม่"""
        new_transaction = Transaction(description, amount, category, date)
        self.transactions.append(new_transaction)
        print("บันทึกรายการสำเร็จ!")
    
    def show_balance(self):
        """แสดงยอดคงเหลือปัจจุบัน"""
        balance = sum(t.amount for t in self.transactions)
        print(f"\nยอดคงเหลือปัจจุบัน: {balance:,.2f} บาท")
    
    def show_transactions(self):
        """แสดงประวัติรายการทั้งหมด"""
        if not self.transactions:
            print("ยังไม่มีรายการ")
            return
        
        print("\nประวัติรายการทั้งหมด:")
        for i, t in enumerate(self.transactions, 1):
            print(f"{i}. {t.date} - {t.description} ({t.category}) {t.amount:+,.2f} บาท")
    
    def summarize_by_category(self):
        """สรุปยอดเงินตามประเภท"""
        if not self.transactions:
            print("ยังไม่มีรายการ")
            return
        
        categories: Dict[str, float] = {}
        for t in self.transactions:
            categories[t.category] = categories.get(t.category, 0) + t.amount
        
        print("\nสรุปยอดเงินตามประเภท:")
        for category, total in categories.items():
            print(f"- {category}: {total:+,.2f} บาท")

def display_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*40)
    print("Personal Finance Tracker")
    print("="*40)
    print("1. เพิ่มรายการรายรับ/รายจ่าย")
    print("2. ดูยอดคงเหลือ")
    print("3. แสดงประวัติรายการทั้งหมด")
    print("4. สรุปยอดเงินตามประเภท")
    print("5. ออกจากโปรแกรม")
    print("="*40)

def main():
    manager = FinanceManager()
    
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            desc = input("รายการ: ")
            amount = float(input("จำนวนเงิน: "))
            category = input("ประเภท (เช่น อาหาร, ค่าผ่อนรถ, เงินเดือน): ")
            date = input("วันที่ (dd/mm/yyyy): ")
            manager.add_transaction(desc, amount, category, date)
        
        elif choice == "2":
            manager.show_balance()
        
        elif choice == "3":
            manager.show_transactions()
        
        elif choice == "4":
            manager.summarize_by_category()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้บริการ!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()
    