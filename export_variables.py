import os

def export_envs():
    '''
    output:
        - prints environment varaible name and value 
    '''
    file = open('env.txt')
    for line in file:
        line_data = line.rstrip('\n')
        data_pieces = line_data.split('=')
        env_name = data_pieces[0]
        env_value = data_pieces[1]
        os.environ[env_name] = env_value
        print(env_name + " : " + os.environ.get(env_name))


if __name__ == "__main__":
    export_envs()
