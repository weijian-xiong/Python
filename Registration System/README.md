# CGI Programming
## Description
Design a web registration system. It allows users to type personal information and store in the mysql database. After register successfully, the phone number users provided will automatically receive a message.

## Structure
```
$Your_Working_Directory 
        |
        +--- Registration-System
                 |
                 +----- Registration_System.html
                 |
                 +----- cgi-bin
                          | 
                          +----- home.py
                          |
                          +----- regist.py
                          |
                          +----- process.py
                          | 
                          +----- confirm.py
```
## Tool
`NGRok`: unzip from folder or download from [Here.](https://ngrok.com/)<br>
[Learn how to use NGRok](https://github.com/dwyl/learn-ngrok)<br>

## How to run
```
cd Path/to/Registration-System
cd cgi-bin
chmod a+x *.py
cd ..
python3 -m http.server --cgi
```
Server starts now, then open a new terminal:
```
./ngrok http 8000
```
You will see this:<br>
<img width="745" alt="1" src="https://user-images.githubusercontent.com/24274444/100442566-d64ef780-306d-11eb-938c-07b725e610e8.png">

Now go to browser type "127.0.0.1:8000" or "localhost:8000" to access localhost.<br>
Or you can access ngrok public URL.(In my case is " https://8bd22fe61cef.ngrok.io", your can find yours in the "Forwarding" row.）You can access this public address from any device.

<img width="612" alt="2" src="https://user-images.githubusercontent.com/24274444/100442568-d64ef780-306d-11eb-8fb8-97fb64a93021.png">
Click "Registration_System.html" to start.

<details><summary>Registration Step Screenshots</summary><p>
Registration System Home Page<br>
<img width="1010" alt="Screen Shot 2020-11-27 at 4 59 15 AM" src="https://user-images.githubusercontent.com/24274444/100442562-d51dca80-306d-11eb-98aa-5a33ed821d1a.png">
Fill out your information<br>
<img width="1010" alt="Screen Shot 2020-11-27 at 4 59 32 AM" src="https://user-images.githubusercontent.com/24274444/100442563-d51dca80-306d-11eb-9a77-0eb17b4fdb12.png">
<img width="1010" alt="Screen Shot 2020-11-27 at 4 59 41 AM" src="https://user-images.githubusercontent.com/24274444/100442564-d5b66100-306d-11eb-97f5-ea93df1cea44.png">
Information is correct.<br>
<img width="1010" alt="Screen Shot 2020-11-27 at 5 00 04 AM" src="https://user-images.githubusercontent.com/24274444/100442565-d5b66100-306d-11eb-8c68-5c2bac828fa6.png">
Information is not correct, need to register again.<br>
<img width="1010" alt="Screen Shot 2020-11-27 at 4 59 49 AM" src="https://user-images.githubusercontent.com/24274444/100442569-d6e78e00-306d-11eb-8c33-04edde26a36e.png">
Information store successfully.<br>
<img width="682" alt="database" src="https://user-images.githubusercontent.com/24274444/100442557-d3ec9d80-306d-11eb-8a6b-e18261f499cf.png">
    
After register successfully, you will receive this message.<br>
    
![SMS](https://user-images.githubusercontent.com/24274444/100442551-d3540700-306d-11eb-8fd6-16433403faa5.jpg)
</p></details>
