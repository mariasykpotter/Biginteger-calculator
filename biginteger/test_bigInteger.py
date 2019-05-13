import unittest
from biginteger import BigInteger


class TestBigInteger(unittest.TestCase):

    def setUp(self):
        data_file = open("data.txt", "r")
        self.data_list = data_file.read().split("\n")
        data_file.close()
        minus = [False] * 10
        for i in range(len(self.data_list)):
            if len(self.data_list[i]) > 1:
                if self.data_list[i][0] == "-":
                    self.data_list[i] = self.data_list[i].replace("-", "")
                    minus[i] = True
        self.big1 = BigInteger(minus[0], self.data_list[0])
        self.big2 = BigInteger(minus[1], self.data_list[1])
        self.big3 = BigInteger(minus[2], self.data_list[2])
        self.big4 = BigInteger(minus[3], self.data_list[3])
        self.big5 = BigInteger(minus[4], self.data_list[4])
        self.big6 = BigInteger(minus[5], self.data_list[5])
        self.big7 = BigInteger(minus[6], self.data_list[6])
        self.big8 = BigInteger(minus[7], self.data_list[7])
        self.big9 = BigInteger(minus[8], self.data_list[8])
        self.big10 = BigInteger(minus[9], self.data_list[9])

    def test_string(self):
        self.assertEqual(self.big1.toString(), self.data_list[0])
        self.assertEqual(self.big2.toString(), self.data_list[1])
        self.assertEqual(self.big5.show(),
                         "3 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 4 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5 - 5")

    def test_comparison(self):
        self.assertEqual(self.big1 > self.big2, False)
        self.assertEqual(self.big2 >= self.big2, True)
        self.assertEqual(self.big3 == self.big2, True)

    def test_arithmethics(self):
        self.assertEqual((self.big1 + self.big2).toString(),
                         "99999000000555555555555562222233333333333333333331111112222222222222211110888")
        self.assertEqual((self.big1 - self.big2).toString(),
                         "79998999999444444444444451111099999999999999999997777776666666666666655555334")
        self.assertEqual((self.big1 * self.big2).toString(),
                         "899990000049999444444444511112111103703703703703681481655553209876543098763138742752962901234567901105920986419753086419753075802222098765432098774074247")
        self.assertEqual((self.big1 // self.big2).toString(), "0")
        self.assertEqual((self.big2 // self.big1).toString(), "8")
        self.assertEqual((self.big2 % self.big1).toString(),
                         "9998999995555555555555562222133333333333333333331111102222222222222211110895")
        self.assertEqual((self.big1 ** self.big4).toString(),
                         '100000000011111111111419753086641975308654320987654321009876666667901234567885679012369506172839506172839488890123456790123456790121728395061728395061729')

    def test_dodatny_vidjemny(self):
        self.assertEqual((self.big9 + self.big10).minus, True)
        self.assertEqual((self.big9 - self.big10).minus, True)
        self.assertEqual((self.big9 * self.big10).minus, True)
        self.assertEqual((self.big8 // self.big7).toString(), "36029")
        self.assertEqual((self.big8 // self.big7).minus, True)
        self.assertEqual((self.big8 // self.big9).minus, False)
        self.assertEqual((self.big8 // self.big9).toString(), "1835")
        self.assertEqual((self.big9 // self.big10).toString(), "5")
        self.assertEqual((self.big9 // self.big10).minus, True)

    def test_bitwis_ops(self):
        self.assertEqual(self.big6.bigint_to_bin().toString(), "1000111010111")
        self.num = (self.big6.bigint_to_bin())
        self.assertEqual(self.num.bin_to_bigint().toString(), "4567")
        self.assertEqual((self.big7 & self.big6).toString(),
                         str(int(self.big6.toString()) & int(self.big7.toString())))
        self.assertEqual((self.big7 ^ self.big6).toString(),
                         str(int(self.big6.toString()) ^ int(self.big7.toString())))
        self.assertEqual((self.big7 | self.big6).toString(),
                         str(int(self.big6.toString()) | int(self.big7.toString())))
        self.assertEqual((self.big7 >> 3).toString(),
                         str(int(self.big7.toString()) >> 3))
        self.assertEqual((self.big7 << 5).toString(), str(int(self.big7.toString()) << 5))


if __name__ == "__main__":
    unittest.main()
