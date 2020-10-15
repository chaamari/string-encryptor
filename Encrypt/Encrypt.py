'''
Class for Encrypting a provided file
'''
import re
import csv
import logging


class Encrypt:
    char_count = dict()
    match_pattern = r"[a-z]+"
    sort_char_count = dict()
    encoder = dict()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, input_file, encrypted_file, decoder_file):
        self.input_file_name = input_file
        self.encrypted_file_name = encrypted_file
        self.decoder_file_name = decoder_file
        logging.basicConfig(filename='encryptor.log', level=logging.DEBUG)

    def encrypt(self):
        input_file = open(self.input_file_name, 'r')
        while True:
            # Read the next line from the source file
            line = input_file.readline()
            pattern = re.compile(self.match_pattern)
            matches = re.findall(pattern, line)
            for match in matches:
                # for each character in a match update the char_count dict
                for c in match:
                    # if item does not exist in char_count dict add it else increase the counter
                    if c not in self.char_count:
                        self.char_count[c] = 1
                    else:
                        self.char_count[c] += 1
            #break when the end of the file is reached
            if not line:
                break
        input_file.close()

        count_char_dict = dict()

        for k,v in self.char_count.items():
            if v in count_char_dict:
                count_char_dict[v].append(k)
            else:
                count_char_dict[v] = [k]
        # sort it by the number of occurrences
        sort_count_char = sorted(count_char_dict.items(), key=lambda x: x, reverse=True)

        #logging.debug("Character count len:", str(len(sort_count_char)))

        # sort the char count dictionary based on the char count values (reversed)
        #self.sort_char_count = sorted(self.char_count.items(), key=lambda x: x[1], reverse=True)

        # create the decoder file and encoder dictionary
        with open(self.decoder_file_name, 'w', newline='') as decoder_file:
            decoder_file_writer = csv.writer(decoder_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            # index for selecting the next item from the alphabet
            index = -1
            for item in sort_count_char:
                for c in sorted(item[1]):
                    index +=1
                    self.encoder[c] = self.alphabet[index]
                    decoder_file_writer.writerow([c, item[0], self.alphabet[index]])

        decoder_file.close()

        # Read the original file again to produce an encrypted file
        input_file = open(self.input_file_name, 'r')
        encrypted_file = open(self.encrypted_file_name, 'w')
        while True:
            # Read the next line from the source file
            line = input_file.readline()
            # break when the end of the file is reached
            if not line:
                break
            encrypted_line = []
            for c in line:
                if c in self.encoder:
                    encrypted_line.append(self.encoder[c])
                else:
                    encrypted_line.append(c)
            encrypted_file.write("".join(encrypted_line))

        encrypted_file.close()
        input_file.close()









