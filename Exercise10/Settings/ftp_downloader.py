""""
FTP file downloader
Tested with Python >=3.6
By:  ishan
    v0.1    19dec23
"""
import ftplib
import settings.ftp as settings


ftp = ftplib.FTP(settings.FTP['URL'])
# Anonymous login
ftp.login() 

ftp.cwd(settings.FTP["a"])

ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()
