# TableRunner
Web app for detailed, automated TTRPG travel in an overworld.

## Development

Install dependencies and run the Flask app:

```bash
pip install -r requirements.txt
python app.py
```

## Deployment on Render

This repository includes a `render.yaml` file for deploying to [Render](https://render.com). Create a new Web Service using this repo and Render will automatically install the dependencies and start the server with Gunicorn.
