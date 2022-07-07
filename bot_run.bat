@echo off

call .\venv\Scripts\activate

set TOKEN=5348559790:AAGR9LtOzgPct0Znh2jToGAaVUlN0Sp9HGs
set DATABASE_URL=postgres://xwalkvymugyvti:2af68906922e284d5ef2a3b4f9f37bfb5cdd4cd1b8a29921372bc930979bab38@ec2-52-30-159-47.eu-west-1.compute.amazonaws.com:5432/d4fe9dau34qc0p

python bot_telegram.py

pause
