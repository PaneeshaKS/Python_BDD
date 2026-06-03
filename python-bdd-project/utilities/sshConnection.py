import paramiko as paramikos
from utilities.configurations import *
import csv


# selcting the ssh client
ssh = paramikos.SSHClient()
# To connect the ssh client to the server
ssh.set_missing_host_key_policy(paramikos.AutoAddPolicy())
ssh.connect(
    hostname=get_ssh_connection()['host'],
    port=int(get_ssh_connection()['port']),
    username=get_ssh_connection()['username'],
    password=get_ssh_connection()['password']
)

# Run Commands
#stdin = take the input (like a asking for a password)
#stdout = output of the command and store that in the variable
#stderr = error output of the command and stored in the variable
stdin, stdout, stderr = ssh.exec_command("ls -a")
print(stdout.readlines())


########### Upload a file to the server ###########
sftp = ssh.open_sftp()  # Open an SFTP session
destination_path = "loanstatus.csv"  # Path on the server
source_path = r"tests\loanstatus.csv"  # Local path to the file
file_transfer = sftp(destination_path, source_path)  # Upload the file

######### Trigger the batch command ###########
stdin, stdout, stderr = ssh.exec_command("python script.py")  # Replace 'script.py' with your script name


####### Download a file from the server ###########
download_path = "downloaded_loanstatus.csv"  # Local path to save the downloaded file
destination_path = "loanstatus.csv"  # Path on the server
sftp.get(destination_path, download_path)  # Download the files




## to validate the data in the file (Parse the output) ####
with open("downloaded_loanstatus.csv", 'r') as file:
    data = csv.reader(file, delimiter=',')  # Read the lines from the downloaded file
    for row in data:
        if row[0] == '15324':
            assert row[1] == 'approved'
            print(f"Updated status for ID {row[0]} to {row[1]}")



sftp.close()  # Close the SFTP session

ssh.close()  # Close the SSH connection