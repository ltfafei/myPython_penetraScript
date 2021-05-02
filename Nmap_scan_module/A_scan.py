#!/usr/bin/python
# -*- coding: GBK -*-

import nmap, sys

def A_scan(scan1):
    nm = nmap.PortScanner()
    # ����nmap����
    scan_result = nm.scan(hosts=scan1, arguments='-v -n -A')
    # ����ɨ�������Ż���ӡ
    for host, result in scan_result['scan'].items():
        if result['status']['state'] == "up":
            print('#' * 17 + 'Host��' + host + '#' * 17)
            # �²����ϵͳ��forѭ��������ӡ
            print('-' * 17 + '����ϵͳ�²�' + '-' * 17)
            for os in result['osmatch']:
                print('����ϵͳΪ��' + os['name'] + " " * 3 + '׼ȷ��Ϊ��'+ os['accuracy'])
            idno = 1
            try:
                for port in result['tcp']:
                    try:
                        print('-' * 17 + "TCP������ϸ��Ϣ" + '[' + str(idno) + ']' + '-' * 17)
                        idno += 1
                        print("TCP�˿ںţ�" + str(port))
                        try:
                            print("����" + result['tcp'][port]['name'])
                        except:
                            pass
                        try:
                            print("״̬��" + result['tcp'][port]['state'])
                        except:
                            pass
                        try:
                            print("�汾��" + result['tcp'][port]['version'])
                        except:
                            pass
                        try:
                            print("���͵İ���" + result['tcp'][port]['reason'])
                        except:
                            pass
                        try:
                            print("��Ʒ��" + result['tcp'][port]['product'])
                        except:
                            pass
                        try:
                            print("CPE��" + result['tcp'][port]['cpe'])
                        except:
                            pass

                        try:
                            print("������Ϣ��" + result['tcp'][port]['extrainfo'])
                        except:
                            pass
                        try:
                            print("�ű���" + result['tcp'][port]['script'])
                        except:
                            pass
                    except:
                        pass
            except:
                pass

            idno = 1
            try:
                for port in result['udp']:
                    try:
                        print('-' * 17 + "UDP������ϸ��Ϣ" + '[' + str(idno) + ']' + '-' * 17)
                        idno += 1
                        print("UDP�˿ںţ�" + str(port))
                        try:
                            print("����" + result['udp'][port]['name'])
                        except:
                            pass
                        try:
                            print("״̬��" + result['udp'][port]['state'])
                        except:
                            pass
                        try:
                            print("�汾��" + result['udp'][port]['version'])
                        except:
                            pass
                        try:
                            print("���͵İ���" + result['udp'][port]['reason'])
                        except:
                            pass
                        try:
                            print("��Ʒ��" + result['udp'][port]['product'])
                        except:
                            pass
                        try:
                            print("CPE��" + result['udp'][port]['cpe'])
                        except:
                            pass

                        try:
                            print("������Ϣ��" + result['udp'][port]['extrainfo'])
                        except:
                            pass
                        try:
                            print("�ű���" + result['udp'][port]['script'])
                        except:
                            pass
                    except:
                        pass
            except:
                pass

if __name__ == '__main__':
    A_scan('192.168.0.120')