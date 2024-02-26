import requests

url = "http://127.0.0.1:8000/"

try:
    response = requests.get(url)
    # 检查请求是否成功（状态码为200）
    if response.status_code == 200:
        print("请求成功！")
        print("响应内容:")
        print(response.text)
    else:
        print("未能获取成功的响应。状态码:", response.status_code)
except requests.exceptions.RequestException as e:
    print("发生请求错误:", e)
