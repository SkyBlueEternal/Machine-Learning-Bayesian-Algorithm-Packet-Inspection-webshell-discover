# coding = utf-8
from urllib.parse import unquote
from scapy.all import *
try:
    # This import works from the project directory
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http
import machine_learning_model


class ListenTraffic():
    def __init__(self):  # 检测到通过第一个数据包的时候加载算法
        self.model = machine_learning_model.shell_detect()
        if isinstance(self.model,machine_learning_model.shell_detect): #machine_learning_model.shell_detect
            print(u"贝叶斯算法加载完成，引擎启动")
        else:
            print(u"贝叶斯算法加载失败。")

    def __result__(self, packet):  # POST 和GET 请求分别处理
        self.http_request = packet
        try:
            self.Method = self.http_request["HTTPRequest"].Method
        except:
            pass
        else:
            if self.Method in b"POST":
                http_request = unquote(str(self.http_request["Raw"].load), 'utf-8')
                self.model.try_classify(unquote(http_request, 'utf-8'))
            elif self.Method in b"GET":
                http_request = self.http_request["HTTPRequest"].Path
                http_request = unquote(str(http_request),'utf-8')
                self.model.try_classify(unquote(http_request,'utf-8'))

    def __flow_separa__(self, packet):  # 区分POST 和GET
        if "POST" in str(packet):
            return packet
            # return packet
        elif "GET" in str(packet):
            return packet
            # return packet
        else:pass

    def run(self, port_name, port_filter):  # 运行监听
        sniff(
            iface=port_name,
            prn=self.__result__,
            lfilter=lambda p: self.__flow_separa__(p),
            filter=port_filter   # 设置端口为 tcp port 80 和8080
        )
