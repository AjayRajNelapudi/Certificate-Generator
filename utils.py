import json

def remove_empty_lists(obj):
    empty_list = []
    while empty_list in obj:
        obj.remove(empty_list)
    return obj

def format_config(filepath):
    with open(filepath) as email_config:
        config = json.load(email_config)
    return config