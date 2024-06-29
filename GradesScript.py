term_list = ["PRELIMS", "MIDTERMS", "PRE-FINALS", "FINALS"]
grades_list = []
grade_calc_holder = 0
print(f"Welcome to grade script thing")
subject_name = input("ENTER SUBJECT NAME: ")

for term in term_list:
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

def identify_terms():
    grade_calc_add = 0
    for term in term_list:
        for grade in grades_list:
            grade_calc_mult = calculate_terms(term, grade)
        grade_calc_add  += grade_calc_mult
        return grade_calc_add

def calculate_terms(term, grade):
    match term:
        case "PRELIMS":
            grade_calc_mult = (grade * 0.20)
            return grade_calc_mult 
        case "MIDTERMS":
            grade_calc_mult = (grade * 0.20)
            return grade_calc_mult 
        case "PRE-FINALS":
            grade_calc_mult = (grade * 0.20)
            return grade_calc_mult 
        case "FINALS":
            grade_calc_mult = (grade * 0.40)
            return grade_calc_mult 

print(f"Your final average in {subject_name} is ", identify_terms())

##grade_calc_final = grade_calc_forty * grade_calc_final
##print(f"Final average is: {grade_calc_final}")

