@echo off
echo ---------------------------------------
echo Author：afei
echo 
echo 需探测IP保存至：check_IP.txt
echo 正在使用ping探测目标主机...
echo ---------------------------------------

setlocal enabledelayedexpansion
for /f %%x in (check_IP.txt) do (
	ping -w 1 -n 1 %%x |findstr "TTL=" >nul
	if !errorlevel! equ 0 (
		echo %%x is alive && echo %%x >> alive_IP.txt) else (
		echo %%x is not alive！)
)
echo 存活主机批量探测完成！
echo 存活IP保存在：alive_IP.txt

pause