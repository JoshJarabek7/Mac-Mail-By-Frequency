import csv
import mailbox
from collections import defaultdict

def count_by_address(mbox_file, output_file):
    mbox = mailbox.mbox(mbox_file)
    sender_counts = defaultdict(lambda: ['', 0])
    for message in mbox:
        sender = message['From']
        split_email = sender.replace("\"", "")
        split_email = split_email.replace('>', "<").split('<')
        if len(split_email) > 1:
            sender_name = split_email[0].strip()
            sender_email = split_email[1].strip()
        else:
            sender_name = ""
            sender_email = split_email[0]
        sender_counts[sender_email][0] = sender_name
        sender_counts[sender_email][1] += 1
    sender_counts_list = [(k, v[0], v[1]) for k, v in sender_counts.items()]
    sender_counts_list.sort(key=lambda x: x[2], reverse=True)
    with open(output_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sender Email Address','Alias', 'Message Count'])
        for sender, name, count in sender_counts_list:
            writer.writerow([sender, name, count])


def friendly_ui():
    print("\n\n-----------Time to fix your mailbox!-----------\n\n")
    user_choice = input(
        ""
          "Have you exported your mailbox file and placed it in the mbox folder?\n"
          "1)\tYes\n"
          "2)\tNo\n"
        ""
        )
    print("\n\n-----------\n\n")
    if user_choice != "1":
        print("Please come back when you have that file on hand.")
        quit()
    