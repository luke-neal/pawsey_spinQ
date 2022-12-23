# SpinQ Web-Hosted Quantum Computing Training

Developed by Luke Antoncich & Eric Pan
Supervisor: Edric Matwiejew

# How to Run Locally

1. Make sure you have Python installed:

    ```
    python3
    ```

2. Create a Virtual Environment:

    MacOS/Linux

    ```
    python3 -m venv venv
    ```

    Windows

    ```
    py -m venv venv
    ```

3. Activate the venv:

    MacOS/Linux

    ```
    . venv/bin/activate
    ```

    Windows

    ```
    venv\Scripts\activate
    ```

4. Install the Requirements:

    ```
    pip install -r requirements.txt
    ```

5. Run the Application:

    Development
    ```
    flask run
    ```
    Production
    ```
    gunicorn -w 1 app:app
    ```