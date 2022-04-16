# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Creating a simple database program using file processing
#
# Computer Science 111
# Name: Tsz Kit Wong
# Email: wongt@bu.edu

def main():
    """function is used to start the program"""

    file = input("Name of file: ")
    run = True

    while run:
        city = input("Name of city: ")
        if city == "quit":
            run = False
        else:
            state_abr = input("Abbreviation of state name:  ").upper()
            print()

        process_file(file, city, state_abr)


def process_file(file_name, city_name, state_name):
    """processes the lines from the text file given by user"""

    opened_file = open(file_name)
    no_result = False

    for line in opened_file:

        remove_end = line[:-1]
        fields = remove_end.split(",")

        popuation_field = float(fields[-1])
        actual_population = int(popuation_field * 1000)

        if city_name in line:
            if state_name in line:
                print(fields[0] + '\t' + fields[1] + '\t' + format(actual_population, '10,d'))
            else:
                no_result = True

    if no_result:
        print(f"No results found for {city_name}, {state_name}")

    print()

    opened_file.close()


# main()
