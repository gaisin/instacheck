# Instacheck: fair Instagram giveaways random winner finder

This script will help you to fairly find winner in giveaways. Giveaways — instagram lotterys with certain conditions. Usually participants have to  
1. tag two of their friends in post's comment
2. like the post
3. subscribe to giveaway's author  
Script is selecting all users, who have met the conditions and select one random user from them. Of course, it select's only unique users, so if someone will post multiple comments, he will have same chances as if he posted one.

### How to install

Python 3 has to be already installed.  
  
After cloning the repository, use `pip` (or `pip3` in case of conflicts with Python 2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Firstly, you need an Instagram account. Put username and password to a .env file, check ```.env_example``` as example. Better not use you personal account, since it can be banned. After finishing with an account, you can run a script.  
  
Script has two required parameters: 
1. Link to the post, e.g. https://www.instagram.com/p/Bt28gc1hMCA/
2. Author's username, e.g. lauravevere
```
$ python main.py https://www.instagram.com/p/Bt28gc1hMCA/ lauravevere
python main.py https://www.insta
gram.com/p/Bt28snYnmMB/ rebecca_rose_stylist
2019-02-14 15:04:30,773 - INFO - Instabot Started
2019-02-14 15:04:32,514 - INFO - Logged-in successfully as 'kibersnatch'!
2019-02-14 15:05:51,860 - ERROR - Request returns 429 error!
2019-02-14 15:05:51,861 - WARNING - That means 'too many requests'. I'll go to s
leep for 5 minutes.
2019-02-14 15:12:17,762 - ERROR - Request returns 429 error!
2019-02-14 15:12:17,763 - WARNING - That means 'too many requests'. I'll go to s
leep for 5 minutes.
Getting followers of 49555342:  83%|███?| 19820/23772 [00:33<00:06, 627.67it/s]
Waiting 2.02 min. due to too many requests.
Getting followers of 49555342: 100%|███?| 23770/23772 [02:47<00:00, 141.53it/s]
The winner is bridt89, profile link: https://instagram.com/bridt89
2019-02-14 15:20:11,407 - INFO - Bot stopped. Worked: 20:33:53.495813
2019-02-14 15:20:11,408 - INFO - Total requests: 2299
```  
As the result you get the winner's username: bridt89.  
  
**Warning**  
Since the library simulates the user's input from a mobile device, the bot can take a pause for five minutes in case of a large number of requests. Don't worry about that.
