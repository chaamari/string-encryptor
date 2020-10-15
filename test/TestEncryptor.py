import unittest
from Encrypt.Encrypt import Encrypt
from Decrypt.Decrypt import Decrypt

class TestString(unittest.TestCase):
    def test_encrypted_string(self):
        out_file = open("input.txt", "w")
        out_file.write("some test string")
        out_file.close()
        e = Encrypt("input.txt", "encrypted_input.txt", "unittest_decoder.txt")
        e.encrypt()
        f = open("encrypted_input.txt", "r")
        self.assertEqual('ahfc bcab abiegd', f.readline())
        f.close()

    def test_decrypted_string(self):
        out_file = open("input_d.txt", "w")
        out_file.write("ahfc bcab abiegd")
        out_file.close()
        d = Decrypt("input_d.txt", "decrypted_input.txt", "unittest_decoder.txt")
        d.decrypt()
        f = open("decrypted_input.txt", "r")
        self.assertEqual('some test string', f.readline())
        f.close()


if __name__ == '__main__':
    unittest.main()



