# whatsapp-bot
## Automated Message sender for Whatsapp Web
### Instructions
---
1. Clone the github repository.<br>
    ```git clone <link>```
<br>
2. Install Selenium package for python.<br>
    ```pip install selenium```
<br>
3. Install [chromedriver](https://chromedriver.chromium.org/) for Google Chrome ([geckodriver](https://github.com/mozilla/geckodriver/releases), if using Firefox)<br>
Ensure, the driver is in $PATH of your system.<br>
4. Open the [script.py](./script.py) file and make necessary changes.<br>
(Explanatory comments are included)

### Note
---
There is a sleep timer of 15 seconds, in the script, to scan the QR code on web.whatsapp.com, when the script is run.<br>```time.sleep(15)```
<br>Increase it, if required.

