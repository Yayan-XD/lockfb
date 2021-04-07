import sys

if sys.version[0:3] != "3.9":
  sys.exit("[+] anda harus menggunakan versi python 3.9, versi python anda sekarang : "+sys.version[0:3])

if __name__ == "__main__":
  try:
    __import__("brute").main()
  except Exception as E:
    exit(str(E))
