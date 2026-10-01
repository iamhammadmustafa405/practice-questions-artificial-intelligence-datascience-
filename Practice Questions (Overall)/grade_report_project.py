# Write a function called 'grade_report' that takes a student's name and any number of exam scores
# (*args). It should return a dictionary with: name, scores list, average, highest score, lowest score,
# and letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, F otherwise).

def avg(scores):
    sum=0
    for score in scores:
        sum += score
    return sum/2

def max_score(scores):
    max=scores[0]
    for i in range(len(scores)):
        if scores[i] > max:
            max= scores[i]
    return max

def min_score(scores):
    min=scores[0]
    for i in range(len(scores)):
        if scores[i] < min:
            min= scores[i]
    return min

def grade(scores):
    sum=0
    for score in scores:
        sum+=score
        
        if sum >= 90:
            return "A Grade"
        elif sum >= 80 and sum < 90:
            return "B Grade"
        elif sum >= 70 and sum < 80:
            return "C Grade"
        elif sum >= 60 and sum < 70:
            return "D Grade"
        elif sum <60:
            return "F"

def grade_report(name,scores):
    
    dict = {"name": name,
            "scores": scores,
            "average": avg(scores),
            "grade": grade(scores),
            "highest score": max(scores),
            "lowest score": min(scores)}
    return dict


my_result= grade_report(name="Hammad Mustafa",scores= [10,20,30,40])
print(my_result)

