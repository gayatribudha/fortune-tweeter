# Fortune Tweeter

This is a python application that tweets fortune quotes to Twitter.

The quotes category can be mentioned in the .env file. If not mentioned, fortune will randomly select category. For the list of all available fortune categories in your computer, run  

`ls /usr/share/fortune/`


> If the list does not display anything or fortune is not installed, install fortune in your computer.


> For Arch Linux, install as `sudo pacman -S fortune-mod`
For Ubuntu, install as `sudo apt install fortune`


All user API tokens for Twitter has to be saved at .env file.


### To run the application:
```
git clone https://github.com/gayatribudha/fortune-tweeter
cd fortune-tweeter
virtualenv venv
pip install -r requirements.txt

```
Create the .env file based on .env.example and set the respective values. 

```
cp .env.example .env
vim .env
```
Run the application as:
```
python app.py
```
