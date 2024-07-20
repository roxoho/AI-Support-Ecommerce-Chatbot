# Installation Methods for Chatbot

## Method 1: Using a Virtual Environment (Recommended)

1. **Creating a Virtual Environment (to avoid unnecessary issues)**

    a. Open VS Code terminal or any other terminal and run the following command to create a virtual environment:

    ```sh
    python -m venv myenv
    ```

    b. Activate the Virtual Environment:

    - **Windows:** In the Command Prompt terminal, run:
    ```sh
    myenv\Scripts\activate
    ```

    - **MacOS and Linux:** Run:
    ```sh
    source myenv/bin/activate
    ```

2. **Unzip the `chatbot.zip` file** into the folder containing the `myenv` folder. The folder structure should resemble this:

    ```
    folder
    ├── myenv
    └── chatbot
    ```

3. **Navigate to the `chatbot` folder** in the terminal:

    ```sh
    cd chatbot
    ```

    a. **Install the dependencies:** Open the terminal and run:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    python app.py
    ```

    Ensure the virtual environment is activated in that terminal.

You are all set! Just follow the mentioned link and use the chatbot.

---

## Method 2: Not Using a Virtual Environment

1. **Unzip the folder** and open it in your code editor.

2. **Install the dependencies:** Open the terminal and run:

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```sh
    python app.py
    ```

You are all set! Just follow the mentioned link and use the chatbot.

---

## Alternative Method (Applicable to All Methods)

You can run the chatbot directly by uncommenting the last 4 lines of the `chatbot.py` file and running it:

```sh
python chatbot.py

Make sure to comment them again to use the web app and ensure you are in the chatbot directory in the terminal. 
