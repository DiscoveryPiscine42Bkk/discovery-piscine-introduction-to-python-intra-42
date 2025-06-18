import sys

# ฟังก์ชันหลักที่รับอาร์กิวเมนต์จาก command line
def main():
    # ตรวจสอบว่ามีอาร์กิวเมนต์หรือไม่
    if len(sys.argv) <= 1:
        print("none")
        return

    # ถ้ามีอาร์กิวเมนต์ ให้แสดงค่าที่รับเข้ามา
    for arg in sys.argv[1:]:
        print(f"{arg}ZZZZZ$")

if __name__ == "__main__":
    main()