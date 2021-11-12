import requests

session = None


def parse_params(params):
    result = '?'
    for key, value in params.items():
        result = result + str(key) + '=' + str(value) + '&'
    return result[:-1]


def get(url, data):
    global session
    headers = {
        "Referer": "https://servicewechat.com/wx2c7f0f3c30d99445/91/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI "
                      "MiniProgramEnv/Windows WindowsWechat",
        "content-type": "text/plain; charset=utf-8",
    }
    if not session:
        session = requests.Session()
    url = url + parse_params(data)
    result = session.get(url, headers=headers)
    return result


def get_customer_list():
    result = None
    url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx'
    data = {
        "act": "CustomerList",
        "city": city,
        "cityCode": cityCode,
        "product": product
    }

    while 1:
        try:
            result = get(url, data).json()
        except:
            continue
        else:
            break
    return list(filter(lambda x: '莲湖区' in x['cname'], result['list']))


if __name__ == '__main__':
    city = ["陕西省", "西安市", ""]
    cityCode = 610100
    product = 1

    customer_list = get_customer_list()
    print(customer_list)
