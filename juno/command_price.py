from telegram import Update
import time
from time import sleep
from data import get_price, get_apr, get_circulating_supply, get_juno_liquidity, get_total_volume


def start(update: Update, context):
    price = get_price()
    message = f"""
🎰️ Juno Price : $ {price:.2f}
📈 Delegation APR: {get_apr():.2f}%
🏦 Market Cap : $ {price * get_circulating_supply() / 1_000_000:.2f} M
♻️  Circulating Supply: {get_circulating_supply():,.0f} Juno
💧 Total liquidity (Osmosis): $ {get_juno_liquidity():,.0f}
💰 24h volume (Osmosis ): $ {get_total_volume():,.0f}
For more information follow our [Grafana board](https://monitor.bronbro.io/d/juno-stats)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
Powered by [Bro_n_Bro](https://twitter.com/Bro_n_Bro)
    """
    post_and_delete = context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown', disable_web_page_preview=True)
    time.sleep(15)
    context.bot.delete_message(chat_id=update.message.chat.id, message_id=post_and_delete.message_id)
    context.bot.delete_message(chat_id=update.message.chat.id, message_id=update.message.message_id)
