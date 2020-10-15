'''
Class for Decrypting a file
'''

import csv
import logging

class Decrypt:
    char_count = dict()
    match_pattern = r"[a-z]+"
    sort_char_count = dict()
    decoder = dict()

    def __init__(self, input_file, decrypted_file, decoder_file):
        self.input_file_name = input_file
        self.decrypted_file_name = decrypted_file
        self.decoder_file_name = decoder_file
        logging.basicConfig(filename='decryptor.log', level=logging.DEBUG)

    def decrypt(self):
        # Read lines in the decoder file and initialize decoder object
        with open(self.decoder_file_name, newline='') as csvfile:
            decoder_reader = csv.reader(csvfile, delimiter=',')
            for original, count, replaced in decoder_reader:
                self.decoder[replaced] = original
                logging.debug("Replace:{} with {}".format(replaced, original))
        # Read encrypted input file and output the decrypted file
        input_file = open(self.input_file_name, 'r')
        output_file = open(self.decrypted_file_name, 'w')
        while True:
            # Read the next line from the input file
            line = input_file.readline()
            # break when the end of the file is reached
            if not line:
                break
            output_line = []
            # decrypt each character in a line
            for c in line:
                if c in self.decoder:
                    output_line.append(self.decoder[c])
                else:
                    # omit special chars
                    output_line.append(c)
            output_file.write("".join(output_line))

        input_file.close()
        output_file.close()









