##
#### The observed PIN (4 kyu)
#################################

import itertools


def get_pins(observed):
    adj_list = {
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["5", "7", "8", "9", "0"],
        "9": ["6", "8", "9"],
        "0": ["8", "0"],
    }

    neighbors = [adj_list[x] for x in observed]

    return ["".join(elem) for elem in list(itertools.product(*neighbors))]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(get_pins("8"), ["5", "7", "8", "9", "0"]),
        self.assertEqual(
            get_pins("11"), ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
        ),
        self.assertEqual(
            get_pins("369"),
            [
                "339",
                "366",
                "399",
                "658",
                "636",
                "258",
                "268",
                "669",
                "668",
                "266",
                "369",
                "398",
                "256",
                "296",
                "259",
                "368",
                "638",
                "396",
                "238",
                "356",
                "659",
                "639",
                "666",
                "359",
                "336",
                "299",
                "338",
                "696",
                "269",
                "358",
                "656",
                "698",
                "699",
                "298",
                "236",
                "239",
            ],
        )


if __name__ == "__main__":
    unittest.main()
