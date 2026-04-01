<div align="center">

# 🏦 Bank Security System & Finance Dashboard Backend

**A secure, structured backend engineered to handle banking operations, financial data processing, role-based access control, and dashboard summaries.**

Built with Python · Flask · SQLite

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br>
</div>

---

## ✨ Overview

This project is a powerful **Finance Data Processing and Access Control Backend** designed to serve financial records, execute complex access constraints based on user roles, and generate high-level dashboard analytics. 

It satisfies rigorous backend engineering requirements by enforcing strict data segregation, providing comprehensive Record CRUD capabilities, supporting multi-layered Role-Based Access Control (RBAC), and using SQLite for lightweight but completely segregated persistence.

---

## 🎯 Core Features & Capabilities

### 1. Robust Role-Based Access Control (RBAC)
The system operates on a precisely segregated permissions model:
- **👤 Customer (Viewer):** Can only view their own dashboard data, fetch personal accounts, and initiate basic transactions securely for their own profiles.
- **📋 Accountant (Analyst):** Has elevated access to view all financial records, review and execute pending withdrawal/transfer requests from customers, and view audit trail logs.
- **👑 Manager (Admin):** Possesses complete CRUD capabilities. Can view all system logs, modify any user data, manage active branches, run global backend analytics, and explicitly manipulate financial records.

### 2. Advanced Financial Records Management
Financial entities (`transactions`) are fully fleshed out with metadata:
- **Record Data:** Supports storing `Amount`, `Type` (Deposit/Withdrawal/Transfer), `Category` (e.g., Salary, Rent, General), `Date` (timestamp), and custom `Notes` / `Descriptions`.
- **Full CRUD & Filtering:** Features a `GET /api/transactions` endpoint supporting dynamic filtering by `category`, `txn_type`, `start_date`, and `end_date`. Admins have explicit access to `PUT` and `DELETE` endpoints to manipulate these records directly.

### 3. Dashboard Summary APIs
Provides an aggregated analytics API (`GET /api/dashboard/summary`) that delivers immediate insights without frontend calculations:
- Calculates **Total Income** & **Total Expenses**.
- Computes **Net Balance**.
- Groups and calculates **Category-wise totals**.
- Computes **Monthly / Weekly financial trends** chronologically.
- Streams **Recent Activity**.

### 4. Data Segregation & Persistence
Instead of a single monolithic database containing highly sensitive information beside application logs, the persistence layer relies on three completely isolated SQLite files:
- `customers.db`: Houses Accounts and Financial Records.
- `accountants.db`: Manages Approval queues and rigid Audit Logs.
- `managers.db`: Controls the User identities, Authentication credentials, System Logs, and active Sessions.

### 5. Validation and Security
- All sensitive API routes are guarded with strict `@role_required` decorators preventing privilege escalation.
- Passwords safely hashed via `SHA-256`.
- Server-side Session management blocks impersonation.
- Failed authentication attempts trigger account locking mechanisms (Alerting Admins after 3 failed attempts).
- Large operations (> ₹5,000) trigger automatic holds and require `Accountant` review.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/sarthakpapneja/banksecuritysystem.git
cd banksecuritysystem

# Install all backend requirements
pip install -r requirements.txt

# Initialize the databases & Seed demo data
python3 seed_data.py
```

### Running the Backend

Start the central Flask server to expose the API on `http://localhost:5005`:

```bash
python3 server.py
```

### Demo Credentials

| Role | Username | Password |
|------|----------|----------|
| 👤 Customer | `john_doe` | `password123` |
| 📋 Accountant | `acc_smith` | `password123` |
| 👑 Manager | `mgr_admin` | `admin123` |

---

## 📁 System Architecture

```text
bank_security_system/
├── server.py          # Central point for routing, rate limiting, and REST delivery
├── db_manager.py      # Abstracted database interactions orchestrating the 3 SQLites
├── auth.py            # Security & session/hash implementations
├── models.py          # Enums & Data structure formatting
├── seed_data.py       # Auto-generator for default state schemas
│
└── data/              # Ephemeral/Persistent DB local storage
    ├── customers.db   
    ├── accountants.db 
    └── managers.db    
```

---

## 📝 API Endpoint Highlights

| Method | Endpoint | Role Restriction | Capability Focus |
|--------|----------|------|-------------|
| **POST** | `/api/login` | *Public* | Validates Hash & provisions session boundaries. |
| **GET**  | `/api/dashboard/summary` | *All* (Logic varies) | Aggregates income, expenses, and monthly trends scoped to the caller's role. |
| **GET**  | `/api/transactions` | *All* | Retrieves records with optional `category` and `type` queries. |
| **POST** | `/api/transactions` | Manager | Explicitly inserts a new categorized financial record manually. |
| **PUT**  | `/api/transactions/:id` | Manager | Updates the metadata (Category, Amount, Description) on existing records. |
| **DELETE**| `/api/transactions/:id` | Manager | Deletes a record directly from the database schema. |
| **POST** | `/api/requests/:id/process` | Analyst/Admin | Evaluates & processes pending large transfer holds. |
| **POST** | `/api/users/create` | Admin | Explicitly creates new users bypassing public systems. |

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

<div align="center">
<b>Made by Sarthak Papneja</b>
</div>
