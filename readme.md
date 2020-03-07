# HW5:  twitter-summarizer-rest-service
## run the code
### requirements
clone this repository
```
https://github.com/BUEC500C1/twitter-summarizer-rest-service-szyszy315.git
```
Install all requirements by running
```
pip3 install -r requirements.txt
```
### run the code
```
python app.py
```
then you can click http://127.0.0.1:5000/ which will lead you to the website. You can input the twitter id here and there is a download page for you to download generated video <br>
![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-szyszy315/blob/master/ec500hw5_1.png)
![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-szyszy315/blob/master/ec500hw5_2.png.png)

### deployment
Created an aws instance of ubuntu 18.04 and copy all the code to it. The code now its running on aws. When i run the app in aws everyone can use the following url to get access to the web application: http://18.191.110.247/.
#### process of deployment
run this script to transfer all files to the instance:
```
scp -i /path/my-key-pair.pem /path/SampleFile.txt ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com:~
```
Connect to Your Linux Instance using an SSH Client:
```
ssh -i /path/my-key-pair.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
```
then run the app:
```
sudo python3 app.py
```
![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-szyszy315/blob/master/ec500hw5_3.png)
![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-szyszy315/blob/master/ec.png)

#### tips
Set host='0.0.0.0' and port=80 when run app on aws. If not you may come up with Unable to connect error.

###Test
Test the web app with Appium Python for Web Applications and AWS Device Farm
