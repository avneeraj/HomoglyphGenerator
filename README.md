# Homoglyph Generator
A Flask-based web application designed to generate homoglyph variants of input text to demonstrate IDN homograph attacks and keyword spoofing potential.

## Features

-   **Homoglyph Generation**: Uses a comprehensive mapping of characters to their look-alike counterparts (based on IronGeek's research).
-   **Web Interface**: Simple UI to input target words and view generated variants.
-   **API Support**: JSON endpoint (`/generate`) for programmatic access.
-   **Safety Limits**: Includes input length caps and generation limits to prevent resource exhaustion.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/avneeraj/HomoglyphGenerator.git
    cd HomoglyphGenerator
    ```

2.  **Install dependencies**:
    This project requires Python and Flask.
    ```bash
    pip install flask
    ```

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Access the interface**:
    Open your web browser and navigate to:
    `http://127.0.0.1:5000`

3.  **Generate Variants**:
    -   Enter a word (e.g., "paypal").
    -   Click "Generate".
    -   View the list of visually similar strings.

## API Usage

You can generate variants via a POST request:

```bash
curl -X POST http://127.0.0.1:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"word": "example"}'
```

## Structure

-   `app.py`: Main Flask application handling routes and API.
-   `homoglyphs.py`: Core logic containing the homoglyph character mapping and generation algorithm.
-   `templates/`: HTML templates for the web interface.
-   `static/`: Static assets (CSS/JS).

## Disclaimer

This tool is for **educational and defensive testing purposes only**. It is intended to help security researchers and administrators understand the risks associated with homoglyph attacks and to test systems for proper character handling. Do not use this tool for malicious purposes.
