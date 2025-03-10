#!/usr/bin/python3
import hashlib,os,pdfplumber,colorama,time,random,zipfile,msoffcrypto,io,threading,chardet
from itertools import product
from rarfile import RarFile


def format_path(path):
    if path[0] == "~":
        path = path.replace("~",os.environ["HOME"])
    if path[0] == "'" and path[-1] == "'":
        path = path[1:-1]
    if path[0] == '"' and path[-1] == '"':
        path = path[1:-1]
    return path

class Genrator:
    def Random(self,charectors,min,max,limit):
        char = list(set(list(charectors)))
        for i in range(limit):
            word = ""
            for ii in range(random.randint(min,max)):
                random.shuffle(char)
                word=word+str(char[0])
            yield word

    def BrutForce(self,my_str,min,max):
        for i in range(min,max+1):
            for w in product(my_str,repeat=i):
                word = "".join(w)
                yield word

    def Dictionay(self,file_name_or_path): # after update tested only garuda linux
        f = open(format_path(file_name_or_path),"rb")
        pass_list = f.readlines()
        f.close()
        for i in pass_list:
            detection = chardet.detect(i)
            encoding = detection["encoding"]
            try:
                yield i.decode(encoding).replace("\n","")
            except:pass




class Check_Key:

    def pdf_key(self,file_name_or_path,password):
        try:
            with pdfplumber.open(format_path(file_name_or_path),password=password) as pdf:
                return True
        except pdfplumber.pdfminer.pdfdocument.PDFPasswordIncorrect:
            return False

    def rar_key(self,file_name_or_path,password):
        f = RarFile(file_name_or_path)
        d = f.namelist()
        try:
            f.read(d[0],pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def zip_key(self,file_name_or_path,password):
        f = zipfile.ZipFile(file_name_or_path)
        d = f.filelist[0]
        try:
            f.read(d.filename,pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def ms_office_key(self,world_excel_powerpoint_rb_file_object,password):
        ms_f = msoffcrypto.OfficeFile(world_excel_powerpoint_rb_file_object)
        ms_f.load_key(password=str(password))
        try:
            ms_f.decrypt(io.BytesIO())
            return True
        except msoffcrypto.exceptions.InvalidKeyError:
            return False
    def hash_key(self,_hash,key,num):
        h = Hash_Genrator(key)
        if num == "1":
            if h.md5() == _hash:
                return True
            else:
                return False
        elif num =="2":
            if h.sha1() == _hash:
                return True
            else:
                return False
        elif num =="3":
            if h.sha224() == _hash:
                return True
            else:
                return False
        elif num =="4":
            if h.sha256() == _hash:
                return True
            else:
                return False
        elif num =="5":
            if h.sha384() == _hash:
                return True
            else:
                return False
        elif num =="6":
            if h.sha512() == _hash:
                return True
            else:
                return False
        elif num =="7":
            if h.blake2b() == _hash:
                return True
            else:
                return False
        elif num =="8":
            if h.blake2s() == _hash:
                return True
            else:
                return False



class Hash_Genrator:

    def __init__(self,str_input):
        self.hash_str = str_input 
    def md5(self):
        return hashlib.md5(self.hash_str.encode('utf-8')).hexdigest()
    def sha1(self):
        return hashlib.sha1(self.hash_str.encode('utf-8')).hexdigest()
    def sha224(self):
        return hashlib.sha224(self.hash_str.encode('utf-8')).hexdigest()
    def sha256(self):
        return hashlib.sha256(self.hash_str.encode('utf-8')).hexdigest()
    def sha384(self):
        return hashlib.sha384(self.hash_str.encode('utf-8')).hexdigest()
    def sha512(self):
        return hashlib.sha512(self.hash_str.encode('utf-8')).hexdigest()
    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode('utf-8')).hexdigest()
    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode('utf-8')).hexdigest()



class Darkforce:
    def __init__(self):
        self.gen = Genrator()
        self.key = Check_Key()
        #------------------------------colors-----------
        self.red = colorama.Fore.RED
        self.yellow = colorama.Fore.YELLOW
        self.blue = colorama.Fore.BLUE
        self.green = colorama.Fore.GREEN
        self.reset = colorama.Fore.RESET

        self.bright = colorama.Style.BRIGHT
        self.dim = colorama.Style.DIM
        self.normal = colorama.Style.NORMAL
        self.reset_all = colorama.Style.RESET_ALL
        #-----------------------------------------------

        self.intro = f"""
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀  █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░ ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░  ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
   ░          ░  ░   ░     ░  ░              ░ ░     ░     ░ ░         ░  ░
 ░                                                         ░                                                 
        {self.green}DarkForce{self.yellow} {self.green}Breaching the Unbreakable
        Author - ({self.blue} Riya Mishra{self.green}){self.reset_all}
        """
    def pass_found(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_wotch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,---------------------------------{style}{style2}----------------,
        |   {self.green}Password Found :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}Password : {self.red}[{self.green}{key}{self.red}]   |
        '---------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def dic_genrated(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_wotch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,--------------------------------------{style}{style2}----------------,
        |   {self.green}Dictionary Generated :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}File Saved : {self.red}[{self.green}{key}{self.red}]   |
        '--------------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def clear(self):
        os.system("clear")
    def stop_wotch(self,start_time):
        tt = time.time() - start_time 
        mins= tt // 60
        sec = tt % 60
        hours = mins // 60
        mins = mins % 60 
        return int(hours),int(mins),int(sec)

    def dic_gen_show(self):
        while self.th_stop:
            for i in ["\\","|","/","-"]:
                time.sleep(0.4)
                dot = i*3#!/usr/bin/python3
import hashlib,os,pdfplumber,colorama,time,random,zipfile,msoffcrypto,io,threading,chardet
from itertools import product
from rarfile import RarFile

class Genrator:
    def Random(self,charectors,min,max,limit):
        char = list(set(list(charectors)))
        for i in range(limit):
            word = ""
            for ii in range(random.randint(min,max)):
                random.shuffle(char)
                word=word+str(char[0])
            yield word

    def BrutForce(self,my_str,min,max):
        for i in range(min,max+1):
            for w in product(my_str,repeat=i):
                word = "".join(w)
                yield word

    def Dictionay(self,file_name_or_path):
        f = open(format_path(file_name_or_path),"rb")
        pass_list = f.readlines()
        f.close()
        for i in pass_list:
            detection = chardet.detect(i)
            encoding = detection["encoding"]
            try:
                yield i.decode(encoding).replace("\n","")
            except:pass




class Check_Key:

    def pdf_key(self,file_name_or_path,password):
        try:
            with pdfplumber.open(format_path(file_name_or_path),password=password) as pdf:
                return True
        except pdfplumber.pdfminer.pdfdocument.PDFPasswordIncorrect:
            return False

    def rar_key(self,file_name_or_path,password):
        f = RarFile(file_name_or_path)
        d = f.namelist()
        try:
            f.read(d[0],pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def zip_key(self,file_name_or_path,password):
        f = zipfile.ZipFile(file_name_or_path)
        d = f.filelist[0]
        try:
            f.read(d.filename,pwd=str(password).encode())
            f.close()
            return True
        except:
            f.close()
            return False

    def ms_office_key(self,world_excel_powerpoint_rb_file_object,password):
        ms_f = msoffcrypto.OfficeFile(world_excel_powerpoint_rb_file_object)
        ms_f.load_key(password=str(password))
        try:
            ms_f.decrypt(io.BytesIO())
            return True
        except msoffcrypto.exceptions.InvalidKeyError:
            return False
    def hash_key(self,_hash,key,num):
        h = Hash_Genrator(key)
        if num == "1":
            if h.md5() == _hash:
                return True
            else:
                return False
        elif num =="2":
            if h.sha1() == _hash:
                return True
            else:
                return False
        elif num =="3":
            if h.sha224() == _hash:
                return True
            else:
                return False
        elif num =="4":
            if h.sha256() == _hash:
                return True
            else:
                return False
        elif num =="5":
            if h.sha384() == _hash:
                return True
            else:
                return False
        elif num =="6":
            if h.sha512() == _hash:
                return True
            else:
                return False
        elif num =="7":
            if h.blake2b() == _hash:
                return True
            else:
                return False
        elif num =="8":
            if h.blake2s() == _hash:
                return True
            else:
                return False



class Hash_Genrator:

    def __init__(self,str_input):
        self.hash_str = str_input 
    def md5(self):
        return hashlib.md5(self.hash_str.encode('utf-8')).hexdigest()
    def sha1(self):
        return hashlib.sha1(self.hash_str.encode('utf-8')).hexdigest()
    def sha224(self):
        return hashlib.sha224(self.hash_str.encode('utf-8')).hexdigest()
    def sha256(self):
        return hashlib.sha256(self.hash_str.encode('utf-8')).hexdigest()
    def sha384(self):
        return hashlib.sha384(self.hash_str.encode('utf-8')).hexdigest()
    def sha512(self):
        return hashlib.sha512(self.hash_str.encode('utf-8')).hexdigest()
    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode('utf-8')).hexdigest()
    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode('utf-8')).hexdigest()



class Darkforce:
    def __init__(self):
        self.gen = Genrator()
        self.key = Check_Key()
        #------------------------------colors-----------
        self.red = colorama.Fore.RED
        self.yellow = colorama.Fore.YELLOW
        self.blue = colorama.Fore.BLUE
        self.green = colorama.Fore.GREEN
        self.reset = colorama.Fore.RESET

        self.bright = colorama.Style.BRIGHT
        self.dim = colorama.Style.DIM
        self.normal = colorama.Style.NORMAL
        self.reset_all = colorama.Style.RESET_ALL
        #-----------------------------------------------

        self.intro = f"""  
▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀  █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░ ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░  ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
   ░          ░  ░   ░     ░  ░              ░ ░     ░     ░ ░         ░  ░
 ░                                                         ░                      
{self.green}DarkForce{self.green}Breaching the Unbreakable  
        Git link - https://github.com/Riya73/darkforce.git                
        Author - ({self.blue} Riya Mishra{self.green}){self.reset_all}
        """
    def pass_found(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_wotch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,---------------------------------{style}{style2}----------------,
        |   {self.green}Password Found :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}Password : {self.red}[{self.green}{key}{self.red}]   |
        '---------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def dic_genrated(self,target,key,obj_time_time):
        main.clear()
        print(self.intro)
        style = "-"*len(key)
        style2 = "-"*len(target)
        hours,mins,sec = main.stop_wotch(obj_time_time)
        time_len = "-"*len(f"{hours}{mins}{sec}")
        show_key = f"""{self.bright}{self.red}
        ,-----------{time_len}---------------,
        |     {self.green}Time:   {self.red}[{self.green}{hours}{self.red}:{self.green}{mins}{self.red}:{self.green}{sec}{self.red}]         |
        '---------------{time_len}-----------'{self.bright}{self.red}
        ,--------------------------------------{style}{style2}----------------,
        |   {self.green}Dictionary Generated :  {self.blue}Target : {self.red}[{self.green}{target}{self.red}] {self.blue}File Saved : {self.red}[{self.green}{key}{self.red}]   |
        '--------------------------------------{style}{style2}----------------'
        {self.reset_all}
        """
        print(show_key)
    def clear(self):
        os.system("clear")
    def stop_wotch(self,start_time):
        tt = time.time() - start_time 
        mins= tt // 60
        sec = tt % 60
        hours = mins // 60
        mins = mins % 60 
        return int(hours),int(mins),int(sec)

    def dic_gen_show(self):
        while self.th_stop:
            for i in ["\\","|","/","-"]:
                time.sleep(0.4)
                dot = i*3
                print()
                print(f"\033[A{self.bright}{self.red}Generating{dot} {self.reset_all}\033[A")
    def trying(self,key,obj_time_time):
        hours,mins,sec = main.stop_wotch(obj_time_time)
        key_len = " "*int(20-len(key))
        print()
        print(f"\033[A{self.bright}{self.red}Trying [{self.green}{key}{self.red}]{key_len}[{self.blue}{hours}:{mins}:{sec}{self.red}] [{self.blue}Ctrl+C for Kill{self.red}]{self.reset_all}\033[A")
    def my_start(self):
        main.clear()
        print(self.intro)
        print(f"{self.blue}Select {self.red}[1]{self.blue} BruteForce {self.red}[2]{self.blue} Dictionary {self.red}[3]{self.blue} Random {self.red}[0]{self.blue} Exit")
        commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force~#{self.reset_all} ")
        if commands =="0":
            print(f"{self.bright}{self.green}Thank You For Using :){self.reset_all}")
            exit()
        #===================================================================================================================================================================================================================================    
        elif commands == "1":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/BruteForce~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "4":
                b_ms_f =input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        b_ms.close()
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                b_ms.close()
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,str(i),hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "6":
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_path = input(f"{self.red}Input File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                b_list = open(format_path(b_path),"w")
                th = threading.Thread(target=main.dic_gen_show)
                self.th_stop = True
                th.start()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    b_list.write(str(i)+"\n")
                b_list.close()
                self.th_stop = False
                time.sleep(2)
                main.dic_genrated(b_str,b_path,start_time)
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

        #=================================================================================================================================================================================================================================== 

        elif commands == "2":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/Dictionary~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "4":
                b_ms_f = input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,i,hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

        #=================================================================================================================================================================================================================================== 

        elif commands == "3":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/Random~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()
            
            elif b_commands == "4":
                b_ms_f = input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,str(i),hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "6":
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                b_path = input(f"{self.red}Input File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                b_list = open(format_path(b_path),"w")
                th = threading.Thread(target=main.dic_gen_show)
                self.th_stop = True
                th.start()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                      b_list.write(str(i)+"\n")
                b_list.close()
                self.th_stop = False
                time.sleep(2)
                main.dic_genrated(b_str,b_path,start_time)
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()
        #=================================================================================================================================================================================================================================== 












if __name__ == "__main__":
    while True:
        try:
            main = Darkforce()
            main.my_start()
        except KeyboardInterrupt:
            pass
        print()
        print(f"\033[A{self.bright}{self.red}Genrating{dot} {self.reset_all}\033[A")
    def trying(self,key,obj_time_time):
        hours,mins,sec = main.stop_wotch(obj_time_time)
        key_len = " "*int(20-len(key))
        print()
        print(f"\033[A{self.bright}{self.red}Trying [{self.green}{key}{self.red}]{key_len}[{self.blue}{hours}:{mins}:{sec}{self.red}] [{self.blue} Ctrl+C for Kill{self.red}]{self.reset_all}\033[A")
    def my_start(self):
        main.clear()
        print(self.intro)
        print(f"{self.blue}Select {self.red}[1]{self.blue} BruteForce {self.red}[2]{self.blue} Dictionary {self.red}[3]{self.blue} Random {self.red}[0]{self.blue} Exit")
        commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force~#{self.reset_all} ")
        if commands =="0":
            print(f"{self.bright}{self.green}Thank You For Using :){self.reset_all}")
            exit()
        #===================================================================================================================================================================================================================================    
        elif commands == "1":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/BruteForce~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "4":
                b_ms_f =input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        b_ms.close()
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                b_ms.close()
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,str(i),hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "6":
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_path = input(f"{self.red}Input File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                b_list = open(format_path(b_path),"w")
                th = threading.Thread(target=main.dic_gen_show)
                self.th_stop = True
                th.start()
                for i in self.gen.BrutForce(b_str,b_min,b_max):
                    b_list.write(str(i)+"\n")
                b_list.close()
                self.th_stop = False
                time.sleep(2)
                main.dic_genrated(b_str,b_path,start_time)
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

        #=================================================================================================================================================================================================================================== 

        elif commands == "2":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/Dictionary~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "4":
                b_ms_f = input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_dic = input(f"{self.red}Input Dictionary File Path or Name >>{self.reset_all}")
                start_time = time.time()
                for i in self.gen.Dictionay(b_dic):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,i,hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

        #=================================================================================================================================================================================================================================== 

        elif commands == "3":
            print(f"{self.blue}Select {self.red}[1]{self.blue} PDF {self.red}[2]{self.blue} RAR {self.red}[3]{self.blue} ZIP {self.red}[4]{self.blue} MS_Office")
            print(f"{self.blue}       {self.red}[5]{self.blue} Hash {self.red}[6]{self.blue} Generate Dictionary {self.red}[0]{self.blue} Exit{self.reset_all}")
            b_commands = input(f"{self.bright}{self.red}Dark{self.green}@{self.red}Force/Random~#{self.reset_all} ")
            if b_commands == "1":
                b_pdf = input(f"{self.red}Input PDF File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.pdf_key(b_pdf,i) == True:
                        main.pass_found(b_pdf,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "2":
                b_rar = input(f"{self.red}Input RAR File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.rar_key(b_rar,i) == True:
                        main.pass_found(b_rar,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "3":
                b_zip = input(f"{self.red}Input zip File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.zip_key(b_zip,str(i)) == True:
                        main.pass_found(b_zip,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()
            
            elif b_commands == "4":
                b_ms_f = input(f"{self.red}Input (Excel,World,PowerPoint) File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                b_ms = open(b_ms_f,"rb")
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.ms_office_key(b_ms,str(i)) == True:
                        main.pass_found(b_ms_f,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "5":
                b_hash =input(f"{self.red}Input Encrypted Hash String >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                hash_type = input(f"{self.red}Select [1]MD5 [2]SHA1 [3]SHA224 [4]SHA256 [5]SHA384 [6]SHA512 [7]BLAKE2B [8]BLAKE2S Type >>{self.reset_all}")
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                start_time = time.time()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                    main.trying(i,start_time)
                    if self.key.hash_key(b_hash,str(i),hash_type) == True:
                        main.pass_found(b_hash,i,start_time)
                        break
                    else:
                        pass
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()

            elif b_commands == "6":
                b_str = input(f"{self.red}Input Characters >>{self.reset_all}")
                b_min = int(input(f"{self.red}Input Min Length Password >>{self.reset_all}"))
                b_max = int(input(f"{self.red}Input Max Length Password >>{self.reset_all}"))
                b_limit = int(input(f"{self.red}Input Limit of Password >>{self.reset_all}"))
                b_path = input(f"{self.red}Input File name or path >>{self.reset_all}").replace("'","").replace('"',"").lstrip().rstrip()
                start_time = time.time()
                b_list = open(format_path(b_path),"w")
                th = threading.Thread(target=main.dic_gen_show)
                self.th_stop = True
                th.start()
                for i in self.gen.Random(b_str,b_min,b_max,b_limit):
                      b_list.write(str(i)+"\n")
                b_list.close()
                self.th_stop = False
                time.sleep(2)
                main.dic_genrated(b_str,b_path,start_time)
                input(f"{self.green}Press Enter to go back to the main menu #{self.reset_all}")
                main.my_start()
        #=================================================================================================================================================================================================================================== 












if __name__ == "__main__":
    while True:
        try:
            main = Darkforce()
            main.my_start()
        except KeyboardInterrupt:
            pass
