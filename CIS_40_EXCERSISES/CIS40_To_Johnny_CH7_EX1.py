# CIS 40 Johnny To Ch 7 Ex 1
# Error Log Parser
try:
    InFile = open("ErrorLog.txt","r")
    OutFile = open("ErrorLog.txt", "a")
    lineCount = 0
    errorCount = 0
    OutFile.write("===========ERROR LINES===========\n")
    for lines in InFile:
# Line count parser
        if lines == "\n":
            lineCount += 0
        else:
            lineCount += 1
# Error line parser
        if "ERROR" in lines.upper():
            errorCount += 1
            print (lines)
# Write error line
            OutFile.write(lines)
# Print line count and error count
    print("LINE COUNT:"+str(lineCount))
    OutFile.write("LINE COUNT:"+str(lineCount)+"\n")
    print("ERROR COUNT:"+str(errorCount))
    OutFile.write("ERROR COUNT:"+str(errorCount)+"\n")
    InFile.close()
    OutFile.close()
except:
    print("File not Found")
    InFile.close()
    OutFile.close()

'''
OUTPUT
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome

[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll

[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp

[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt

[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A

LINE COUNT:108
ERROR COUNT:5
'''