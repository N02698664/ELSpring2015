#!/bin/bash

### BEGIN INIT INFO
#Provides:                      monitor
#Required-Start:          $remote_fs, $syslog
#Required-Stop:                  $remote_fs, $syslog
#Default-Start:                  2 3 4 5
#Default-Stop:                  0 1 6
#Short-Description:        pyinotify monitoring service
#Description:                    this service monitors for new picture files in the OpenCV folder and executes a python script to process them
### END INIT INFO


DIR=/home/pi/
DAEMON=$DIR/monitor.py
DAEMON_NAME=monitor

DAEMON_USER=pi

PIDFILE=/var/run/$DAEMON_NAME.pid

. /lib/lsb/init-functions

do_start()
{
        log_daemon_msg "Starting pyinototify monitor daemon"
        start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --startas $DAEMON
        log_end_msg $?
}

do_stop()
{
        log_daemon_msg "Stopping pyinotify monitor daemon"
        start-stop-daemon --stop --pidfile $PIDFILE --retry 10
        log_end_msg $?
}

case $1 in

        start|stop)
                do_${1}
                ;;

        restart|reload|force-reload)
                do_stop
                do_start
                ;;

        status)
                status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
                ;;

        *)
                echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
                exit 1
                ;;

esac

exit 0
