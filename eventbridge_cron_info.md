# 📅 Amazon EventBridge Cron Expressions for EC2 Automation

This file contains all cron expressions used to schedule EC2 lifecycle automation using AWS Lambda.

---

## 🕘 IST to UTC Conversion Reference

Amazon EventBridge uses **UTC**, so you must convert your IST time.  
🧠 Example: 9:00 AM IST = 3:30 AM UTC

---

## 🔄 Scheduled Lambda Actions

### 🔹 Start EC2 (with Name=TagName) daily at 9:00 AM IST
- **Cron (UTC):** `cron(30 3 * * ? *)`
- **Lambda:** `lambda_start_instance_with_tag_name.py`
- **Use case:** Start tagged EC2 instance every morning

---

### 🔹 Stop EC2 (with Name=TagName) daily at 6:00 PM IST
- **Cron (UTC):** `cron(30 12 * * ? *)`
- **Lambda:** `lambda_stop_instance_with_tag_name.py`
- **Use case:** Stop tagged EC2 instance every evening

---

### 🔹 Start EC2 (without Name tag) daily at 9:00 AM IST
- **Cron (UTC):** `cron(30 3 * * ? *)`
- **Lambda:** `lambda_start_instance_without_tag_name.py`
- **Use case:** Start unnamed EC2s automatically

---

### 🔹 Terminate all EC2 (without Name tag) every Sunday at 7:00 PM IST
- **Cron (UTC):** `cron(30 13 ? * SUN *)`
- **Lambda:** `lambda_terminate_unnamed.py`
- **Use case:** Weekly cleanup of untagged EC2s

---

## 📘 Cron Format (AWS EventBridge)

```text
cron(Minutes Hours Day-of-month Month Day-of-week Year)

All times are in UTC

Use ? when either Day-of-month or Day-of-week is not used

You can schedule hourly, daily, weekly, etc.

💡 Tips:

Test Lambda manually before linking to EventBridge

Use dead-letter queues (DLQ) for error handling

Always apply IAM least-privilege roles for Lambda functions

