import hashlib , sys, pyfiglet

ascii_banner = pyfiglet.figlet_format('Hash Cracker')
print(ascii_banner)


print("Algorithms available:  MD5 | SHA1 | SHA22 | SHA224 | SHA256")

hash_type = str(input('Enter type of hash: '))
wordlist_location = str(input("Enter wordlist location: "))
hash = str(input('Enter Hash: '))

word_list = open(f'{wordlist_location}').read()

lists = word_list.splitlines()

def fn_md5():
    hash_object = hashlib.md5(f'{word}'.encode('utf-8'))
    hashed = hash_object.hexdigest()
    if hash == hashed:
        print(f"\033[1;32m HASH FOUND: {word} \n")

def fn_sha1():
    hash_object = hashlib.sha1(f'{word}'.encode('utf-8'))
    hashed = hash_object.hexdigest()
    if hash == hashed:
        print(f"\033 HASH FOUND: {word} \n")
    breakpoint
        
def fn_sha256():
    hash_object = hashlib.sha256(f'{word}'.encode('utf-8'))
    hashed = hash_object.hexdigest()
    if hash == hashed:
        print(f"\033[1;32m HASH FOUND: {word} \n")
    
for word in lists:
    if hash_type == 'MD5' or 'md5':
       fn_md5()
    
    
    elif hash_type == 'SHA1' or 'sha1':
        fn_sha1()
   
    elif hash_type == 'SHA256' or 'sha256':
        fn_sha256()
