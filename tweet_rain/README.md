# tweet rain

These are Nebri instances working to tweet rain-related weather information using feeds
from Yahoo! Weather on top of [yweather] [1] and [twitter] [2] Python packages.

  [1]: https://pypi.python.org/pypi/yweather "yweather Python package"
  [2]: https://pypi.python.org/pypi/twitter "twitter Python package"

yweather processes
==================
The first script `yweather_scrapper` is for getting weather info based-on location. I then
make **Nebri drips** for two locations of my interest where I commute and live, the city of
Jakarta and Bogor. These drips are set each to every 3 hours and every 3 hours 35 minutes.

Second script `yweather_forecast` is for getting forecast of weather instead. I also then
make **Nebri drips** for the same two locations, but setting them to two times a day (morning
and evening).

Rain related codes that are used to filter the weather feeds are:
Code     Description
1     0     tornado
2     1     tropical storm
3     2     hurricane
4     3     severe thunderstorms
5     4     thunderstorms

6     11     showers
7     12     showers

8     21     haze
9     24     windy

10     26     cloudy
11     27     mostly cloudy (night)
12     28     mostly cloudy (day)

13     38     scattered thunderstorms
14     39     scattered thunderstorms
15     40     scattered showers

twitter processes
=================
The `twitter` scripts are only extensions to each `yweather` script, hence there are two. Pretty
basics.

unit test scripts
=================
For each process, there is unit test script for troubleshooting.
