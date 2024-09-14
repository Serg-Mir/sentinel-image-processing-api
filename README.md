# Sentinel Image Processing API

This FastAPI application provides endpoints to process Sentinel-2 imagery based on provided coordinates and analyze image colors.

## Features

- Retrieve Sentinel-2 images for a given bounding box
- Analyze the main color of retrieved or uploaded images
- Three endpoints:
  1. Get Sentinel image
  2. Get Sentinel image with main color analysis
  3. Upload and analyze image color

Note: For detailed API documentation with example outputs, please see [API Documentation](docs/API_DOCUMENTATION.md).


## Prerequisites

- Python 3.8+
- Sentinel Hub account (for API credentials)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Serg-Mir/sentinel-image-processing-api.git
   cd sentinel-image-processing-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. For development, install additional packages:
   ```
   pip install -r requirements-dev.txt
   ```

5. Create a `.env` file in the project root and add your Sentinel Hub credentials:
   ```
   SH_CLIENT_ID=your_client_id_here
   SH_CLIENT_SECRET=your_client_secret_here
   ```

## Usage

1. Start the FastAPI server:
   ```
   python run.py
   ```
   or

   ```
   uvicorn app.main:app --reload
   ```

2. Access the API endpoints:
   - Get Sentinel image: `GET /api/image?bbox=min_lon,min_lat,max_lon,max_lat`
   - Get Sentinel image with color: `GET /api/image-with-color?bbox=min_lon,min_lat,max_lon,max_lat`
     - The image will be returned as the response body
     - The main color will be included in the `X-Main-Color` response header
   - Upload and analyze image: `POST /api/upload-image` (multipart form data)

3. Visit `http://localhost:8000/docs` for the interactive API documentation.


## Development

### Running Tests

To run the tests, use the following command:

```
pytest
```

For test coverage report:

```
pytest --cov=app tests/ --cov-report=xml
```

## Project Structure

```
sentinel-image-processing-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── services/
│   └── utils/
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── screenshot_endpoint1.png
│   ├── screenshot_endpoint2.png
│   └── screenshot_endpoint3.png
├── tests/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── run.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
Before starting to contribute to this project, please install `pre-commit` to make
sure your changes get checked for style and standards before committing them to repository:

    $ pip install pre-commit

    $ pre-commit install

### Code Formatting and Linting

This project uses `black` for code formatting, `mypy` for type checking, and `pre-commit` for managing hooks.


## License

This project is licensed under the Apache License, Version 2.0. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Acknowledgements

This project makes use of the Sentinel Hub API for retrieving satellite imagery. I am thankful to the Sentinel Hub team for their excellent service.
