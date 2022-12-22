import os

if __name__ == '__main__':
    print('*' * 80)
    print(os.environ)
    print('*' * 80)
    print(os.environ['GITHUB_TOKEN'])
    print('*' * 80)
    print(os.environ['GITHUB_REPOSITORY_OWNER'])
    print('*' * 80)
    print(os.environ['GITHUB_REPOSITORY'].split('/')[1])
    print('*' * 80)
    print(os.environ['GITHUB_REPOSITORY_NAME'])
