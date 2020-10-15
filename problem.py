import sys
from Encrypt.Encrypt import Encrypt
from Decrypt.Decrypt import Decrypt

if __name__ == "__main__":
    arg_names = ["src", "function", "input_file", "output_file", "decoder_file"]
    args = dict()
    for i, arg in enumerate(sys.argv):
        args[arg_names[i]] = arg
    if args["function"] == "encrypt":
        e = Encrypt(args["input_file"], args["output_file"], args["decoder_file"])
        e.encrypt()
    elif args["function"] == "decrypt":
        d = Decrypt(args["input_file"], args["output_file"], args["decoder_file"])
        d.decrypt()



