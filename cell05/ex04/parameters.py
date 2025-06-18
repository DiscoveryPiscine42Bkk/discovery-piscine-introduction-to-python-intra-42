# parameters.py

import sys

def main():
    # ไม่รวมชื่อไฟล์ (sys.argv[0])
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()                      