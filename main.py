import subprocess
import os
from mailbox_helper import count_by_address, friendly_ui


if __name__ == "__main__":
    friendly_ui()
    count_by_address("mbox/mbox", "csv/output.csv")
    csv_file_path = os.path.join(os.getcwd(), "csv/output.csv")
    subprocess.run(['open', csv_file_path])