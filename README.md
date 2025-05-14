# Sense HAT Crypto Price Tracker

Sense HAT Crypto Price Tracker is a tool powered by [CoinGecko API](https://www.coingecko.com/en/api) for capturing the latest price action of select cryptocurrencies through candle stick charts displayed on an 8x8 LED sense HAT screen. Users navigate through the menu and charts using the joystick on the sense HAT. Each cryptocurrency has three different variations; Users can explore charts with candles representing 30 minutes, 4 hours, or 4 days.

## Features

* **Main menu**
  - Users are greeted with a menu displaying the coins available to track, represented by a colored square on the screen.
  - Moving the joystick will move a cursor in the same direction.

<div align='center'>
  <img src="./demo/menu.gif" alt="Demo of main menu" width="400" height="200" />
</div>
<p align='center'>
  <small>Main menu</small>
</p>

* **Candle stick chart**
  - Once a user clicks on a coin, a candle stick chart showing the latest activity is displayed.
  - By clicking the joystick again, they can rotate through the different chart variations.
  - User can return to the main menu by holding the joystick down.

<div align='center'>
  <img src="./demo/bitcoin_chart.gif" alt="Demo of bitcoin chart" width="400" height="200" />
</div>
<p align='center'>
  <small>Bitcoin chart</small>
</p>

## Usage

1. Connect to your Raspberry Pi and clone this repository on it.

2. Get a demo API key from [CoinGecko](https://docs.coingecko.com/v3.0.1/reference/setting-up-your-api-key) and add it to a `.env` with the label `API_KEY`. <ins>If you opt to get a pro API key instead</ins>, make sure you change the `headers` object in `chart.py` to this:

```js
headers = {
  'x_cg_pro_api_key': constants.API_KEY
}
```
3. Run the program with this command:

```bash
python app.py
```

## Notes

* Indicators representing which chart variation is currently displayed have been added but are not shown in the Bitcoin chart gif.
* Due to some demo API restrictions, there may be issues getting some charts to display.
* For now, once a user clicks a coin, the latest data is fetched and cached and never updated throughout the life of the program. 
