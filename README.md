# Telegram Price Bot

![image](https://user-images.githubusercontent.com/89855562/136571388-930288ce-cba6-4a19-a87b-b6e68df7beff.png)


Create your bot, using BotFather, more information you can find [here](https://core.telegram.org/bots)
During creation, you will get bot token, you will need it to update [juno/bot.py] (https://github.com/bro-n-bro/tg-price-bot/blob/main/juno/bot.py)

We are using our private node api endpoints (LCD_ENDPOINTS), so we can't share them with you. You need to find public endpoints or run Juno node to get neccessary information for updating [juno/data.py](https://github.com/bro-n-bro/tg-price-bot/blob/main/juno/data.py)

After all required information will be on place - you can run juno price bot:

```
docker-compose up -d --build
```


