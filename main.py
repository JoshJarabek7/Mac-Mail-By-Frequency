import mailbox
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog
from openpyxl import Workbook
from tkinter import messagebox

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
    wb = Workbook()
    ws = wb.active
    ws.append(['Sender Email Address', 'Alias', 'Message Count'])
    for sender, name, count in sender_counts_list:
        ws.append([sender, name, count])
    wb.save(output_file)
    messagebox.showinfo("Success!", "The file has been successfully processed!")


def select_file():
    mbox_file = filedialog.askopenfilename(initialdir="/", title="Select mbox file", filetypes=(("Mbox files", "*.mbox"), ("All files", "*.*")))
    output_file = filedialog.asksaveasfilename(initialdir="/", title="Save output file", defaultextension=".xlsx", filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    count_by_address(mbox_file, output_file)

def create_gui():
    root = tk.Tk()
    root.title("Mailbox Fixer")

    label = tk.Label(root, text="Select your mbox file and output file location.")
    label.pack(padx=10, pady=10)

    button = tk.Button(root, text="Select mbox file", command=select_file)
    button.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_gui()
