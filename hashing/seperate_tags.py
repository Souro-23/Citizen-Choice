import re
def seperate_tags(tags):

    temp=re.split(' #| | #',tags)
    while '' in temp:
        temp.remove('')
    return temp;
