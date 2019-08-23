import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if type(numerator) is not int:
            raise TypeError
        if type(denominator) is not int:
            raise TypeError
        
        if denominator != 0:
            gcd = math.gcd(numerator, denominator)
            self.numerator = int(numerator/gcd)
            self.denominator = int(denominator/gcd)
        else:
            self.numerator = numerator
            self.denominator = denominator


    def nan(self):
        if self.denominator == 0:
            return math.nan

    def __str__(self):

        self.nan()

        if self.denominator in [1, -1]:
            return str(int(self.numerator/self.denominator))

        is_negative = self.numerator/self.denominator < 0

        if is_negative:
            return "-"+str(abs(self.numerator))+"/"+str(abs(self.denominator))
        else:
            return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        self.nan()

        result_numerator = (self.numerator*frac.denominator +
                            self.denominator*frac.numerator)
        result_denominator = self.denominator*frac.denominator

        return Fraction(result_numerator, result_denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator/self.denominator == frac.numerator/frac.denominator

    def __sub__(self, frac):
        """Return the subtraction result of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """

        if self.nan():
            return math.nan

        result_numerator = (self.numerator*frac.denominator -
                            self.denominator*frac.numerator)
        result_denominator = self.denominator*frac.denominator

        return Fraction(result_numerator, result_denominator)

    def __gt__(self, frac):
        # __gt__  for f > g

        return self.numerator/self.denominator > frac.numerator/frac.denominator

    def __mul__(self, frac):

        self.nan()

        result_numerator = self.numerator * frac.numerator
        result_denominator = self.denominator * frac.denominator

        return Fraction(result_numerator, result_denominator)

    def __neg__(self):
        self.nan()
        return Fraction(self.numerator * -1, self.denominator)

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)
