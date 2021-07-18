

def format_customer(first_name, last_name, location = None):
    if location is None:
        print(first_name, last_name)
    else:
        print(first_name, last_name, "("+location+")")

format_customer("John", "Smith", location="California")
format_customer('Mareike', 'Schmidt')


def format_customer_second_way(first_name, last_name, location=None):
    if location is None:
        print("%s %s"%(first_name, last_name))
    else:
        print("%s %s (%s)"%(first_name, last_name, location))

format_customer_second_way("John", "Smith", location="California")
format_customer_second_way('Mareike', 'Schmidt')

def format_customer_third_way(first_name, last_name, location=None):
    if location is None:
        print("{} {}".format(first_name, last_name))
    else:
        print("{} {} ({})".format(first_name, last_name, location))

format_customer_third_way("John","Smith")
