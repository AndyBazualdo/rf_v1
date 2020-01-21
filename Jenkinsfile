pipeline {
    agent { label 'master'}
    stages {
        /*stage('local docker image') {
            agent {
                 docker { image 'gato756/rf_v1:latest' }
            }
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh "python -m robot.run --NoStatusRC /home/andy/tests/Outlook/test1.robot"
            }
        }
        stage('local docker-compose') {
            agent{ label 'master' }
            steps {
                sh 'pwd'
                sh 'ls -al'
                sh 'docker-compose up -d'
            }
        }
      stage('slave01'){
            agent{ label 'slave01' }
            steps{
                sh 'pwd'
                sh 'ls -la'
                sh "cd ./tests/Outlook/"
                sh 'pwd'
                sh 'ls -la'
                sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', passThreshold: 95.0, reportFileName: 'report.html', unstableThreshold: 5.0
            }*/

      stage('slave01 + docker approach'){
            agent{ label 'slave01' }
            steps{

                sh "docker run -d -p 4444:4444 --name selenium-hub selenium/hub"
                sh "docker run -d -P -p 5900:5900 --link selenium-hub:hub -e VNC_NO_PASSWORD=1 -v /dev/shm:/dev/shm selenium/node-chrome-debug"
                sh "docker run -d -P -p 5901:5900 --link selenium-hub:hub -e VNC_NO_PASSWORD=1 -v /dev/shm:/dev/shm selenium/node-firefox-debug"
                sleep(time:20,unit:"SECONDS")
                wrap([$class: 'Xvnc', takeScreenshot: false, useXauthority: false]) {
                //sh 'export DISPLAY=:0'
                //sh 'python startViewers.py'
                sh 'vncviewer localhost:5900 &'
                sh """sshpass -p 123 ssh -X -Y -C -g -L 5903:localhost:5900 jenkins@192.168.196.134 \\ vncviewer localhost:5900 &"""
                //sh 'sshpass -p 123 ssh -X -Y -C -g -L 5901:localhost:5901 jenkins@192.168.196.134 \ vncviewer localhost:5901'
                sh 'pwd'
                sh 'ls -la'
                sh 'python -m robot.run --NoStatusRC --variable SERVER:${CT_SERVER} --outputdir ./reports ./tests/Outlook/test1.robot'
                robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'reports', passThreshold: 95.0, reportFileName: 'report.html', unstableThreshold: 5.0
                sh 'docker-compose -f docker-compose1.yml down'
                sh 'docker stop $(docker ps -a -q)'
                sh 'docker rm $(docker ps -a -q) -f'
                }
            }
       }
  }
  post{
    always {
          /*sh 'docker-compose down'
          sh 'docker stop $(docker ps -a -q)'
          sh 'docker rm $(docker ps -a -q) -f'*/
        cleanWs deleteDirs: true, notFailBuild: true
    }
}
}
