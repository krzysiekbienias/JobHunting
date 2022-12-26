import heapq

def intToRoman(num: int) -> str:
    t_digits = [("M", 1000), ("D", 500), ("C", 100),
                ("L", 50), ("X", 10),
                ("V", 5), ("I", 1),
                ("CM", 900), ("CD", 400), ("XC", 90), ("IX", 9), ("XL", 40), ("IV", 4)]
    t_digits.sort(key=lambda x:x[1],reverse=True)
    roman_int = []
    for symbol, value in t_digits:
        if num == 0:
            break
        count, num = divmod(num, value)
        roman_int.append(symbol * count)
    roman_num = "".join(roman_int)
    return roman_num



def reverse(row):
    return row.reverse()

def reversed_rows(matrix):

    rev=list(map(reverse,matrix))
    return rev
def swap_around_diag(matrix):

    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[j][i],matrix[i][j]=matrix[i][i],matrix[i][j]





if __name__=="__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    u,v=3,5
    rev_row=reversed_rows(matrix=matrix)
    print("THE END")


