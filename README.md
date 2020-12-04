# Raspberry Pi Temperature Monitoring script

## Disclaimer

This quick script was for the most part taken from [Leonardo Gentile's Github repo](https://gist.github.com/LeonardoGentile). However I adapted it to run with a GMail account. I also added in this README the procedure to run it with a GMail account. 

## 1 - Setting up your GMail account

*tldr: Click the link, enable the connection from less secured apps*

First of all, you'll want your GMail account to be set up to authorize connections from less secured apps (understand, non Google apps). In order to do so, please click on the following link and enable the connection from less secured apps (that is, after logging in with the email account you'll send your mail from) : https://myaccount.google.com/lesssecureapps 

## 2 - Create a credentials .py file

*tldr: Create a file named gmail_cred.py in the same folder (or at least in a subfolder) as your script, add three variables: `email` and `passwd`, with the values being your email and your password, and finally `remail`, the value being the receiver's email address*

You do not want your Google credentials to be in the script, right ? Then we'll create another file where we'll store the script. Of course, you can always add other layers of complexity for security purposes, but that's not the goal here. So first of all, create a file named *gmail_cred.py*. **Don't forget this file needs to be in the same folder** (*can be in a subfolder though*) **as the one the script will be in**.

`nano gmail_cred.py`
```python
# Edit the strings below
email = 'your_email@gmail.com'
passwd = '/R4nd0m_GM4il*P4ssW0rd!'
remail = 'receiver_mail@address.com'
```

## 3 - Download the script

*tldr: In the same folder as your gmail_cred.py file, run the first two commands below*

Now we just need to download the script from github. Make sure you are in the same folder as your *gmail_cred.py* file, then run :
`curl -OL https://raw.githubusercontent.com/edaveau/raspberry-temperature-monitoring/main/temp_check.py`

Then place the correct rights on it :
`chmod 744 temp_check.py`

The file can now be executed. We just need to make sure it works as expected. To do this, we'll set the temperature the Raspberry will send the alert at to, say, 30°C (I suppose your Raspberry runs at about 40-45°C). This way, we'll get an alert (bear in mind that if you change the critical alert to 30°C for this test, the script will make your Raspberry shut down, and you want to avoid that).

`sed -i '8s/60/30/' temp_check.py`

Then, run the script

`python3 temp_check.py`

You should receive the email alerting you of your current temperature. If so, you can change the alert temperature back to 60 :

`sed -i '8s/30/60/' temp_check.py`

## 4 - Create a Cronjob

*tldr: Run the last two commands below*

Here, we'll schedule the script to check the temperature every hour. But you can change this interval while creating the cronjob :

`crontab -e`

Then paste the following at the bottom of the file :

`60 * * * * python3 ~/Scripts/temp_check.py`

Of course, you can change the 60 minutes time interval to whatever suits you best.