# ฟังก์ชันหาคนที่มีผมสี "red"
def find_the_redheads(family):
    # ใช้ list comprehension เพื่อกรองคนที่มีผมสี "red"
    return [name.capitalize() for name, hair_color in family.items() if hair_color == "red"]

# ตัวอย่าง dictionary ของครอบครัว Dupont
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
print(find_the_redheads(dupont_family))