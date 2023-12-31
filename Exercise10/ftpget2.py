import ftplib

FTP = {
    "a": '/mirrors/ubuntu-cdimage/releases/22.04/release',
    "FILENAME": 'SHA256SUMS',
    "URL": 'ftp.heanet.ie'
}

# Making the connection
ftp = ftplib.FTP(FTP['URL'])
# do the login 
ftp.login() 
# browse to the directory
ftp.cwd(FTP["PATH"])
# get the file back 
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()
