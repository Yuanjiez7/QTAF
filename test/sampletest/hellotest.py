# -*- coding: utf-8 -*-
'''
模块描述
'''
#2012-11-20  allenpan  - Created
#2013-01-15  aaronlai  - 已经没有htmlcontrols和htmlcontrols2模块，修改测试用例
#2013-01-15  aaronlnai - 空构造函数抛出TypeError
import testbase
import tuia.webcontrols as web
from testbase import logger
from testbase import context
import time
import threading
from testbase.testresult import EnumLogLevel

def _some_thread():
    logger.info('非测试线程打log, tid=%s' % threading.current_thread().ident)
    
class HelloTest(testbase.TestCase):
    '''测试示例
    '''
    owner = "allenpan"
    status = testbase.TestCase.EnumStatus.Ready
    timeout = 1
    priority = testbase.TestCase.EnumPriority.Normal
    
    def runTest(self):
        #-----------------------------
        self.startStep("测试webcontrols.WebElement构造函数")
        #-----------------------------
        self.assert_equal('断言失败', False, True)
        try:
            web.WebElement()
        except TypeError:
            pass
        except:
            self.fail("空构造函数没有抛出TypeError")
        
        #-----------------------------
        self.startStep("测试webcontrols.WebPage构造函数")
        #-----------------------------
        try:
            web.WebPage()
        except TypeError:
            pass
        except:
            self.fail("空构造函数没有抛出TypeError")
            
        
        logger.info("QTA日志", extra=dict(attachments={"qq.tlg":__file__, "qta.log": __file__}))
        
        #-----------------------------
        self.startStep("测试webcontrols.WebPage构造函数")
        #-----------------------------
        t1 = threading.Thread(target=_some_thread)
        t2 = threading.Thread(target=_some_thread)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        raise RuntimeError("XX")
    
    def get_extra_record(self):
        return {
            'screenshots':{
                'PC截图': __file__,
                '设备723982ef8截图':__file__,
            }
        }
        
class TimeoutTest(testbase.TestCase):
    '''超时示例
    '''
    owner = "eeelin"
    status = testbase.TestCase.EnumStatus.Ready
    timeout = 0.1
    priority = testbase.TestCase.EnumPriority.Normal
    
    def runTest(self):
        time.sleep(7)
        
class CrashTest(testbase.TestCase):
    '''发生Crash
    '''
    owner = "eeelin"
    status = testbase.TestCase.EnumStatus.Ready
    timeout = 0.1
    priority = testbase.TestCase.EnumPriority.Normal
    
    def runTest(self):
        context.current_testresult().log_record(EnumLogLevel.APPCRASH, "App Crash", attachments={'QQ12e6.dmp':__file__, 'QQ12e6.txt':__file__})
                
    
class App(object):
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def get_creenshot(self):
        return __file__
    
    
class QT4iTest(testbase.TestCase):
    '''QT4i测试用例
    '''
    #owner = "eeelin"
    status = testbase.TestCase.EnumStatus.Ready
    timeout = 0.1
    priority = testbase.TestCase.EnumPriority.Normal
    
    def initTest(self, testresult):
        super(QT4iTest,self).initTest(testresult)
        self._apps = []
        
    def runTest(self):
        self._apps.append(App("A"))
        self._apps.append(App("B"))
        raise RuntimeError("XXX")
    
    def get_extra_fail_record(self):
        attachments = {}
        for app in self._apps:
            attachments[app.name+'的截图'] = app.get_creenshot()
        return {},attachments
    
if __name__ == '__main__':
#     HelloTest().run()
#     CrashTest().debug_run()
    QT4iTest().debug_run()