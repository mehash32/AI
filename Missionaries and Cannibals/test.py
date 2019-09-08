
print("\n********* Missionaries and Carnival Game *********")
print("There are 3 missionaries and 3 carnivals at the left side of the display")
print("\n")
input("Press any key to start........ ")
print("\nX X X O O O     ------------------>  \n")

left_m = 3
left_c = 3

right_m = 0
right_c = 0

while 1:
    print("  What should be send from left to write ? ")
    m = int(input("    First type the number of missionaries :"))
    c = int(input("    Second type the number of carnivals :"))
    print("")
    if m+c <= 2 and m <= left_m and c <= left_c :
        left_m = left_m - m
        left_c = left_c - c
        if left_c > left_m > 0:
            print("Game Over....1")
            break
        right_m = right_m + m
        right_c = right_c + c
        if right_c > right_m > 0:
            print("Game Over....2")
            break
        for i in range(left_c):
            print("X ", end=" ")
        for i in range(left_m):
            print("O ", end=" ")
        print(" <------------------ ", end=" ")
        for i in range(right_c):
            print("X ", end=" ")
        for i in range(right_m):
            print("O ", end=" ")
        print("\n")
        if left_m == 0 and left_c == 0 and right_m == 3 and right_c == 3:
            print("Congratulations! You have done it.")
            break

        print("  What should be send from right to left ?")
        m = int(input("    First type the number of missionaries :"))
        c = int(input("    Second type the number of carnivals :"))
        if m + c <= 2 and m <= right_m and c <= right_c:
            right_m = right_m - m
            right_c = right_c - c
            if right_c > right_m > 0:
                print("Game Over....2")
                break
            left_m = left_m + m
            left_c = left_c + c
            if left_c > left_m > 0:
                print("Game Over....1")
                break

            for i in range(left_c):
                print("X ", end=" ")
            for i in range(left_m):
                print("O ", end=" ")
            print(" ------------------> ", end=" ")
            for i in range(right_c):
                print("X ", end=" ")
            for i in range(right_m):
                print("O ", end=" ")
            print("\n")
        else:
            print("\n  Wrong input. Please input the correct number\n")
    else:
        print("\n  Wrong input. Please input the correct number\n")