# play_with_arrays.py

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    print("Original array:", original_array)

    # สร้างอาเรย์ใหม่โดยบวกแต่ละค่าด้วย 2
    new_array = [x + 2 for x in original_array]
    print("New array:", new_array)

if __name__ == "__main__":
    main()