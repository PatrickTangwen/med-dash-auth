## Instructions for Running the Authentication System Locally
If you haven't install Node.js in your computer,please download it from the following url:<br>
[Node.js](https://nodejs.org/en/download)

1. Open your terminal<br> 
2. Navigate to the main directory by typing the following command:<br>
```cd med-dash-integration```
3. Install the necessary dependencies:<br>
```npm install```
4. Start the backend server:<br>
```npm run dev```
5. After starting the frontend server, you will see the URL of the local host displayed in the terminal.<br>
6. Copy and paste this URL into your web browser's address bar.<br>
7. You should now be able to access and interact with the login system locally in your browser.
8. As for now, the username and password are fixed. Please use ```13800000002``` for username and ```246810``` for the password.

## Instructions for Running ETL File
1. Navigate to the ETL directory by typing the following command:<br>
```cd med-dash-integration```<br>
```cd vital_data_etl```<br>

2. Install any necessary packages:<br>
```pip install -r requirements.txt```

3. Run the run.py to download csv files from vital:<br>
```python run.py```

4. You should be able to find all csv files in folder called "vital_csvs"

## Instructions for Running AWS Locally

1. Navigate to the repository directory: <br>
```cd med-dash-integration```<br>

2. Use the following commands to gain access to the AWS server:<br>
``` chmod 0400 med_dash.pem ``` <br>
``` ssh -i med_dash.pem ubuntu@54.214.106.120 -L xxxx:localhost:xxxx ``` <br>
(If you are Windows user and have issue with the command above, then try to use the follwoing command)
```sudo ssh -i med_dash.pem ubuntu@54.214.106.120 -L xxxx:localhost:xxxx ``` <br>```
(Make sure the file name is **"med_dash.pem"** with **"pem"** extension instead of other file extension)<br>
You should replace **xxxx** by **<any 4-digit-number>** for both **xxxx** to avoid using the same port number.

4. In the same terminal, use the following commands to connect to the Jupyter notebook:<br>
``` source venv/bin/activate ``` <br>
``` jupyter notebook --port=<same 4-digit-number you have placed above> ```<br>
After executing these commands, you will see the following response:<br>
![image](https://github.com/PatrickTangwen/med-dash-integration/assets/102566928/ccc26df0-97e3-444e-9300-613a13ac4d0f)

5. Copy the URL displayed at the bottom:<br>
For example, the URL displayed at the bootom of the screenshot is:<br>
```http://localhost:1112/lab?token=3dfe77414fa7c9d8683eb806ff737a8d89eac2c78b1659fc``` <br>
(You should have a different URL as you use different port number)

6. Open a new browser tab and paste the URL into the address bar, and you should now be able to access the Jupyter notebook.<br>
