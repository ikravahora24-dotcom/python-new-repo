def students_marks(marks):
    lowest_mark=min(marks)
    highest_mark=max(marks)
    average_mark=sum(marks)/len(marks)
    return lowest_mark,highest_mark,average_mark
marks=(78, 85, 62, 90, 55)
lowest_mark,highest_mark,average_mark=students_marks(marks)
print("Lowest Mark:", lowest_mark)
print("Highest Mark:", highest_mark)
print("Average Mark:", average_mark)
