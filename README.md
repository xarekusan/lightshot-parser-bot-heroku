![https://img.shields.io/badge/Status-Working-green](https://img.shields.io/badge/Status-Working-green)
![https://img.shields.io/badge/Python-3.9.1-blue](https://img.shields.io/badge/Python-3.9.1-blue)
# Lightshot Parser Bot on Heroku
**This bot is designed for parsing random photos from the site [prnt.sc](https://prnt.sc/). This will work on Heroku**
## Deploy to Heroku
### Prerequisites
In order for the bot to run on Heroku, we need to install the Heroku command line interface. If you are using Linux, you can do this as follows:
```
$ sudo add-apt-repository "deb https://cliassets.heroku.com/branches/stable/apt ./"  
$ curl -L https://cli-assets.heroku.com/apt/release.key |  
$ sudo apt-key add -  
$ sudo apt-get update  
$ sudo apt-get install heroku 
```
If you are using macOS or Windows, follow this [guide](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
### Installing
Using the following instructions, we will upload the bot to Heroku and launch it.
1. Open a command line and go to the directory where you want to clone repo.  
2. Use the following commands to clone the repo to your directory and move into the project directory:  
```
git clone https://github.com/xarekusan/lightshot-parser-bot-heroku.git
cd lightshot-parser-bot-heroku
```
3. Now let's create a Heroku application:
```
heroku login
heroku create
```
4. Set the config:
```
heroku labs:enable runtime-dyno-metadata
heroku config:set BOT_TOKEN=<your token>
```
5. Push the Bot to Heroku:
```
git push heroku main
```
If you did everything according to the instructions, the bot should have been successfully installed. Now we just need to start the bot with the following command:
```
heroku ps
```
**Congratulations! Bot is running**  
To view the logs, you can use the command:
```
heroku logs --tail
```
