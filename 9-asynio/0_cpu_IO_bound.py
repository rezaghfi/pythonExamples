# I/O bound vs CPU-bound
import requests

#i/o bound : به خاطر اینکه یک درخواست در شبکه ارسال می شه و محدود به پهنای باند شبکه است
response = requests.get('https://github.com/rezaghfi')
#وابسته به پردازنده من است
items = response.headers.items()
#cpu
res_headers = [f"{key}: {value}" for key, value in items]
#cpu
formatted_headers = "\n".join(res_headers)
#i/o
with open("headers.txt", 'w') as file:
    file.write(formatted_headers)
