import linode_api4
import time
import os
import send_notification

LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def restart_linode_server():
    print("Rebooting the server...")
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    server = client.load(linode_api4.Instance, '<linode-id>')
    server.reboot()
    
    while True:
        server = client.load(linode_api4.Instance, '<linode-id>')
        if server.status == 'running':
            time.sleep(30) # Wait 30 more seconds or a minute because sometimes even though status changes to running, server is not fully booted.
            message = "Subject: SERVER REBOOTED!\nLinode server rebooted and now its up and running."
            send_notification.send_gmail_notification(message)
            print("Server rebooted successfully!")
            break