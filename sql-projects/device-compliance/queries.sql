-- Device Compliance Analysis Queries
-- Author: Gwene Jackson

-- Overall compliance rate
SELECT 
    COUNT(*) as total_devices,
    SUM(CASE WHEN is_compliant = TRUE THEN 1 ELSE 0 END) as compliant_count,
    ROUND(100.0 * SUM(CASE WHEN is_compliant = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) as compliance_percentage
FROM devices;

-- Active violations by severity
SELECT 
    severity,
    COUNT(*) as violation_count
FROM compliance_violations
WHERE is_resolved = FALSE
GROUP BY severity
ORDER BY 
    CASE severity
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
    END;
