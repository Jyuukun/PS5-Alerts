# PS5-Alerts

Get notified by email as soon as a PlayStation 5 becomes available at major French retailers!

## Features

-   Monitors PS5 stock at Amazon, Auchan, Boulanger, Carrefour, Cdiscount, Cultura, Darty, Fnac, Leclerc, and Micromania.
-   Sends an email alert when a PS5 is detected in stock.
-   Configurable email notification settings.
-   Simple, efficient, and easy to run.

## Requirements

-   Python 3.6+
-   [woob](https://woob.tech/) (Web Outside Of Browsers)
-   Internet connection

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/PS5-Alerts.git
    cd PS5-Alerts
    ```

2. **Install dependencies:**

    - Install Python dependencies (if any, add a `requirements.txt` if needed).
    - Install [woob](https://woob.tech/) as required by the project.

3. **Configure email notifications:**
    - Copy the example config and edit it:
        ```bash
        cp config.example config
        ```
    - Edit the `config` file to set your email credentials and recipient:
        ```
        [mail]
        login = <your_login>
        password = <your_password>
        sender = <sender_email>
        receiver = <receiver_email>
        ```

## Usage

Run the main script to start monitoring:

```bash
python3 main.py
```

**Tip:** To keep the script running in the background, use `screen` or `tmux`:

```bash
screen -S ps5-alerts python3 main.py
```

## How it works

-   The script checks each retailer for PS5 availability in a loop.
-   If a PS5 is found, an email notification is sent and the check interval increases.
-   If not, it continues checking every 30 minutes.

## Credits

Built using [woob](https://woob.tech/)

## License

MIT License. See LICENSE file.
