[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/paypi/paypi-python">
    <img src="images/logo.png" alt="Logo" height="80">
  </a>

  <h3 align="center">PayPI Python Client</h3>

  <p align="center">
    Sell your API, today.
    <br />
    <a href="https://partner.paypi.dev/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://paypi.dev/">Homepage</a>
    ·
    <a href="https://github.com/paypi/paypi-python/issues">Report Bug</a>
    ·
    <a href="https://github.com/paypi/paypi-python/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

[![PayPI Screenshot][product-screenshot]](https://paypi.dev)

PayPI makes API creators' lives easier by handling API keys, user accounts, payments and more.
API users have one account to access all APIs using PayPI.

We worry about API authentication and payments so you can focus on making awesome APIs! This library enables you to interact with PayPI from a Python project.

<!-- GETTING STARTED -->

## Getting Started

> <a href="https://partner.paypi.dev/"><strong>See full documentation here</strong></a>

Install `paypi` from PyPI:

```sh
pip install paypi
# or
python -m pip install paypi
```

Then import it, create an instance with your private key and use it to authenticate and make charges against users:

```python
from paypi import PayPI

paypi = PayPI("<Your API Secret>")


@app.route("/")
async def hello():
    user = await paypi.authenticate("<Users Subscription Secret>")

    # do some work...

    await user.make_charge("<Charge ID>")
    # charge is now made...
```

In a synchronous environment you can also use the synchronous API calls. This cannot be done from an asyncio thread:

```python
paypi = PayPI("<Your API Secret>")
user = paypi.authenticate_sync("Users Subscription Secret")
user.make_charge_sync("<Charge ID>")
```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/paypi/paypi-python/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

All contributions are welcome. Please follow this workflow:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

All rights reserved.

<!-- CONTACT -->

## Contact

Alex - alex@paypi.dev  
Tom - tom@paypi.dev

Project Link: [https://github.com/paypi/paypi-python](https://github.com/paypi/paypi-python)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Paypi/paypi-python.svg?style=flat-square
[contributors-url]: https://github.com/paypi/paypi-python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Paypi/paypi-python.svg?style=flat-square
[forks-url]: https://github.com/paypi/paypi-python/network/members
[stars-shield]: https://img.shields.io/github/stars/Paypi/paypi-python.svg?style=flat-square
[stars-url]: https://github.com/paypi/paypi-python/stargazers
[issues-shield]: https://img.shields.io/github/issues/Paypi/paypi-python.svg?style=flat-square
[issues-url]: https://github.com/paypi/paypi-python/issues
[license-shield]: https://img.shields.io/github/license/Paypi/paypi-python.svg?style=flat-square
[license-url]: https://github.com/paypi/paypi-python/blob/master/LICENSE
[product-screenshot]: images/product.png
