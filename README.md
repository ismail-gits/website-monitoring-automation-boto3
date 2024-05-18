# Website Monitoring Automation with Boto3

## Overview

The Website Monitoring Automation with Boto3 project is a Python-based system designed to monitor the health of a web application running on a server. It periodically checks the application's status and performs automated actions such as sending notifications and restarting services if the application is down.

## Features

- **Website Monitoring:** Regularly checks the status of the web application.
- **Automated Notifications:** Sends email notifications if the application is down.
- **Service Restarts:** Automatically restarts the application and the server when needed.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `schedule`
  - `paramiko`
  - `linode_api4`
  - `smtplib`
- A Linode account with API access.
- An SMTP server setup (e.g., Gmail) for sending notifications.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
   
2. **Install the required Python packages:**
    ```bash
    pip3 install requests schedule paramiko linode_api4
    ```

3. **Set up environment variables:**
    - `LINODE_TOKEN`: Your Linode API token.
    - `EMAIL_ADDRESS`: Your email address used for sending notifications.
    - `EMAIL_PASSWORD`: Your email password.


## Configuration

1. **Update the application URL in `monitor_application` function:**
    ```python
    response = requests.get('<server-url>')
    ```

2. **Update the server details in `restart_docker_container` function:**
    ```python
    ssh.connect(hostname='<server-ip>', username='root', key_filename='<public-ssh-key-path>')
    ```

3. **Update the Linode server ID in `restart_linode_server` function:**
    ```python
    server = client.load(linode_api4.Instance, '<linode-id>')
    ```
    or configure it for other cloud provider which you are using.

## Usage

1. **Run the monitor script:**
    ```bash
    python monitor_application.py
    ```

2. **The script will:**
    - Check the application status every 5 seconds.
    - Send a notification if the application is down.
    - Restart the application if it is not responding.
    - Reboot the server if it cannot be reached.

## Script Details
`monitor_application.py`
This script monitors the application's status and takes appropriate actions if the application is down.

- **Function: monitor_application()**
    - Checks if the application is up.
    - Sends a notification and restarts the application if it is down.
    - If there is a connection error, sends a notification, reboots the server, and restarts the application.
    
- **Function: restart_docker_container()**
    - Connects to the server via SSH.
    - Restarts the Docker container running the application.
    - Sends a notification after a successful restart.
    
- **Function: restart_linode_server()**
    - Reboots the Linode server.
    - Waits until the server is fully running.
    - Sends a notification after a successful reboot.

- **Function: send_gmail_notification()**
    - Sends an email notification using Gmail's SMTP server.