#!/usr/bin/env python36

####################################################################
# Yuval Matityahu                                                  #
#  version 1.1                                                     #
# 14.6.2018                                                        #
#                                                                  #
#  This script try to send email                                   #
#  The user have to give parmaters fo Sender,Recipient and nassage #
#                                                                  #
#   There are use with TRY and ECEPTION to catch an error          #
#   if the email didn't send
#################################################################### 


# Import smtplib for the actual sending function

import smtplib



# From == the sender's email address
# To == the recipient's email address
# msg == the message to be send to recipient

From = input("enter e-mail of sender :")
To = input("enter e-mail of recipient :")
msg = input("enter message to send to recipient :")

# Send the message via our own SMTP server.
try:
	s = smtplib.SMTP('smtp.gmail.com',586)
    s.send_message(From,To,msg)
    s.quit()
    print('Mail was seccesufuly sent')
except smtplib.SMTPException:
	print('An error - Cant send email {}:{}',format(errno,strerror))    


