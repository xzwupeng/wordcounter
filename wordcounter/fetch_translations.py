import urllib2, json, sys


def fetch_translations_from_file(file):
    trans_list = []
    with open(file) as f:
        for line in f:
            trans = fetch_translation(line.split(","))
            trans_list.append(trans)
    return trans_list


def fetch_translation(word):
    url = "http://dict.youdao.com/jsonresult?q={0}&keyfrom=deskdict.main&type=1&pos=-1&client=deskdict&id" \
          "=27ea057a1166e21b0&vendor=ynote.download&in=setup1_YoudaoDict_ynote.download&appVer=6.3.69.7015" \
          "&appZengqiang=0&abTest=5&le=eng&LTH=0".format(word)
    response = urllib2.urlopen(url)
    content = response.read()
    json_content = json.loads(content)
    # dict_content = {'basic': [], 'web': []}
    # for s in json_content['basic']:
    #     dict_content['basic'].append(unicode(s))
    # for s in json_content['web']:
    #     dict_content['web'].append(unicode(s))
    # return dict_content
    return json_content


def write_to_file(data, file='data1.txt'):
    f = open(file, 'w')
    for item in data:
        for field in item:
            f.write(str(field)+',')
        f.write('\n')


if __name__ == '__main__':
    # words_file = sys.argv[1]
    # print "fetching translations..."
    # translations = fetch_translations_from_file(words_file)
    # print "writing file"
    # write_to_file(translations)
    data = json.dumps(fetch_translation('windmill'), indent=4, ensure_ascii=False)
    print data
