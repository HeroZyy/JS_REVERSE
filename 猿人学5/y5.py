import requests
import execjs
import requests


def p(page):
    with open('y5.js', 'r', encoding='utf-8') as f:
        s = f.read()
        res = execjs.compile(s).call('get_config')
    url = f"https://match.yuanrenxue.cn/api/match/5?page={page}&m={res['m']}&f={res['f']}"
    # print(url)
    payload = {}
    headers = {
        'Cookie': f'sessionid=your_sessionid; m={res["r_m"]}; RM4hZBv0dDon443M={res["r_r"]};',
    }
    # print(headers)
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


arr = []
for i in range(1, 6):
    res = p(i).json()
    print(res['data'])
    arr.append([i['value'] for i in res['data']])
res_a = []
for i in arr:
    for j in i:
        res_a.append(j)

res_a.sort(reverse=True)
print(res_a)

sum = 0
for i in range(0,5):
    print(res_a[i])
    sum += res_a[i]
print(sum)

