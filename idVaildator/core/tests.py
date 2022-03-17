import unittest
from .EgyptianNationalId import EgyptianNationalId
import datetime

VALID_ID = "30103211203135"


class TestNationalId(unittest.TestCase):
    def setUp(self) -> None:
        self.id = EgyptianNationalId(VALID_ID)

    def test_validaty(self):
        id_2 = "abc123"
        id_3 = "301031120135"
        id_4 = "4010311203135"
        id_5 = "30103214403135"

        with self.assertRaises(ValueError):
            EgyptianNationalId(id_2)
        with self.assertRaises(ValueError):
            EgyptianNationalId(id_3)
        with self.assertRaises(ValueError):
            EgyptianNationalId(id_4)
        with self.assertRaises(ValueError):
            EgyptianNationalId(id_5)
        self.assertEqual(self.id.is_valid(), True)

    def test_gender(self):
        id_female = EgyptianNationalId("29501023201922")
        self.assertEqual(self.id.fields["gender"], "Male")
        self.assertEqual(id_female.fields["gender"], "Female")

    def test_governarate(self):
        self.assertEqual(self.id.fields["governrate"], "Dakahlia")

    def test_birthday(self):
        self.assertEqual(
            self.id.fields["birthDate"], datetime.datetime(2001, 3, 21).date()
        )

    def test_century(self):
        self.assertTrue(2002 in self.id.century)


if __name__ == "__main__":
    unittest.main()
