# ฟังก์ชันเพื่อแสดงชื่อและวันเกิดของนักวิทยาศาสตร์หญิง
def famous_births(scientists):
    # ใช้การ loop ผ่าน dictionary และแสดงชื่อและวันเกิดของแต่ละคน
    for key, value in scientists.items():
        print(f"{value['name']} was born in {value['date_of_birth']}.")

# ข้อมูลของนักวิทยาศาสตร์หญิง
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

# เรียกใช้ฟังก์ชัน famous_births
famous_births(women_scientists)