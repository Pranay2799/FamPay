# Flask YouTube API Integration
This project is a simple Flask application that fetches and stores the latest YouTube videos related to a specific query using the YouTube Data API. It provides an API endpoint to retrieve the stored videos in a paginated response.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- YouTube Data API key
- 
### Installation
1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-youtube-api
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - **Windows:**
    
        ```bash
        venv\Scripts\activate
        ```
    
    - **Linux/macOS:**
    
        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install Flask Flask-SQLAlchemy requests
    ```

### Configuration

1. Create a file named `config.py` in the `instance` directory.
2. Add your YouTube Data API key to the `config.py` file:

    ```python
    # instance/config.py
    YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
    SEARCH_QUERY = 'Cricket'
    ```

### Running the Application

Run the following command to start the Flask application:

```bash
python run.py

