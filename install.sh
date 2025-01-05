#!/bin/bash

###################################
#     Yet Another pppwn suite     #
#           by ZaindORp           #
###################################

# A suite to install pppwn and a custom web ui to your linux device.
# Run this script as root.

install_path=/opt/pppwn

##########
if [ $(whoami) != 'root' ]; then
  echo "please run as root"
  exit 1
fi
##########
start=null
echo 'do you want to installation pppwn suite?'
echo 'this will modify your host, your init, your pppoe config'
echo "it's only suggested to install it to a device which is just designed to be used like this"
echo 'do you want to continue? (Y/N)'
while [ $start != 'Y' ] && [ $start != 'N' ]; do
  read start
  if [ $start != 'Y' ] && [ $start != 'N' ]; then
    echo "please input Y/N"
  fi
done
if [ $start == N ]; then
  echo "stopped"
    exit 0
fi
##########
echo "- copying files to ${install_path}..."
cp -r -p $(pwd)/* ${install_path}
##########
echo "- copying pppwn..."
case $(uname -m) in
  x86_64)
    cp ${install_path}/files/pppwn/x86_64/pppwn ${install_path}
    ;;
  armv7l)
    cp ${install_path}/files/pppwn/arm/pppwn ${install_path}
    ;;
  aarch64)
    cp ${install_path}/files/pppwn/aarch64/pppwn ${install_path}
    ;;
  mips)
    cp ${install_path}/files/pppwn/mips/pppwn ${install_path}
    ;;
  mipsel)
    cp ${install_path}/files/pppwn/mipsel/pppwn ${install_path}
    ;;
esac
##########
echo "- copying pppoe-server configs to /etc/ppp..."
cp -p ${install_path}/files/ppp/* /etc/ppp
##########
echo "- copying init files to /etc/init.d/S99pppwn"
echo "#!/bin/sh

PPPWNDIR=${install_path}

case \$1 in
  start)
    echo 'Starting pppwn'
    python \${PPPWNDIR}/app.py
    ;;
  stop)
    echo \"Stopping pppwn\"
    echo \"unrealized function\"
    ;;
  *)
    echo \"Usage: \$0 {start|stop}\"
    exit 1
    ;;
esac

exit 0" > /etc/init.d/S99pppwn
##########
echo "- making files executable..."
chmod +x ${install_path}/*.py
chmod +x /etc/init.d/S99pppwn
##########
echo "- setting hosts to block update and redirect user manual to the setting..."
echo  -e '\n# added by pppwn suite\n192.168.1.1\tmanuals.playstation.net\n127.0.0.1\tupdate.playstation.net\n127.0.0.1\tdl.playstation.net' >> /etc/hosts
##########
echo "- cleaning unused files..."
rm -r ${install_path}/files
##########
echo "- generate the config..."
echo "available interface are:
$(ip ad | grep \< | sed 's/^[0-9]\{1,\}: //' | sed 's/:.\{0,\}$//')"
echo "please enter the interface you wish to work with:"
read interface
echo "{interface:${interface}}" > ${install_path}/config.json
##########
echo "finished."
