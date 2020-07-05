## MeliBot

##### Prerequisites

The setups steps expect following tools installed on the system.

- Github
- Python 3.6 or above
- Flask
- ngrok
- Twilio

##### 1. Check out the repository

```bash
git clone git@github.com:levei-co/levei-bot.git
```

##### 2. Setup

Run the following commands to create and setup the database.

```bash
python3 -m venv levei-bot-venv
source levei-bot-venv/bin/activate
pip3 install -r requirements.txt
```

##### 3. Start the ngrok server

You can start the server using the command given below.

```bash
ngrok http 5000
```

##### 4. Start Bot

```bash
python main.py
```