"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit G Take-Home Assignment
"""


def part1():
    max_pop = 0
    max_state = ""
    file_obj = open("States.txt", "r")
    for line in file_obj:
        line_list = line.split()
        pop = int(line_list[2])
        if line_list[1] == "Midwest" and pop > max_pop:
            max_pop = pop
            max_state = line_list[0]
    print(f"Highest population state in the Midwest is:  {max_state} {max_pop}")
    file_obj.close()


def part2_and_part3():
    d = {}
    f = open("USPresidents.txt")
    for line in f:
        (state_name, president_name) = line.split()
        if state_name not in d:
            d[state_name] = [president_name]
        else:
            d[state_name].append(president_name)
    f.close()

    # for k, v in d.items():
    #     print(k, v)

    max_presidents = max(d, key=lambda k: len(d[k]))
    print(f"The state with the most presidents is {max_presidents} with {len(d[max_presidents])} presidents:")
    for president_name in d[max_presidents]:
        print(president_name)

    print()
    d1 = {}
    for k, v in d.items():
        d1[k] = len(v)

    # for k, v in d1.items():
    #     print(k, v)

    most_pop_states = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}

    new_set = {(k, d1.get(k, 0)) for k in most_pop_states if d1.get(k, 0) != 0}

    print(f"{len(new_set)} of the {len(most_pop_states)} high populations states have had presidents born in them:")

    for s, no_of_pre in sorted(new_set):
        print(s, no_of_pre)


def main():
    # print("Part 1 output")
    part1()
    print()
    # print("Part 2 output")
    part2_and_part3()


if __name__ == "__main__":
    main()


'''
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITG_TAKEHOME_ASSIGNMENT_1.py
Highest population state in the Midwest is:  IL 12802000

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

8 of the 10 high populations states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2

Process finished with exit code 0

'''