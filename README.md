# Discord Dad Jokes

A simple Python script that fetches dad jokes from a RapidAPI endpoint and sends them to a Discord channel using a webhook. This project demonstrates how to make API requests, process JSON responses, and interact with Discord's webhook system. It's a fun and lighthearted example of how you can integrate APIs and automate interactions in your Discord server.

## Features

- Fetches random dad jokes from a third-party API.
- Sends the setup and punchline of the joke to a Discord channel using a webhook.
- Handles potential errors gracefully to ensure smooth execution.

## Prerequisites

- Python 3.x
- Libraries: `json`, `requests`

## Getting Started

1. Clone the repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Replace the `BOT_URL` in the script with your own Discord webhook URL.
4. Replace the `X-RapidAPI-Key` value in the `headers` dictionary with your own RapidAPI key. You might need to make an account.
https://rapidapi.com/KegenGuyll/api/dad-jokes/

## Usage

1. Run the script, and it will fetch a random dad joke from the API.
2. The joke's setup and punchline will be printed to the console.
3. The setup and punchline will also be sent to the configured Discord channel using a webhook.

Feel free to customize and expand upon this project to fit your needs. You can enhance the bot by adding features like multiple jokes in a row, responding to user commands, or incorporating additional APIs.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
