# ฟังก์ชันที่จะเพิ่ม 1 ให้กับค่าที่ส่งมา
def add_one(value):
    return value + 1

# โปรแกรมเริ่มทำงานที่นี่
if __name__ == "__main__":
    # ตัวแปรที่เราจะใช้
    my_var = 5

    # แสดงค่าของตัวแปรก่อนการเรียกฟังก์ชัน
    print("Before calling add_one:", my_var)

    # เรียกฟังก์ชัน add_one และอัพเดตค่าของตัวแปร
    my_var = add_one(my_var)

    # แสดงค่าของตัวแปรหลังการเรียกฟังก์ชัน
    print("After calling add_one:", my_var)