=== Giriş Yap ===
Kullanıcı adı: 1
Şifre: 1
Traceback (most recent call last):
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 198, in _new_conn
    sock = connection.create_connection(
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 445, in request
    self.endheaders()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 276, in connect
    self.sock = self._new_conn()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 213, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x00000235850B88E0>: Failed to establish a new connection: [WinError 10061] Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8080): Max retries exceeded with url: /login (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000235850B88E0>: Failed to establish a new connection: [WinError 10061] Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\PC\test-BLACK-F\z.py", line 103, in <module>
    main()
  File "C:\Users\PC\test-BLACK-F\z.py", line 91, in main
    login()
  File "C:\Users\PC\test-BLACK-F\z.py", line 32, in login
    r = requests.post(SERVER_URL + "/login", json={"username": username, "password": password})
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=8080): Max retries exceeded with url: /login (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000235850B88E0>: Failed to establish a new connection: [WinError 10061] Hedef makine etkin olarak reddettiğinden bağlantı kurulamadı'))
