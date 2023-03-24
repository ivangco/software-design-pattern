# genera las claves privadas y publicas (si es que no existen)
ssh-keygen -b 4096

#enviar la clave publica al servidor remoto
scp ~/.ssh/id_rsa.pub webdesa@192.168.18.53:/home/webdesa/uploaded_key.pub

#agregar la clave publica en el servidor remoto
##generar archivo si no existe
touch .ssh/authorized_keys 


#otorgar permisos al archivo creado
chmod 600 .ssh/authorized_keys
#copiar clave publica en el archivo creado
echo `cat ~/uploaded_key.pub` >> ~/.ssh/authorized_keys
#borrar clave enviada
rm uploaded_key.pub
#reestableser servicio ssh
sudo service sshd restart


#enviar archivo desde la maquina locall sin credenciales
sftp webdesa@192.168.18.53:<la ruta de destino> <<< $'put <la ruta del archivo a enviar>'