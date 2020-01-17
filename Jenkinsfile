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
                sh "docker run -d -P -p 5900:5900 --link selenium-hub:hub -v /dev/shm:/dev/shm selenium/node-chrome-debug"
                sh "docker run -d -P -p 5901:5900 --link selenium-hub:hub -v /dev/shm:/dev/shm selenium/node-firefox-debug"
                sleep(time:20,unit:"SECONDS")
                sh 'vncviewer localhost:5901 -passwd < (vncpasswd -f <<<"secret")'
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
  post{
    always {
          /*sh 'docker-compose down'
          sh 'docker stop $(docker ps -a -q)'
          sh 'docker rm $(docker ps -a -q) -f'*/
        cleanWs deleteDirs: true, notFailBuild: true
    }
}
}
