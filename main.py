import requests
import schedule
import send_notification
import restart_server
import restart_application
    
def monitor_application():
    try:
        response = requests.get('<server-url>')
        if response.status_code == 200:
            print("Application is up and running successfully!")
        else:
            print("Application is down. Fix it!")
            message = f"Subject: SITE DOWN!\nApplication returned {response.status_code}. Fix the issue! Restart the application"
            send_notification.send_gmail_notification(message)
            restart_application.restart_docker_container()
    except Exception as ex:
        print(f"Connection error")
        message = f"Subject: SITE DOWN!\nApplication not accessible"
        send_notification.send_gmail_notification(message)
        restart_server.restart_linode_server()
        restart_application.restart_docker_container()
    
schedule.every(5).seconds.do(monitor_application)

while True:
    schedule.run_pending()