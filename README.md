# Python Web API

A simple FastAPI server for everbliss assessments

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the Server

Option 1 - Direct Python:
```bash
python app.py
```

Option 2 - Python module:
```bash
python -m uvicorn app:app --reload
```

Option 3 - Uvicorn command (if uvicorn is in your PATH):
```bash
uvicorn app:app --reload
```

The server will start on `http://localhost:8000`

## API Endpoints & Test Cases

### 1. Add Numbers
- **Endpoint:** `POST /add_numbers`
- **Request JSON:**
  ```json
  { "a": 5, "b": 3 }
  ```
- **Response JSON:**
  ```json
  { "result": 8 }
  ```
- **Missing Field Example:**
  ```json
  { "a": 5 }
  ```
  **Response:**
  ```json
  { "detail": ["Field 'b' is required"] }
  ```
- **Invalid Payload Example:**
  ```json
  { "a": 0, }
  ```
  **Response:**
  ```json
  { "detail": ["Invalid request payload please check request body"] }
  ```

### 2. Subtract Numbers
- **Endpoint:** `POST /subtract_numbers`
- **Request JSON:**
  ```json
  { "a": 10, "b": 4 }
  ```
- **Response JSON:**
  ```json
  { "result": 6 }
  ```

### 3. Concatenate Strings
- **Endpoint:** `POST /concat_strings`
- **Request JSON:**
  ```json
  { "s1": "foo", "s2": "bar" }
  ```
- **Response JSON:**
  ```json
  { "result": "foobar" }
  ```
- **Invalid Type Example:**
  ```json
  { "s1": 123, "s2": "bar" }
  ```
  **Response:**
  ```json
  { "detail": ["Invalid request payload please check request body"] }
  ```

### 4. Remove Substring
- **Endpoint:** `POST /remove_substring`
- **Request JSON:**
  ```json
  { "s": "hello world", "substr": "world" }
  ```
- **Response JSON:**
  ```json
  { "result": "hello " }
  ```

## Interactive API Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI documentation and to test endpoints interactively.

## Notes
- All endpoints expect JSON payloads.
