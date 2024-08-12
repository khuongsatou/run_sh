chmod +x run.sh&./run.sh
chmod +x run_report.sh&./run_report.sh

# Prefix report:
test_Tên file.py

# Tạo báo cáo
pytest --cov=add --cov-report=html test_add.py