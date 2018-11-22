import requests

def KG_View(entity):
    url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity
    sess = requests.get(url)  # 请求
    text = sess.text  # 获取返回的数据

    response = eval(text)  # 转为字典类型
    knowledge = response['data']

    nodes = []
    for avp in knowledge['avp']:
        if avp[1] == knowledge['entity']:
            continue
        node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
        nodes.append(node)
    links = []
    for i in range(len(nodes)):
        node = nodes[i]
        # node = str(node)
        # node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target').replace("'rela'", 'rela')
        links.append(node)
        print(node)
    print(links)
    return links

def mention2entity(mention):
    '''
    获取歧义关系
    :param mention:
    :return:
    '''
    url = 'https://api.ownthink.com/kg/ambiguous?mention={mention}'.format(mention=mention)
    sess = requests.get(url)
    text = sess.text
    entities = eval(text)  #转为字典类型
    print(entities)
    return entities


def question2info(question):
    '''
    问答
    :param questtion:
    :return:
    '''
    url = 'https://api.ownthink.com/bot?token=openbot&info={question}'.format(question=question)
    sess = requests.get(url)
    text = sess.text
    answer = eval(text)
    print(answer)
    return answer

if __name__ == '__main__':
    KG_View('习近平')

    mention2entity('泡泡糖')

    question2info("美国总统是谁？")