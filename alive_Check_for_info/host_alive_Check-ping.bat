@echo off
echo ---------------------------------------
echo Author��afei
echo 
echo ��̽��IP��������check_IP.txt
echo ����ʹ��ping̽��Ŀ������...
echo ---------------------------------------

setlocal enabledelayedexpansion
for /f %%x in (check_IP.txt) do (
	ping -w 1 -n 1 %%x |findstr "TTL=" >nul
	if !errorlevel! equ 0 (
		echo %%x is alive && echo %%x >> alive_IP.txt) else (
		echo %%x is not alive��)
)
echo �����������̽����ɣ�
echo ���IP�����ڣ�alive_IP.txt

pause