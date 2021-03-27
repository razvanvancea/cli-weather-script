# These scripts make your life easier, automating regular CLI set of tasks
## **Docker and Zalenium scripts** - available on Linux and MACOS
### **Prerequisites:** 
Python v3, Docker, Git

### **Installation:**
1. Clone this project in your home directory
```html
  cd ~/
  git clone https://github.com/razvanvancea/cli-scripts.git
```
2. Open the .bashrc file
```html
nano ~/.bashrc
```
3. For LINUX users: Add the following aliases at the bottom of the file
```html
  alias sdocker='python3 ~/cli-scripts/linux/start_docker.py'
  alias szalenium='python3 ~/cli-scripts/linux/start_zalenium.py'
```
3. For MACOS users: Add the following aliases at the bottom of the file
```html
alias szalenium='python3 ~/cli-scripts/macos/start_zalenium.py'
```

_NOTE: 'sdocker' and 'szalenium' are only aliases. They can be renamed with any other shortcut names._

4. Save and close the file (e.g. for nano editor: CTRL+X, then press Y and Enter)
5. Reload the .bashrc file, using the following CLI command
```html
source ~/.bashrc
```

### **How to use the scripts?**

For _LINUX/MACOS_ users, to **start Zalenium** with a desired number of containers via CLI:
```html
szalenium 3
```
The above command will create 3 containers. If you do not pass the argument (3), a message asking for the number will be prompted in the terminal, waiting for your input (it accepts only numbers).

For _LINUX_ users, to **start Docker** via CLI:
```html
sdocker
```

It it will verify if the Docker daemon is already running. If so, it will notify you by a console message. Otherwise, it will start the docker service.

## **Get Weather from the CLI script** - available on Linux and MACOS

### **Prerequisites**
Python v3, Git

### **Installation**
The same as above, but the step no.3 requires adding to the .bashrc file the following commands.

```html
alias wb='python3 ~/cli-scripts/get_weather.py Bucharest'
alias weather='python3 ~/cli-scripts/get_weather.py' 
```

**Do not forget** to follow the 4th and 5th step as well.

_NOTE: 'wb' and 'weather' are aliases. They can be replaced with any other names._

_NOTE: in the first alias, feel free to replace "Bucharest" with your current location._

Return the weather of **your current location** (it will always be the same location set in .bashrc) via CLI:
```html
wb
```

Return the weather of a **specific location** via CLI (the location name needs to be _passed as argument_):
```html
weather Berlin
```

## **Schedule automatic shutdown script** - available on Linux

### **Prerequisites**
Python v2 or v3, Git

### **Installation**
The same as above, but the step no.3 requires adding to the .bashrc file the following commands.

```html
alias sd='python ~/cli-scripts/linux/shutdown_scheduler.py'
alias notsd='python ~/cli-scripts/linux/cancel_shutdown_scheduler.py'
```

**Do not forget** to follow the 4th and 5th step as well.

_NOTE: 'sd' is only an alias that can be replaced with any other name._

Usage via CLI:
```html
sd 45
```
In the above example, the computer will be automatically shutted down after 45 minutes.
The argument represents the number of minutes (e.g. 45). It accepts only numeric values, otherwise an error message will be thrown.

If you want to **cancel** the shutdown script, use the following CLI command:
```html
notsd
```

