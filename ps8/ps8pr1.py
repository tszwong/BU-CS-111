# ps8pr1.py  (Problem Set 8, Problem 1)
# A class to represent calendar dates
#
# CS 111
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu


class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year


    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s


    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####

    def advance_one(self):
        """changes the called object so that it represents one
        calendar day after the date that it originally represented"""

        self.day += 1
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.month == 2 and self.is_leap_year():
            days_in_month[2] = 29
            if self.day > days_in_month[self.month]:
                self.month += 1
                self.day = 1
        else:
            if self.day > days_in_month[self.month]:
                if self.month == 12:
                    self.month = 1
                    self.day = 1
                    self.year += 1
                else:
                    self.day = 1
                    self.month += 1


    def advance_n(self, n):
        """changes the calling object so that it represents n
        calendar days after the date it originally represented"""

        if n == 0:  # check if advancing 0 days
            print(self)

        else:
            print(self)
            for i in range(n):
                self.advance_one()
                print(self)  # prints the day during each iteration of the loop


    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other) represent
        the same calendar date (i.e., if the have the same values for their day, month,
        and year attributes). Otherwise, this method should return False"""

        if self.day == other.day and self.year == other.year \
                and self.month == other.month:
            return True
        else:
            return False


    def is_before(self, other):
        """returns True if the called object represents a calendar date that occurs
        before the calendar date that is represented by other. If self and other represent
        the same day, or if self occurs after other, the method should return False"""

        if self.year < other.year:  # check for smaller year
            return True
        elif self.year == other.year:  # if same year check month and/or day
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        else:
            return False


    def is_after(self, other):
        """eturns True if the calling object represents a calendar date that occurs after
        the calendar date that is represented by other. If self and other represent the same day,
        or if self occurs before other, the method should return False"""

        if self.year > other.year:
            return True
        else:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
            return False


    def days_between(self, other):
        """returns an integer that represents the
        number of days between self and other"""

        if self == other:
            return 0

        copy_self = self.copy()
        copy_other = other.copy()
        count_days = 0

        if copy_self.is_before(copy_other):
            while copy_self != copy_other:
                copy_self.advance_one()
                count_days -= 1

        if copy_self.is_after(copy_other):
            while copy_self != copy_other:
                copy_other.advance_one()
                count_days += 1

        return count_days


    def day_name(self):
        """returns a string that indicates the name of the day of the week of the Date
        object that calls it. In other words, the method should return one of the following
        strings: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' """

        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        week_day_index = self.days_between(Date(4, 11, 2022)) % 7

        week_day_name = day_names[week_day_index]

        return week_day_name
