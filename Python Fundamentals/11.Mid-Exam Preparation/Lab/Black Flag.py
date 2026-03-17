days = int(input())
plunder_for_a_day = int(input())
expected_plunder = float(input())
total_plunder = 0

for i in range(1, days + 1):

    total_plunder += plunder_for_a_day
    if i % 3 == 0:
        total_plunder += plunder_for_a_day * 0.50

    if i % 5 == 0:
        total_plunder -= total_plunder * 0.30

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    if expected_plunder != 0:
        print(f"Collected only {(total_plunder / expected_plunder) * 100:.2f}% of the plunder.")
