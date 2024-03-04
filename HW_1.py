'''WEEKLY CONSUMPTION'''
print()
print('WEEKLY CONSUMPTION')
days_of_weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Enter consumption: ")
t_con = 0  # total consumption

for i in range(1, 8):  # cycles
    all_days = int(input(f"{days_of_weeks[i - 1]} – "))
    t_con += all_days  # bunch
a_con = round(t_con / 7, 1)  # average consumption #rounding and separation

print(f"Total consumption: {t_con} ")
print(f"Average consumption: {a_con}")

# print()
# print("Your weekly calculations are ready!")

if t_con >= 5000:
    print('Your weekly consumption is higher than planned!')
elif 5000 >= t_con > 0:
    print('Your weekly consumption is stable!')
else:
    print('Your weekly consumption is zero!')