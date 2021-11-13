import requests

session = None
url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx'
city = ["陕西省", "西安市", ""]
cityCode = 610100
product = 1


def parse_params(params):
    url_params = '?'
    for key, value in params.items():
        url_params = url_params + str(key) + '=' + str(value) + '&'
    return url_params[:-1]


def get(data):
    global session, url
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
    result = None
    # while 1:
    #     try:
    #         result = session.get(url, headers=headers, timeout=2)
    #         print("text", result.text)
    #     except:
    #         continue
    #     else:
    #         # while 1:
    #         #     try:
    #         #         result = result.json()
    #         #     except:
    #         #         print(result.text)
    #         #         continue
    #         #     else:
    #         #         break
    #         result = result.json()
    #         break
    result = session.get(url, headers=headers, timeout=2).json()
    return result


def get_customer_list():
    data = {
        "act": "CustomerList",
        "city": city,
        "cityCode": cityCode,
        "product": product
    }
    result = get(data)
    return list(filter(lambda x: "莲湖区" in x["cname"], result["list"]))


def get_customer_product(customer_id):
    data = {
        "act": "CustomerProduct",
        "id": customer_id
    }
    product_list = get(data)["list"]
    result = list(filter(lambda x: "九价" in x["text"], product_list))
    return result["BtnLable"] != "暂未开始"


def get_customer_subscribe_date_all():
    for customer_item in customer_list:
        data = {
            "act": "GetCustSubscribeDateAll",
            "pid": product,
            "id": customer_item["id"],
            "month": "202112"
        }
        print(1)
        date_list = get(data)["list"]
        print("date", date_list)


if __name__ == '__main__':
    customer_list = get_customer_list()
    # customer_product = get_customer_product()
    get_customer_subscribe_date_all()
