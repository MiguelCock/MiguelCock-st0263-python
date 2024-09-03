# info de la materia: ST0263-242 Topicos de telematica

# Estudiante: Miguel Cock, <macockc@eafit.edu.co>

# Pofesor: Alvaro Enrique Ospina Snajuan, <aeospinas@eafit.edu.co>

# P2P con gRPC y CHORD

# 1. breve descripción de la actividad

Desarrollo de una res distribuida de nodos p2p utilizando la arquitectura de **DHT** de **CHORD** para la busqueda rapida y organizacion de la informacion

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se utilizo gRPC para toda la comunicacion, no utilce REST ya que me reducia el tiempo para entender la tecnologia de gRPC y ya que es mas lento en terminos generales que este, para que se pudiera lograr una mayor velocidad de envio de mensajes.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

No se logro que se mantuviera la consistencia del anillo de chord con los predecesores y antecesores como se especifica en la logica aunque si se logro una forma de este, se implemento parte de la funcionalidad de la finguer table pero tampoco es utilizada, se logro que los peer se conecten entre ellos y se manden informacion pero no se mandan archivos. Se logra guardar la informacion de los peer a los que uno esta conectado.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas

Se separo gran parte de las funcionalidades de la aplicacion para el trabajo agile de este, separandola en 3 instancias, la coneccion del usuario a la red, el inicio del servidor y las acciones que el usuario puede hacer con este, dejando un archivo unico para cada una de estas partes, siendo el archivo bootstrap el que contiene metodos para conectarse a los otros peer y darles informacion. Por otro lado, el archivo listen es el que inicia el servidor con la clase Peer en la cual se implementan los metodos de respuesta a las llamadas al servidor. Y en user_action se implementan las diferentes acciones que puede hacer un usuario como guardar un archivo, preguntar a otros peer por archivos y mirar el estado de la finger table.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones

Al inicio quería usar go para el desarrollo y es la razón por la que no estoy en equipo con alguien, pero porque se daño el cargador de mi PC me toco migrar a python para el cumplimiento de la actividad.

Solo se utilizo gRPC para la comunicación entre peers.

python version: 3.11
Protobuf version: 5.28
GRPC version: 1.66.1

## como se compila y ejecuta

``` bash
python -m pip install gprcio

pip install gprcio-tools

python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. p2p.proto

python <ip> <port>
```

## detalles del desarrollo

## detalles técnicos

Se logro entender en rasgos generales la implementacion de Chord anque no se pudiera implementar en su totalidad

Se logro entender la libreria de gRPC para la implementacion de las comunicaciones

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

Todo se pide por consola.

``` bash
python <ip> <port>
```

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

No se requiere crear directorios mas alla del directorio donde se encuentran los archivos

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones

# IP o nombres de dominio en nube o en la máquina servidor

En mi caso no tuve tiempo para probarlo en aws pero no es tan diferente de la maquina virtual de google con la que lo testeaba, toca eso si en aws abrir las gateways y pedir ips reservadas pero por la falta de tiempo y herramientas termine haciendo todo el testeo de la aplicacion en local host haciendo que cada puerto diferenciara el peer.

## una mini guia de como un usuario utilizaría el software o la aplicación

una vez se ejecuta la aplicacion en diferentes computadores/local la aplicacion misma pedira al usuario por la informacion necesaria para su ejecucion.

# 5. otra información que considere relevante para esta actividad

## VIDEO

# referencias

## <https://grpc.io/docs/languages/python/quickstart/>

## <https://github.com/grpc/grpc>

## <https://replit.com/@MiguelKokc/p2p-py#p2p.proto>

## <https://chatgpt.com/>

## <https://chatgpt.com/share/30520c0e-6465-429c-aba9-d03d447d728f>

## <https://chatgpt.com/share/98d8e633-c822-4039-a501-8968542ae405>
