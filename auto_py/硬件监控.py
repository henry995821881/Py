Python监控CPU情况

1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
"""

#!/usr/bin/python
import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid + '|grep Raw|grep Cpu|grep -v Kernel').read().split('\n')[:-1]
        return sn1
                                                                
def getDate(host):
        items = getAllitems(host, '.1.3.6.1.4.1.2021.11')
                                                                
        date = []
        rate = []
        cpu_total = 0
        #us = us+ni, sy = sy + irq + sirq
        for item in items:
                float_item = float(item.split(' ')[3])
                cpu_total += float_item
                if item == items[0]:
                        date.append(float(item.split(' ')[3]) + float(items[1].split(' ')[3]))
                elif item == item[2]:
                        date.append(float(item.split(' ')[3] + items[5].split(' ')[3] + items[6].split(' ')[3]))
                else:
                        date.append(float_item)
                                                                
        #calculate cpu usage percentage
        for item in date:
                rate.append((item/cpu_total)*100)
                                                                
        mean = ['%us','%ni','%sy','%id','%wa','%cpu_irq','%cpu_sIRQ']
                                                                
        #calculate cpu usage percentage
        result = map(None,rate,mean)
        return result
                                                                
if __name__ == '__main__':
        hosts = ['192.168.10.1','192.168.10.2']
        for host in hosts:
                print '==========' + host + '=========='
                result = getDate(host)
                print 'Cpu(s)',
                #print result
                for i in range(5):
                        print ' %.2f%s' % (result[i][0],result[i][1]),
                print
                print

Python监控系统负载
1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
"""

#!/usr/bin/python
import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')
        return sn1
                                                                     
def getload(host,loid):
        load_oids = '1.3.6.1.4.1.2021.10.1.3.' + str(loid)
        return getAllitems(host,load_oids)[0].split(':')[3]
                                                                     
if __name__ == '__main__':
        hosts = ['192.168.10.1','192.168.10.2']
        #check_system_load
        print '==============System Load=============='
        for host in hosts:
                load1 = getload(host, 1)
                load10 = getload(host, 2)
                load15 = getload(host, 3)
                print '%s load(1min): %s ,load(10min): %s ,load(15min): %s' % (host,load1,load10,load15)

Python监控网卡流量
1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
"""
#!/usr/bin/python
import re
import os
#get SNMP-MIB2 of the devices
def getAllitems(host,oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
        return sn1
                                                                                      
#get network device
def getDevices(host):
        device_mib = getAllitems(host,'RFC1213-MIB::ifDescr')
        device_list = []
        for item in device_mib:
                if re.search('eth',item):
                        device_list.append(item.split(':')[3].strip())
        return device_list
                                                                                      
#get network date
def getDate(host,oid):
        date_mib = getAllitems(host,oid)[1:]
        date = []
        for item in date_mib:
                byte = float(item.split(':')[3].strip())
                date.append(str(round(byte/1024,2)) + ' KB')
        return date
                                                                                      
if __name__ == '__main__':
        hosts = ['192.168.10.1','192.168.10.2']
        for host in hosts:
                device_list = getDevices(host)
                                                                                      
                inside = getDate(host,'IF-MIB::ifInOctets')
                outside = getDate(host,'IF-MIB::ifOutOctets')
                                                                                      
                print '==========' + host + '=========='
                for i in range(len(inside)):
                        print '%s : RX: %-15s   TX: %s ' % (device_list[i], inside[i], outside[i])
                print


Python监控磁盘

1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
"""
#!/usr/bin/python
import re
import os
def getAllitems(host,oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
        return sn1
                                                             
def getDate(source,newitem):
        for item in source[5:]:
                newitem.append(item.split(':')[3].strip())
        return newitem
                                                             
def getRealDate(item1,item2,listname):
        for i in range(len(item1)):
                listname.append(int(item1[i])*int(item2[i])/1024)
        return listname
                                                             
def caculateDiskUsedRate(host):
        hrStorageDescr = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageDescr')
        hrStorageUsed = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageUsed')
        hrStorageSize = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageSize')
        hrStorageAllocationUnits = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageAllocationUnits')
                                                             
        disk_list = []
        hrsused = []
        hrsize = []
        hrsaunits = []
                                                             
        #get disk_list
        for item in hrStorageDescr:
                if re.search('/',item):
                        disk_list.append(item.split(':')[3])
        #print disk_list      
                                                             
        getDate(hrStorageUsed,hrsused)
        getDate(hrStorageSize,hrsize)
        #print getDate(hrStorageAllocationUnits,hrsaunits)
                                                             
        #get hrstorageAllocationUnits
        for item in hrStorageAllocationUnits[5:]:
                hrsaunits.append(item.split(':')[3].strip().split(' ')[0])
        #caculate the result
        #disk_used = hrStorageUsed * hrStorageAllocationUnits /1024 (KB)
        disk_used = []
        total_size = []
        disk_used = getRealDate(hrsused,hrsaunits,disk_used)
        total_size = getRealDate(hrsize,hrsaunits,total_size)
                                                             
        diskused_rate = []
        for i in range(len(disk_used)):
                diskused_rate.append(str(round((float(disk_used[i])/float(total_size[i])*100), 2)) + '%')
                                                             
        return diskused_rate,disk_list
                                                             
if __name__ == '__main__':
        hosts = ['192.168.10.1','192.168.10.2']
        for host in hosts:
                result = caculateDiskUsedRate(host)
                diskused_rate = result[0]
                partition = result[1]
                print "==========",host,'=========='
                for i in range(len(diskused_rate)):
                        print '%-20s used: %s' % (partition[i],diskused_rate[i])
                print


Python监控内存(swap)的使用率


1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装
'''
#!/usr/bin/python
import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
        return sn1
                                                                            
def getSwapTotal(host):
        swap_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalSwap.0')[0].split(' ')[3]
        return swap_total
                                                                            
def getSwapUsed(host):
        swap_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailSwap.0')[0].split(' ')[3]
        swap_total = getSwapTotal(host)
        swap_used = str(round(((float(swap_total)-float(swap_avail))/float(swap_total))*100 ,2)) + '%'
        return swap_used
                                                                            
def getMemTotal(host):
        mem_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalReal.0')[0].split(' ')[3]
        return mem_total
                                                                            
def getMemUsed(host):
        mem_total = getMemTotal(host)
        mem_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailReal.0')[0].split(' ')[3]
        mem_used = str(round(((float(mem_total)-float(mem_avail))/float(mem_total))*100 ,2)) + '%'
        return mem_used
                                                                            
if __name__ == '__main__':
        hosts = ['192.168.10.1','192.168.10.2']
        print "Monitoring Memory Usage"
        for host in hosts:
                mem_used = getMemUsed(host)
                swap_used = getSwapUsed(host)
                print '==========' + host + '=========='
                print 'Mem_Used = %-15s   Swap_Used = %-15s' % (mem_used, swap_used)
                print