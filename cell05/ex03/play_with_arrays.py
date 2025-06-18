# play_with_arrays.py

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    print(original_array)

    # กรองค่า >= 8 แล้วบวก 2
    transformed = [x + 2 for x in original_array if x >= 8]

    # แปลงเป็นเซตเพื่อลบค่าซ้ำ
    result_set = set(transformed)
    print(result_set)

if __name__ == "__main__":
    main()  