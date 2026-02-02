# Animals Web Generator 

This project generates a simple HTML website that displays information about animals using data fetched from the **API Ninjas Animals API**.

The user is prompted to enter an animal name (for example, `Fox` or `Monkey`), and the program fetches relevant animal data from the API and dynamically generates an `animals.html` webpage.

The project demonstrates:

- Working with external APIs
- Handling user input
- Separating code into logical modules
- Generating HTML using Python
- Managing secrets with environment variables

---

## Features

- Fetches animal data from a real-world API
- Generates an HTML page with animal cards
- Handles invalid or non-existent animal names gracefully
- Uses environment variables to protect API keys
- Clean, modular architecture (data fetching separated from website generation)

---

## Project Structure

```
Zootopia with APIs/
│
├── animals_web_generator.py   # Main program (website generator)
├── data_fetcher.py            # Fetches data from the API
├── animals_template.html      # HTML template
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Ignored files (e.g. .env)
└── .env                       # API key (not committed)
```

---

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd Zootopia-with-APIs
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API key:

```
API_NINJAS_KEY=your_api_key_here
```

---

## Usage

Run the program with:

```bash
python animals_web_generator.py
```

You will be prompted to enter an animal name:

```
Enter a name of an animal: Fox
```

After running successfully, an `animals.html` file will be generated. Open it in your browser to view the results.

If the animal does not exist, the website will display a friendly error message.

---

## Requirements

- Python 3.8+
- requests
- python-dotenv

---

## Contributing (Optional)

Contributions are welcome! Feel free to:

- Open issues
- Submit pull requests
- Improve styling or functionality

---

## License

We welcome contributions! If you'd like to contribute to this project, please contact.
