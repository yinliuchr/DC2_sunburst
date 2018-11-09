import json

with open("jbn", 'r') as load_f:
    ori = json.load(load_f)
    # print(ori)
print


# print()
# print(len(ori))
# a = ori[0]
# print(a)
# print(type(a))
# print(len(a['children']))
# b = str(a['user']) +'__'+ str(a['id'])
# print(type(b))


def dfs(post):
    res = {}
    if post['children']:
        pass
    else:
        res['size'] = 1
    res['name'] = str(post['user']) + '__' + str(post['id'])
    res['children'] = []
    for cd in post['children']:
        temp = find_post_upon_id(cd, ori)
        res['children'].append(dfs(temp))
    return res


def find_post_upon_id(id_num, source):
    for items in source:
        if items['id'] == id_num:
            return items
    return


a = ori[0]

print(dfs(a))

with open("data.json", 'w') as write_f:
    ori = json.dump(dfs(a), write_f)
