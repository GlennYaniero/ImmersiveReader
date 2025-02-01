# Immersive Reader Integration

This repository contains a sample project demonstrating how to integrate Microsoft's Immersive Reader with a FastAPI backend and a JavaScript frontend.

## Author
Glenn Yaniero, Sensory Reflection

## Features

- Convert text into an immersive reading experience.
- Backend API using FastAPI.
- Frontend integration using the Immersive Reader JavaScript SDK.

## Prerequisites

- Python 3.6+
- Azure Cognitive Services account with Immersive Reader resource

## Setup

### Backend (FastAPI)

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/immersive-reader-integration.git
    cd immersive-reader-integration
    ```

2. Install the required Python packages:

    ```sh
    pip install fastapi uvicorn requests
    ```

3. Replace the placeholders `YOUR_IMMERSIVE_READER_ENDPOINT` and `YOUR_IMMERSIVE_READER_KEY` in `main.py` with your actual Azure Immersive Reader endpoint and key.

4. Run the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

### Frontend (JavaScript)

1. Open `immersive.html` in your preferred code editor.

2. Replace the placeholders `YOUR_ACCESS_TOKEN` and `YOUR_SUBDOMAIN` with your actual access token and subdomain.

3. Launch a local web server to serve the `immersive.html` file. You can use Python's built-in HTTP server for this:

    ```sh
    python -m http.server
    ```

4. Open your browser and navigate to `http://localhost:8000` to see the application in action.

## Usage

- Click the "Launch Immersive Reader" button to convert the sample text into an immersive reading experience.
- The backend FastAPI server will handle token generation and send the required data to the Immersive Reader API.

 
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Microsoft Immersive Reader](https://azure.microsoft.com/en-us/services/immersive-reader/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org
