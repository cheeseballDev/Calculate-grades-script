## instead of relying on multiple global variables, pass the variables inside the function

def main():
    TERM_LIST = ["PRELIMS","MIDTERMS","PRE-FINALS","FINALS"]
    grades_list = []
    grades_list_mult = []
    grade_calc_holder = 0
    print(f"Welcome to grade script thing")
    subject_name = input("ENTER SUBJECT NAME: ")

    for term in TERM_LIST:
        while True:
            try:
                grade = input(f"What is your {term} grade for {subject_name}: ")
                grade = float(grade)
                if grade <= 100 and grade >= 65:
                    grades_list.append(grade)
                    break
                print(f"Invalid grade amount, try again!")
                continue
            except ValueError:
                print(f"Invalid input, try again!")
                continue

    def multiply_terms():
        for i in range(3, len(grades_list), 4):
            grade_calc_mult = (grades_list[i] * 0.40)
            grades_list_mult.append(grade_calc_mult)
        for p in range(0, 3):
            grade_calc_mult = (grades_list[p] * 0.20)
            grades_list_mult.append(grade_calc_mult)
        return add_terms()
    
    def add_terms():
        grade_calc_add = 0
        for grade in grades_list_mult:
            grade_calc_add += grade
        return grade_calc_add
    
    final_average = multiply_terms()
    print(f"Your final average in {subject_name} is {final_average:.2f}")

if __name__ == "__main__":
    main()
