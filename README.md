# Machine-Learning-Bayesian-Algorithm-Packet-Inspection-webshell-discover
基于包检测和贝叶斯算法的webshell检查程序<br>
<br>
主文件:main.py<br>
port_name 指定网卡名称<br>
port_filter 制定过滤<br>
<br>
拆包器:listen_traffic.py<br>
主要用于拆包，提取HTTP请求中的特征。<br>
<br>
算法文件：machine_learning_model.py<br>
使用贝叶斯算法，对于shell学习。<br>
<br>
webshell文件夹:shell<br>
这里面是webshell文件,命名规则是 <normal\shell>-<文件类型>-<特征>-<文件编号>-<文件后缀>，例如:normal-php-code-3.php<br>

<br>
备注:不支持from-data检测,并且检测率并不高。<br>

<br>
测试情况<br>
告警信息:<br>

![image](https://github.com/SkyBlueEternal/Machine-Learning-Bayesian-Algorithm-Packet-Inspection-webshell-discover/blob/master/image/%E6%B5%8B%E8%AF%95%E5%91%8A%E8%AD%A6.png?raw=true)

![image](https://github.com/SkyBlueEternal/Machine-Learning-Bayesian-Algorithm-Packet-Inspection-webshell-discover/blob/master/image/%E6%B5%8B%E8%AF%95%E6%AD%A3%E5%B8%B8.png?raw=true)
