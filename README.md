# Bring weather info directly into your terminal
## available on Linux and MacOS platforms
### **Prerequisites:** 
Python v3, Git

### **Installation:**
1. Clone the project in the home directory
```html
  cd ~/
  git clone https://github.com/razvanvancea/linux-cli-weather-script.git
```
2. Open the .bashrc file
```html
nano ~/.bashrc
```
3. Add the following aliases
```html
alias wb='python3 ~/linux-cli-weather-script/get_weather.py Bucharest'
alias weather='python3 ~/linux-cli-weather-script/get_weather.py' 
```
4. Save and close the file (e.g. for nano editor: CTRL+X, then press Y and Enter)
5. Use the following command to reload the .bashrc file
```html
source ~/.bashrc
```

### **How to use the scripts?**

Return the weather of **your chosen location** (it will always be the same location set in .bashrc) via CLI:
```html
wb
```

Return **specific location** weather via CLI (the location name needs to be _passed as argument_):
```html
weather Berlin
```

_NOTE: 'wb' and 'weather' are aliases. They can be replaced with any other names._

_NOTE: in the first alias, feel free to replace "Bucharest" with your desired location._
