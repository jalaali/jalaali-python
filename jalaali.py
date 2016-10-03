class Jalaali:
    @staticmethod
    def to_jalaali(gy, gm, gd):
        """Convert a Gregorian date to Jalaali

        :param gy: Gregorian Year
        :type gy: int
        :param gm: Gregorian Month
        :type gm: int
        :param gd: Gregorian Day
        :type gd: int
        :return: the converted Jalaali date
        :rtype: tuple
        """
        # TODO return method to_jalaali

    @staticmethod
    def to_gregorian(jy, jm, jd):
        """Convert a Jalaali date to Gregorian

        :param jy: Jalaali Year
        :type jy: int
        :param jm: Jalaali Moth
        :type jm: int
        :param jd: Jalaali Day
        :type jd: int
        :return: the converted Gregorian date
        :rtype: tuple
        """

        # TODO return method to_Gregorian

    @staticmethod
    def is_valid_jalaali_date(jy, jm, jd):
        """Checks whether a Jalaali date is valid or not.

        :param jy: Jalaali Year
        :type jy: int
        :param jm: Jalaali Month
        :type jm: int
        :param jd: Jalaali Day
        :type jd: int
        :return: is date valid?
        :rtype: bool
        """
        year_is_valid = (-61 <= jy <= 3177)
        month_is_valid = (1 <= jm <= 12)
        pass

    @staticmethod
    def is_leap_jalaali_year(jy):
        """Checks whether this is a leap year or not.

        :param jy: Jalaali Year
        :type jy: int
        :return: is leap year?
        :rtype: bool
        """
        pass
