from github import Github
import getpass
username = raw_input("Username: ")
pw = getpass.getpass()
# First create a Github instance:

# using username and password
g = Github(username, pw)
otherUser = g.get_user(raw_input("choose a user to list repositories: "))
# Then play with your Github objects:
for repo in otherUser.get_repos():
    print repo.name
