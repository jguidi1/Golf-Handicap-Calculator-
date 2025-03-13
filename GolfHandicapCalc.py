def golf_handicap_calc(score, course_rating, slope_rating):
    differential = (score - course_rating) * 113 / slope_rating
    return differential

score = int(input("Enter your score: "))
course_rating = float(input("Enter the course rating: "))
slope_rating = int(input("Enter the slope rating: "))
differential = golf_handicap_calc(score, course_rating, slope_rating)
print("Your differential is: " + str(differential))