# Python Server Monitoring Project

## Project Overview
This project monitors server CPU utilization using Python and JSON.

It reads server information from a JSON file and checks CPU usage to identify server health status.

## Technologies Used

- Python 3
- JSON
- Git
- GitHub
- VS Code

## Project Structure

```text
python-practices/
│
├── test.py
├── server.json
└── README.md
```

## Monitoring Logic

CPU Usage Status:
- Above 80%: CRITICAL
- Above 65% and up to 80%: WARNING
- 65% or below: NORMAL

## How to Run

1. Install Python 3.
2. Clone this repository.
3. Open the project folder in Terminal.
4. Run:

```bash
python3 test.py
```

## Sample Output

```text
NORMAL: webserver
CRITICAL: database
WARNING: app
```

## Learning Outcomes

- Reading JSON files using Python
- Using loops and conditional statements
- Monitoring server CPU utilization
- Managing project code using Git and GitHub

## Author
Python and DevOps Learning Project
