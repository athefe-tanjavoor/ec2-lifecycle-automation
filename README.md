# 🚀 EC2 Lifecycle Automation using AWS Lambda & Boto3

This project automates the management of Amazon EC2 instances using **AWS Lambda** functions written in **Python** with the **Boto3** SDK. The automation covers the full EC2 lifecycle: creation, start, stop, termination, and cleanup of unnamed instances — with or without specific tags.

---

## 📌 Features

✅ Create EC2 instance with a specific `Name` tag (e.g., `Name=aatif`)  
✅ Create EC2 instance without a `Name` tag  
✅ Start EC2 instance using `Name` tag  
✅ Start EC2 instance **without** a `Name` tag  
✅ Stop EC2 instance using `Name` tag  
✅ Stop all running EC2 instances  
✅ Terminate EC2 instance using `Name` tag  
✅ Terminate all unnamed EC2 instances  
✅ Trigger Lambda functions using **Amazon EventBridge** (e.g., daily at 9 AM IST)

---

## 📂 Folder Structure

ec2-lifecycle-automation/
├── eventbridge_cron_info.md # Cron expressions for scheduled tasks
├── lambda_create_instance_with_tag_name.py # Creates EC2 instance with Name=TagName
├── lambda_create_instance_without_tag_name.py # Creates EC2 instance without Name tag
├── lambda_start_instance_with_tag_name.py # Starts EC2 instance with Name=TagName
├── lambda_start_instance_without_tag_name.py # Starts EC2 instance without Name tag
├── lambda_stop_instance_with_tag_name.py # Stops EC2 instance with Name=TagName
├── lambda_stop_all_instance.py # Stops all running EC2 instances
├── lambda_terminate_instance_with_tag_name.py # Terminates EC2 instance with Name=TagName
├── lambda_terminate_unnamed.py # Terminates all EC2 instances without Name tag
└── README.md

---

## 🔧 Technologies Used

- **AWS Lambda** – Serverless compute for automation logic  
- **Amazon EC2** – Compute service (target of the automation)  
- **Python** + **Boto3** – Used in Lambda to interact with EC2  
- **IAM** – Secure execution using least-privileged roles  
- **EventBridge** – For scheduled automation (e.g., daily at 9 AM)  
- **CloudWatch Logs** – For monitoring Lambda output  

---

## 🕘 Example Schedule with EventBridge

To run EC2 automation tasks like starting instances every day at **9:00 AM IST**, use this cron expression:

```bash
cron(30 3 * * ? *)  # 3:30 AM UTC = 9:00 AM IST
📌 Setup:

Go to Amazon EventBridge → Create Rule

Use Schedule pattern → cron

Set your Lambda function as the target

🛡️ IAM Permissions Required
Each Lambda function must use a role with the following permissions:

{
  "Effect": "Allow",
  "Action": [
    "ec2:DescribeInstances",
    "ec2:StartInstances",
    "ec2:StopInstances",
    "ec2:RunInstances",
    "ec2:TerminateInstances",
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
  ],
  "Resource": "*"
}
👨‍💻 Author
Aatif – DevOps enthusiast automating cloud infrastructure using AWS Lambda and Python.

📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute.