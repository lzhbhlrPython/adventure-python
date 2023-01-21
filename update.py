from git import *

repo = Repo('.')
repo.git.add('*.py')
#repo.git.add('*.md')
repo.git.commit('-m', 'update')
repo.git.push()
