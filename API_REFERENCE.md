# ZenRupee API Reference

This document provides a comprehensive list of all API endpoints available in the ZenRupee (Aegis Nexus Bank) platform.

## Authentication

### [POST] /api/login
Authenticates a user and starts a session.
- **Request Body**: `{"username": "...", "password": "..."}`
- **Response**: `{"success": true, "user": {...}}`

### [POST] /api/logout
Ends the current session.
- **Role**: Any logged-in user
- **Response**: `{"success": true}`

### [GET] /api/me
Returns current session user details.
- **Role**: Any logged-in user
- **Response**: `{"user_id": 1, "username": "...", "role": "..."}`

---

## Customer & Account Operations

### [GET] /api/accounts
Lists accounts. Customers see their own; Staff see all.
- **Role**: Any logged-in user
- **Response**: List of account objects.

### [GET] /api/accounts/<account_id>
Returns detailed information for a specific account.
- **Response**: Account object.

### [GET] /api/accounts/lookup/<account_id>
Public lookup (for transfers) showing only recipient name.
- **Response**: `{"account_id": 1, "customer_name": "..."}`

### [GET] /api/accounts/<account_id>/transactions
Fetches transaction history for an account.
- **Response**: List of transaction objects.

---

## Financial Transactions

### [POST] /api/deposit
Deposits money into an account.
- **Roles**: Customer, Manager
- **Request Body**: `{"account_id": 1, "amount": 1000, "category": "..."}`

### [POST] /api/withdraw
Withdraws money. Amounts ≥ ₹5,000 require Accountant approval.
- **Roles**: Customer, Manager
- **Request Body**: `{"account_id": 1, "amount": 1000}`

### [POST] /api/transfer
Transfers funds between accounts. Amounts ≥ ₹5,000 require approval.
- **Roles**: Customer, Manager
- **Request Body**: `{"src_id": 1, "dst_id": 2, "amount": 1000}`

---

## Staff & Management

### [GET] /api/requests
Lists pending approval requests (withdrawals, transfers, user creation).
- **Roles**: Accountant, Manager

### [POST] /api/requests/<request_id>/process
Approves or rejects a pending request.
- **Roles**: Accountant, Manager
- **Request Body**: `{"action": "approve" | "reject"}`
- *Note: User creation requests can only be processed by Managers.*

### [POST] /api/users/request-create
Accountant submits a new user for Manager approval.
- **Role**: Accountant
- **Request Body**: `{"username": "...", "password": "...", "role": "customer", ...}`

### [POST] /api/users/create
Direct user creation by a manager.
- **Role**: Manager
- **Request Body**: `{"username": "...", "password": "...", "role": "..."}`

### [GET] /api/dashboard/summary
Returns financial metrics and trends for the dashboard.
- **Role**: Any logged-in user (content adapts to role)

### [GET] /api/report
Generates a full bank balance and statistics report.
- **Role**: Manager

---

## Security & Logs

### [GET] /api/alerts
Fetches unread security alerts for the current user.
- **Response**: List of alerts.

### [GET] /api/audit-log
Fetches the global audit trail of all sensitive actions.
- **Role**: Accountant, Manager

### [GET] /api/system-logs
Fetches chronological system events and login logs.
- **Role**: Manager
