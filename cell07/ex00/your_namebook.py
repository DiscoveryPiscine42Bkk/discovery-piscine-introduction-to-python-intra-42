# สร้างฟังก์ชันเพื่อดึงข้อมูลจาก dictionary และคืนค่าลิสต์ของชื่อ
def array_of_names(persons):
    # คืนค่าลิสต์ของชื่อ (การรวมชื่อและนามสกุล)
    return [f"{key.capitalize()} {value.capitalize()}" for key, value in persons.items()]

# ตัวอย่าง dictionary
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
print(array_of_names(persons))