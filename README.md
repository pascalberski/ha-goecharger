[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

# go-eCharger Integration for Home Assistant
A simple go-eCharger V1-api integration for Home Assistant

### Getting started
##### Installation via HACS
1. Go to your HACS-Integrations page (.../hacs/integrations)
2. Click on the three points in the top right corner
3. Click on Custom Repositories
4. Paste this url: https://github.com/pascalberski/ha-goecharger/
5. Select Integration and click on Add
6. Click on Install
7. Configure the integration as shown below and restart Home Assistant.

##### Manual installation
1. Download this repository
2. Go to the `custom_components` in your Home Assistant folder (it should be in the directory where the `configuration.yaml` can be found)
    - if the `custom_components` directory doesn't exist, create it
3. Copy the goecharger directory from the `custom_components` folder in the downloaded repository to the `custom_components` folder in your Home Assistant folder
4. Configure the integration as shown below and restart Home Assistant.


### Configuration
in `configuration.yaml`
```
goecharger:
  chargers:
    - id: 1
      name: Charger1
      host: ip/hostname
    - id: 2
      name: Charger2
      host: ip/hostname
```

### Available sensor
- state (`car`)
- allow charging (`alw`)
- total energy (`eto`)
- current sensor for each phase (`nrg`)
- voltage sensor for each phase (`nrg`)
- power sensor for each phase (`nrg`)
- total power sensor (`nrg`)




[integration_blueprint]: https://github.com/pascalberski/ha-goecharger
[buymecoffee]: https://www.buymeacoffee.com/pascalberski
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/pascalberski/ha-goecharger.svg?style=for-the-badge
[commits]: https://github.com/pascalberski/ha-goecharger/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/pascalberski/ha-goecharger/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/pascalberski/ha-goecharger.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Pascal%20Berski%20@pascalberski-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/pascalberski/ha-goecharger.svg?style=for-the-badge
[releases]: https://github.com/pascalberski/ha-goecharger/releases
[user_profile]: https://github.com/pascalberski
