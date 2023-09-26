# Emails-tracking
Using a tracking pixel for monitoring the opening of emails.

<b>For Learning Purposes only</b>


## The Idea
Spy pixels or tracker pixels are hyperlinks to remote image files in HTML email messages that staelthily monitor the recipent's activity upon downloading the associated pixel. They are commonly embedded in the HTML of an email as small, imperceptible, transparent graphic files. Spy pixels are commonly used in marketing.

[Click here](https://en.wikipedia.org/wiki/Spy_pixel) to learn more.


## The Steps
You need a running basic server to deploy this web application. Ubuntu 20.04 LTS is used in this deployment.

### Step 1
Make sure you have python>=3.8 and pip>=21.0.0 
- run `pip3 install -r requirements.txt`
- run `sudo apt-get update`
- run `sudo apt-get install apache2 libapache2-mod-wsgi-py3`

### Step 2
Clone this repository: `git clone https://github.com/skanosBH/Emails-tracking`

Change your working directory to `YOUR_Path/Emails-tracking/app`

Link the the app directory to site-root defined apache configuration: `sudo ln -sT YOUR_Path/Emails-tracking/app /var/www/html/app`

### Step 3
Add the following block below configuration to the `/etc/apache2/sites-enabled/000-default.conf`:
```
WSGIDaemonProcess app threads=5
WSGIScriptAlias / /var/www/html/app/flaskapp.wsgi
<Directory app>
    WSGIProcessGroup app
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
```
[Click here](https://jqn.medium.com/deploy-a-flask-app-on-aws-ec2-1850ae4b0d41) to read more about Deploying a flask app.

### Step 4
Restart the Web Server `systemctl restart apache2`

_Additional Informations:_
If you need to stop the apache server run `systemctl stop apache2` and if you need to start it again run `systemctl start apache2`.
In case of troubleshoots, check the error logs in `/var/apache2/logs/error.log`.


### Step 5
Install the Chrome plugin _HTML Editor for Gmail__ and add `<img src ="_VM's_IP_/first" height=1 width=1>` to your email or your web page.



## Results
When a user opens an email with the embedded spy pixel, the User-Agent string, timestamp, and IP Address are logged to the `Emails-tracking/spy_pixel_logs.txt` file.

You can use _https://temp-mail.org/_ to test the application with random temporary email addresses.
