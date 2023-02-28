from constraint import Problem


def coloring_map():
    # Part 1 - we will do this together in class.
    p = Problem()
    p.addVariable("WA", ("Red", "Green", "Blue"))
    p.addVariable("NT", ("Red", "Green", "Blue"))
    p.addVariable("SA", ("Red", "Green", "Blue"))
    p.addVariable("Q", ("Red", "Green", "Blue"))
    p.addVariable("V", ("Red", "Green", "Blue"))
    p.addVariable("NSW", ("Red", "Green", "Blue"))
    p.addVariable("T", ("Red", "Green", "Blue"))

    p.addConstraint(lambda a,b: a != b, ("SA", "WA"))
    p.addConstraint(lambda a,b: a != b, ("SA", "NT"))
    p.addConstraint(lambda a,b: a != b, ("SA", "Q"))
    p.addConstraint(lambda a,b: a != b, ("SA", "NSW"))
    p.addConstraint(lambda a,b: a != b, ("SA", "V"))
    p.addConstraint(lambda a,b: a != b, ("WA", "NT"))
    p.addConstraint(lambda a,b: a != b, ("NT", "NSW"))
    p.addConstraint(lambda a,b: a != b, ("V", "NSW"))
    print(p.getSolution())


def scheduling_problem():
    # Look at "Part 2" instructions and do that here.
    week = Problem()
    week.addVariable("Alice", ("Mon", "Wed", "Fri"))
    week.addVariable("Bob", ("Mon", "Tue"))
    week.addVariable("Charlie", ("Tue", "Wed", "Thu", "Fri"))
    week.addVariable("Danielle", ("Mon", "Wed", "Fri"))
    week.addVariable("Edwin", ("Wed", "Thu", "Fri"))

    week.addConstraint(lambda a,b: a == b, ("Bob", "Alice"))
    week.addConstraint(lambda a,b: a != b, ("Danielle", "Charlie"))
    week.addConstraint(lambda a,b: a != b, ("Bob", "Charlie"))
    week.addConstraint(lambda a,b: a != b, ("Danielle", "Edwin"))
    week.addConstraint(lambda a,b: a != b, ("Danielle", "Alice"))
    week.addConstraint(lambda a,b,c: a in (b, c), ("Edwin", "Bob", "Charlie"))
    print(week.getSolution())




def main():
  coloring_map()
  scheduling_problem()
  

if __name__ == "__main__":
  main()