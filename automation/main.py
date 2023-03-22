# this file is only for testing the classes

import NotificationSender as NotificationSender
import user_data as ud
import sys
import emoji

if len(sys.argv) < 2 or not (sys.argv[1] == 'P' or sys.argv[1] == 'S' or sys.argv[1] == 'B'):
    print("The first command line argument should be P, S or B. Exiting.")
    sys.exit()

tier = sys.argv[1]

def get_users_in_tier(tier):
    return set(filter(lambda row: row.tier == tier, user_pref_table))

def get_users_sms(rows):
    return set(filter(lambda row: row.sms_noti, rows))

def get_users_email(rows):
    return set(filter(lambda row: row.email_noti, rows))

user_pref_table = ud.User_Preferences_Table().getData()
users_in_tier = get_users_in_tier(tier)

users_for_email = get_users_email(users_in_tier)
users_for_sms = get_users_sms(users_in_tier)

for user in users_for_email:
    print(user)
    noti_sender = NotificationSender.NotificationSender(user, 'not implemented')
    noti_sender.send_mail('This is a test massage', 'This is an automated message using cron.\n\rFinally working!')


