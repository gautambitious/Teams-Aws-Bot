## Enhanced version to start the bot from AWS mobile app using EC2 or Auto Run from windows PC([Original](https://github.com/TobiasPankner/Teams-Auto-Joiner))

### Steps for EC2:
* Create EC2 windows and access it through RDP client.
* Enable file downloads using [this](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-windows-file-download-ie/)
* Download and Install Google Chrome and Python 3.x
* Download/Clone this repository
* Rename config.json.example to config.json
* Edit the config.json file using these [options](https://github.com/TobiasPankner/Teams-Auto-Joiner)
* Edit the credentials.py file if you want to recieve email updates for the Bot from your GMail account
* Download [AutoLogon](https://docs.microsoft.com/en-gb/sysinternals/downloads/autologon), extract and run it
* Double Click on run_this.bat file and You're done

##### You can now start and stop this instance from AWS app to start and stop the teams bot

If you want to run the bot normally, then follow steps on the PC([Original](https://github.com/TobiasPankner/Teams-Auto-Joiner)) Repo
