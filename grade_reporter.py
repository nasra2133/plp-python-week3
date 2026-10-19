scores = [72, 45, 90, 61, 38]

passed=0
failed=0

total = sum(scores)
average = total / len(scores)

print("Total:", total)
print("Average:", round(average, 1))

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(score, grade)
    if score >= 50:
        passed += 1
    else:
        failed += 1
        print("Number passed:", passed)
        print("Number failed:", failed)
        print("Total score:", total)
        print("average:", round(average,)) 