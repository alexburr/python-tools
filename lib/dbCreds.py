import sys

class dbCreds:
    uid_file_path: str = ''
    pwd_file_path: str = ''
    uid = ''
    pwd = ''

    def __init__(self, uid_file_path: str, pwd_file_path: str):
        self.uid_file_path = uid_file_path
        self.pwd_file_path = pwd_file_path

        creds_result = self.set_db_creds()

        if creds_result != 0:
            sys.exit('INVALID CREDENTIALS FILE')

    
    def set_db_creds(self) -> int:
        i = 0

        try:
            with open(self.uid_file_path) as uid_file:
                for uf_line in uid_file:
                    if i == 1:
                        return 1
                    self.uid = uf_line
                    i = i + 1        
            
            i = 0

            with open(self.pwd_file_path) as pwd_file:
                for pf_line in pwd_file:
                    if i == 1:
                        return 1
                    self.pwd = pf_line
                    i = i + 1
        except FileNotFoundError:
            return -1

        return 0
