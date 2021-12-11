import java.io.*;

public class DeserializeTest {
public static void main(String[] args) throws Exception {
new ObjectInputStream(new BufferedInputStream(new FileInputStream("bingo.obj"))).readObject();
}
}
