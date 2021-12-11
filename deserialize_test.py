from java.io import FileInputStream, BufferedInputStream, ObjectInputStream
ois = ObjectInputStream(BufferedInputStream(FileInputStream("bingo.obj")))
aaa = ois.readObject()
