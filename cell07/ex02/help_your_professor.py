# ฟังก์ชันคำนวณค่าเฉลี่ยของคะแนน
def average(class_scores):
    # คำนวณผลรวมของคะแนนแล้วหารด้วยจำนวนสมาชิกในคลาส
    return sum(class_scores.values()) / len(class_scores)

# ข้อมูลคะแนนของนักเรียนในคลาส 3B
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

# ข้อมูลคะแนนของนักเรียนในคลาส 3C
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# คำนวณค่าเฉลี่ยของทั้งสองคลาสและแสดงผล
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")