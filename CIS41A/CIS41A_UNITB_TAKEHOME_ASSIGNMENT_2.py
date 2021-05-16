"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit B Take-Home Assignment 2
"""

SMALL_BEADS_BOX_PRICE = 9.20
MEDIUM_BEADS_BOX_PRICE = 8.52
LARGE_BEADS_BOX_PRICE = 7.98

no_of_small_beads = int(input("Enter number of small bead boxes:  "))
no_of_medium_beads = int(input("Enter number of medium bead boxes:  "))
no_of_large_beads = int(input("Enter number of large bead boxes:  "))

small_beads_cost = no_of_small_beads * SMALL_BEADS_BOX_PRICE
medium_beads_cost = no_of_medium_beads * MEDIUM_BEADS_BOX_PRICE
large_beads_cost = no_of_large_beads * LARGE_BEADS_BOX_PRICE
total_cost = small_beads_cost + medium_beads_cost + large_beads_cost

print(f"{'SIZE':<10s}{'QTY':>5s}{'COST PER BOX':>15s}{'TOTALS':>10s}")
print(f"{'Small':<10s}{no_of_small_beads:>5d}{SMALL_BEADS_BOX_PRICE:>15.2f}{small_beads_cost:>10.2f}")
print(f"{'Medium':<10s}{no_of_medium_beads:>5d}{MEDIUM_BEADS_BOX_PRICE:>15.2f}{medium_beads_cost:>10.2f}")
print(f"{'Large':<10s}{no_of_large_beads:>5d}{LARGE_BEADS_BOX_PRICE:>15.2f}{large_beads_cost:>10.2f}")
print(f"{'TOTAL':<30s}{total_cost:10.2f}")

"""
Execution results:
First Run:
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITB_TAKEHOME_ASSIGNMENT_2.py
Enter number of small bead boxes:  10
Enter number of medium bead boxes:  9
Enter number of large bead boxes:  8
SIZE        QTY   COST PER BOX    TOTALS
Small        10           9.20     92.00
Medium        9           8.52     76.68
Large         8           7.98     63.84
TOTAL                             232.52

Process finished with exit code 0

Second Run:
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITB_TAKEHOME_ASSIGNMENT_2.py
Enter number of small bead boxes:  5
Enter number of medium bead boxes:  10
Enter number of large bead boxes:  15
SIZE        QTY   COST PER BOX    TOTALS
Small         5           9.20     46.00
Medium       10           8.52     85.20
Large        15           7.98    119.70
TOTAL                             250.90

Process finished with exit code 0
"""
