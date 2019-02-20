from instabot import Bot
import os
import re
import random
from dotenv import load_dotenv
import argparse


def get_tagged_users(comments, bot):
    mask = "@([a-zA-Z0-9._]{1,100})"
    tagged_users = []
    for comment in comments:
        tagged_usernames = re.findall(mask, comment['text'])
        real_usernames = [username for username in tagged_usernames if is_user_exists(username, bot)]
        if len(real_usernames) >= 2:
            tagged_users.append((str(comment['user_id']), comment['user']['username']))
    return tagged_users


def is_user_exists(username, bot):
    user_id = bot.get_user_id_from_username(username)
    if user_id is None:
        return False
    else:
        return True


def get_liked_users(media_id, users, bot):
    liked_users = []
    likers = bot.get_media_likers(media_id)
    for user_id, username in users:
        if user_id in likers:
            liked_users.append(user)
    return liked_users


def get_followed_users(username, users, bot):
    followed_users = []
    followers = bot.get_user_followers(username)
    for user_id, username in users:
        if user_id in followers:
            followed_users.append(user)
    return followed_users


def get_random_user(users):
    random_number = random.randint(0, len(users)-1)
    return users[random_number]


def main():
    parser = argparse.ArgumentParser(description='This is a Instagram giveaway '\
                                                 'winner checker.')
    parser.add_argument('post_link', help='Url of instagram post')
    parser.add_argument('username', help="Post's author's instagram username")
    args = parser.parse_args()
    post_link = args.post_link
    username = args.username

    load_dotenv()
    INSTA_USERNAME = os.getenv('INSTA_USERNAME')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')
    bot = Bot()
    bot.login(username=INSTA_USERNAME, password=INSTA_PASSWORD)
    media_id = bot.get_media_id_from_link(post_link)
    comments = bot.get_media_comments_all(media_id)
    tagged_users = get_tagged_users(comments, bot)
    unique_tagged_users = set(tagged_users)
    liked_users = get_liked_users(media_id, unique_tagged_users, bot)
    followed_users = get_followed_users(username, liked_users, bot)
    if followed_users:
        winner = get_random_user(followed_users)
        print('The winner is {}, profile link: https://instagram.com/{}'.format(
                                                            winner[1], 
                                                            winner[1]))
    else:
        print('No one met all the requirements')


if __name__ == '__main__':
    main()
