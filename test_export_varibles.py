import os
from export_variables import export_envs

def test_export_envs():
    export_envs()
    file = open('env.txt')
    for line in file:
        line_data = line.rstrip('\n')
        data_pieces = line_data.split('=')
        env_name = data_pieces[0]
        env_value = data_pieces[1]
        assert os.environ.get(env_name) == env_value
