age = input('Please enter your age ')
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_limit = 90
weeks_in_a_year = round(365/7)
years_left = age_limit - int(age)
print(years_left)
print(weeks_in_a_year)
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left in your life.")