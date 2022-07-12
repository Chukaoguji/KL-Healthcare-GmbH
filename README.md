# 
<h2 align="center">KL-Healthcare-GmbH</h2>

[![GitHub stars](https://img.shields.io/github/stars/maxKudi/KL-Healthcare-GmbH)](https://github.com/maxKudi/KL-Healthcare-GmbH/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/maxKudi/KL-Healthcare-GmbH)](https://github.com/maxKudi/KL-Healthcare-GmbH/network)
[![GitHub issues](https://img.shields.io/github/issues/maxKudi/KL-Healthcare-GmbH)](https://github.com/maxKudi/KL-Healthcare-GmbH/issues)
[![GitHub license](https://img.shields.io/github/license/maxKudi/KL-Healthcare-GmbH)](https://github.com/maxKudi/KL-Healthcare-GmbH/blob/master/LICENSE)

The [```KL-Healthcare-GmbH Project```](https://github.com/maxKudi/KL-Healthcare-GmbH/) Is an application written in Python that allows the user to enter a date and time, and displays a simple message for the booked time when the countdown is done. 

[![Download](https://img.shields.io/badge/download-dataset-f20a0a.svg?longCache=true&style=flat)](https://github.com/maxKudi/KL-Healthcare-GmbH/archive/master.zip)

## Performance 
Currently a 2D array was used as the data structure to mimic a database in as much as this 2D array can be increased to 1000, i would recommend [0 - 9] so as not to break some part of the code. The unit test code tests the values the user inputs.  

## Description - Example program flow

```
How much data do you want to enter? 3
Please enter a date: 12.07.2022 
Please enter a time: 16:00

Please enter a date: 12.07.2022
Please enter the time: 17:00

Please enter the date: 13.07.2022
Please enter the time: 07:00

Thank you very much. I will notify them!
...

The first date has been reached! (12.07.2022 - 16:00)
The second date has been reached! (12.07.2022 - 17:00)
The third date was reached! (13.07.2022 - 07:00)
```
