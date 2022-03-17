import re
from datetime import datetime

EG_ID_REGEX: str = r"^(2|3)[0-9]{2}[0-1][0-9][0-3][0-9](01|02|03|04|11|12|13|14|15|16|17|18|19|21|22|23|24|25|26|27|28|29|31|32|33|34|35|88)\d{5}$"

GOVERNORATES: dict[str, str] = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Ash Sharqia",
    "14": "Kaliobeya",
    "15": "Kafr El - Sheikh",
    "16": "Gharbia",
    "17": "Monoufia",
    "18": "El Beheira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Fayoum",
    "24": "El Menia",
    "25": "Assiut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "New Valley",
    "33": "Matrouh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "Foreign",
}

CENTURY: dict[str, range] = {
    "2": range(1900, 2000),
    "3": range(2000, 2100),
}


class EgyptianNationalId:
    """
    Class repersting an Egyption National Id

    >>> id = EgyptianNationalId('29501023201952')
    >>> 1999 in id.century
    True
    >>> id.birth_date.year == 1995
    True
    >>> id.birth_date.month
    1
    >>> id.birth_date.day
    2
    >>> id.birth_date.governorate
    'New Valley'
    """

    def __init__(self, id: str) -> None:
        """
        init the class with the id number

        Args:
            id (str): The id number
        """
        self.id: str = id

        if not self.is_valid():
            raise ValueError("Invalid id number")

        self.fields = {}
        self.__extract_info_from_national_id()
        self.__convert_birth_date()
        self.__convert_century()
        self.__convert_gender()
        self.__convert_governrate()

    def is_valid(self) -> bool:
        """
        check the if format of the id is valid id number

        Returns:
            bool: return True if the id is valid False
        """
        match = re.match(EG_ID_REGEX, self.id)
        if match:
            return True
        return False

    def __extract_info_from_national_id(self) -> None:
        """
        Parse the string and extract the info from the id number

        Returns:
            None
        """
        self.birth_century: str = self.id[0]
        self.birth_str: str = self.id[1:7]
        self.governrate_code: str = self.id[7:9]
        self.serial_number: str = self.id[9:13]
        self.gender_code: int = int(self.id[12])
        self.check_digit: str = self.id[13]

    def __convert_gender(self) -> None:
        """
        Convert the gender code to male or female

        even -> female
        odd -> male
        """
        self.fields["gender"] = "Female" if self.gender_code % 2 == 0 else "Male"

    def __convert_governrate(self) -> None:
        """
        convert the governrate code to the governrate name
        """
        self.fields["governrate"] = GOVERNORATES[self.governrate_code]

    def __convert_birth_date(self) -> None:
        """
        Convert the birth date to a datetime object
        """
        self.fields["birthDate"] = datetime.strptime(self.birth_str, "%y%m%d").date()

    def __convert_century(self) -> None:
        """
        Convert the birth century to a range object
        """
        self.century: range = CENTURY[self.birth_century]

    def __str__(self) -> str:
        """
        Return the feilds of the id number
        """
        return (
            f"id {self.id} \n"
            f"birth_century {self.birth_century} \n"
            f"birth_date {self.birth_date} \n"
            f"governrate {self.governrate} \n"
            f"gender {self.gender}"
        )
