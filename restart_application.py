import paramiko
import send_notification

def restart_docker_container():
    print("Restarting the application...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh.connect(hostname='<server-ip>', username='root', key_filename='<public-ssh-key-path>')
    stdin, stdout, stderr = ssh.exec_command('docker start nginx')
    print(stdout.readlines())
    ssh.close()
    
    message = "Subject: APPLICATION RESTARTED!\nApplication restarted and now its up and running!"
    send_notification.send_gmail_notification(message)
    
    print("Application restarted successfully!")