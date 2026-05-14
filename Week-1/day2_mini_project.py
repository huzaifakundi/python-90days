# =============================================
# MINI PROJECT — Study Tracker
# =============================================

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_per_day = [1, 1, 1, 1, 1, 3, 3]

print("\n--- My Weekly Study Schedule ---")
total_hours = 0

for i in range(len(days_of_week)):
    day = days_of_week[i]
    hours = hours_per_day[i]
    total_hours += hours      # adds to running total
    print(f"{day}: {hours} hour(s)")
#alternative using zip
total_hours = 0
for day, hours in zip(days_of_week, hours_per_day):
    total_hours += hours
    print(f"{day}: {hours} hour(s)")

print(f"\nTotal study hours this week: {total_hours}")
print(f"Total study hours in 90 days (~13 weeks): {total_hours * 13}")