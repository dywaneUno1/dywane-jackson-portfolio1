-- Device Compliance Database Schema
-- Tracks device enrollment, OS versions, and compliance status
-- Author: Gwene Jackson

-- Drop existing tables if they exist
DROP TABLE IF EXISTS compliance_violations;
DROP TABLE IF EXISTS device_updates;
DROP TABLE IF EXISTS devices;
DROP TABLE IF EXISTS departments;

-- Departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    manager_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Devices table
CREATE TABLE devices (
    device_id INTEGER PRIMARY KEY,
    serial_number VARCHAR(50) UNIQUE NOT NULL,
    device_name VARCHAR(100),
    device_type VARCHAR(50) NOT NULL,
    model VARCHAR(100),
    os_version VARCHAR(20),
    enrollment_date DATE,
    last_check_in TIMESTAMP,
    department_id INTEGER,
    assigned_user VARCHAR(100),
    is_supervised BOOLEAN DEFAULT FALSE,
    is_compliant BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Compliance Violations table
CREATE TABLE compliance_violations (
    violation_id INTEGER PRIMARY KEY,
    device_id INTEGER NOT NULL,
    violation_type VARCHAR(100) NOT NULL,
    violation_description TEXT,
    detected_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_date TIMESTAMP,
    severity VARCHAR(20),
    is_resolved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

-- Sample data
INSERT INTO departments (department_id, department_name, manager_name) VALUES
(1, 'Engineering', 'Sarah Chen'),
(2, 'Marketing', 'Michael Rodriguez'),
(3, 'Operations', 'Jennifer Williams');
