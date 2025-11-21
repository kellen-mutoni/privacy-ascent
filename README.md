# PRIVACY ASCENT – Mental Health Navigator

A lightweight offline mental-health assistant built with Python + MySQL.

## Overview

Privacy Ascent is a command-line-based, minimal menu-driven application designed to help users monitor, understand, and improve their mental well-being. It allows users to create accounts, monitor their state of mind, and access mental health resources.

## Problem Statement

Mental health challenges are increasingly common among students and young adults. However, many hesitate to use online mental health apps due to privacy concerns, data breaches, Social stigmas, and lack of data control.

**Privacy Ascent provides:**
- **Complete Privacy**: All data stored locally on your MySQL server
- **User Control**: You own all your data
- **Accessible**: Simple command-line interface, no complex setup or hidden costs
- **Offline Access**: No internet required after initial setup

## Key Features

- User authentication (register/login)
- Mood tracking with intelligent feedback
- Mental health resources by category
- Guest mode for resource browsing

## Requirements

- Python 3.12.3
- MySQL server
- mysql-connector-python


## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kellen-mutoni/privacy-ascent.git
cd privacy-ascent
```

### 2. Install Dependencies
```bash
pip install mysql-connector-python
```

### 3. Start MySQL Server
Before running `database.py`, confirm that your MySQL server is running. If MySQL is stopped, the script will fail with connection errors.
### Linux/Mac:
```
sudo service mysql status
```

If it's not active, run:
```
sudo service mysql start
```

### Windows:

1. Press Win + R, type services.msc
2. Find MySQL or MySQL80
3. Make sure the status is Running
4. Start it if necessary

### 4. Create Database User
```bash
mysql -u root -p
```
Then run:
```sql
CREATE USER 'health'@'localhost' IDENTIFIED BY 'Private123!';
GRANT ALL PRIVILEGES ON privacy_ascent.* TO 'health'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Create Database Tables
```bash
python3 database.py
```

### 6. Populate Sample Resources (Optional)
```bash
mysql -u health -p
# Password: Private123!
```
Copy and paste SQL commands from `./sample_resources.md`

### 7. Run the Application
```bash
python3 main.py
```
Enjoy using Privacy Ascent to track and improve your mental well-being!


## Developed By

- **Kellen Mutoni**
- **Prince Ganza**
- **Derrick Rugwiro**
- **Tiffany Turate**
- **Herve Rwigema**
