[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

# go-eCharger Integration for Home Assistant

### Configuration
in configuration.yaml
```
goecharger:
  chargers:
    - id: 1
      name: Charger1
      host: ip/hosname
    - id: 2
      name: Charger2
      host: ip/hosname
```

### Available sensor
- state (car)
- allow charging (alw)
- total energy (eto)
- current sensor for each phase (nrg)
- voltage sensor for each phase (nrg)
- power sensor for each phase (nrg)
- total power sensor (nrg)




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
