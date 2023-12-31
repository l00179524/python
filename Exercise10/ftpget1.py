import ftplib

# Set the path  of the code
a = '/mirrors/ubuntu-cdimage/releases/22.04/release'
# What file that is suppose to be downloaded
filename = 'SHA256SUMS'
# Make the connections for  ftp 
ftp = ftplib.FTP("ftp.heanet.ie")
# do the login
ftp.login() 

ftp.cwd(a)
# get the file back
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# and finally exit 
ftp.quit()