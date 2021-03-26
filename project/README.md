# CoronaInfo

The purpose of CoronaInfo app is to be updated on the current status of COVID-19 virus infection around the world. It also shows news associated with corona virus published in various popular newspaper.

The source code of this project can be found [here](https://github.com/amritoo/corona-info).

## Features

CoronaInfo shows latest information on corona virus. Specifically it does -

- Allow user to select and save home country.
- At start shows detailed latest information on selected home country and also global status.

![Home](https://github.com/amritoo/corona-info/blob/master/images/home.jpg)

- Can also show all other countries information on 'country' option. Also shows travel warning of the selected country.

![Country](https://github.com/amritoo/corona-info/blob/master/images/country.jpg)

- Show latest news on corona virus published on various newspaper and also gives the option to view the news using any browser.

![News](https://github.com/amritoo/corona-info/blob/master/images/news.jpg)

- Support light and dark mode.
- Save the latest data including news on the device so that one can view everything offline as well.

CoronaInfo updates data at launch-time. It saves all data retrieved from the api using an sqlite database. Then queries the database to find information and show it to users as required.

This is CS50.

## Technology used

1. Java
2. Sqlite
3. Android studio
4. Google material design

## Reference

- API from [Coronatracker](https://api.coronatracker.com/)
- App Icon image downloaded from [Vectorstock](https://www.vectorstock.com/) and edited using [Onlinejpgtools](https://onlinejpgtools.com/)
