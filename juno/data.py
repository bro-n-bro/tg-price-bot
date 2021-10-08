import requests


def get_price() -> float:
    return requests.get('https://api-osmosis.imperator.co/tokens/v1/price/JUNO', timeout=30).json()['price']


def get_supply() -> int:
    res = requests.get(url='LCD_ENDPOINT/cosmos/bank/v1beta1/supply', timeout=30).json()
    data =  res['supply']
    for i in data:
      if  i['denom'] == 'ujuno':
         return int(i['amount'])

def get_inflation() -> float:
    res = requests.get(url='LCD_ENDPOINT/cosmos/mint/v1beta1/inflation',timeout=30).json()
    return float(res['inflation'])


def get_bonded_tokens() -> int:
    res = requests.get(url='LCD_ENDPOINT/cosmos/staking/v1beta1/pool',timeout=30).json()
    return int(res['pool']['bonded_tokens'])


def get_circulating_supply() -> float:
    res = requests.get(url='/', timeout=30).json()
    return float(res['circulatingSupply'])


def get_apr() -> float:
    supply = get_supply()
    inflation = get_inflation()
    bonded_tokens = get_bonded_tokens()
    return supply * inflation / bonded_tokens * 100
 
def get_osmo_juno_liquidity() -> int:
    res = requests.get(url='https://api-osmosis.imperator.co/pools/v1/497',timeout=30 ).json()
    return float(res[0]['liquidity'])

def get_atom_juno_liquidity() -> int:
    res = requests.get(url='https://api-osmosis.imperator.co/pools/v1/498',timeout=30 ).json()
    return float(res[0]['liquidity'])

def get_juno_liquidity() -> int:
    osmo_juno_liquidity = get_osmo_juno_liquidity()
    atom_juno_liquidity = get_atom_juno_liquidity()
    return osmo_juno_liquidity + atom_juno_liquidity

def get_total_volume() -> int:
    res = requests.get(url='https://api-osmosis.imperator.co/tokens/v1/all',timeout=30 ).json()
    return float(res[4]['volume_24h']) 
