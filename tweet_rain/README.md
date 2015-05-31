# tweet rain

These are Nebri instances working to tweet rain-related weather information using feeds
from Yahoo! Weather on top of [yweather] [1] and [twitter] [2] Python packages.

  [1]: https://pypi.python.org/pypi/yweather "yweather Python package"
  [2]: https://pypi.python.org/pypi/twitter "twitter Python package"

yweather scripts
================
The first script `yweather_scrapper` is for getting weather info based-on location. I then
make **Nebri drips** for two locations of my interest where I commute and live, the city of
Jakarta and Bogor. These drips are set each to every 3 hours and every 3 hours 35 minutes.

Second script `yweather_forecast` is for getting forecast of weather instead. I also then
make **Nebri drips** for the same two locations, but setting them to two times a day (morning
and evening).
